"""A script that enables exiting Amazon WorkSpaces by pressing CAPS LOCK"""
import logging

from win32con import WM_KILLFOCUS, VK_MEDIA_PLAY_PAUSE, VK_CAPITAL
import win32api
import win32gui

import pyWinhook as pyHook


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def OnKeyboardEvent(event):
    logger.debug("MessageName: %s" % event.MessageName)
    logger.debug("Message: %s" % event.Message)
    logger.debug("Time: %s" % event.Time)
    logger.debug("Window: %s" % event.Window)
    logger.debug("WindowName: %s" % event.WindowName)
    logger.debug("Ascii: %s" % event.Ascii)
    logger.debug("Key: %s" % event.Key)
    logger.debug("KeyID: %s" % event.KeyID)
    logger.debug("ScanCode: %s" % event.ScanCode)
    logger.debug("Extended: %s" % event.Extended)
    logger.debug("Injected: %s" % event.Injected)
    logger.debug("Alt %s" % event.Alt)
    logger.debug("Transition %s" % event.Transition)
    key_state = win32api.GetKeyState(event.KeyID)
    logger.debug("Key state %s" % key_state)
    logger.debug("-" * 80)
    current_key = event.KeyID
    if event.KeyID == VK_MEDIA_PLAY_PAUSE and key_state < 0:
        logger.info("Exiting...")
        exit(0)
    if event.WindowName != "Amazon WorkSpaces":
        return True
    if current_key == VK_CAPITAL:
        logger.debug("CAPS LOCK pressed")
        aws_window = win32gui.FindWindow(None, "Amazon WorkSpaces")
        win32gui.SendMessage(aws_window, WM_KILLFOCUS)
        return False
    # return True to pass the event to other handlers
    # return False to stop the event from propagating
    return True


def main():
    import pythoncom
    hm = pyHook.HookManager()
    hm.KeyDown = OnKeyboardEvent
    hm.HookKeyboard()
    logger.info("Capturing keyboard events. Hold Play/Pause to exit.")
    logger.info("Press CAPS LOCK to de-focus Amazon WorkSpaces")
    pythoncom.PumpMessages()


if __name__ == '__main__':
    from argparse import ArgumentParser
    argparser = ArgumentParser()
    argparser.add_argument("--debug", action="store_true")
    args = argparser.parse_args()
    if args.debug:
        logger.setLevel(logging.DEBUG)
    main()
