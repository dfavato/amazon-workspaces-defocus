# Amazon WorkSpaces de-focus

As of July 11th 2023 [Amazon WorkSpaces](https://aws.amazon.com/workspaces)
lacks a keyboard shortcut[^1] to fastly switch to the host environment.

I wrote a python script that when running is able to capture the pressing of
`CAPS LOCK` and uses it to kill the focus from the "Amazon WorkSpaces" window.
After this you can "Ctrl + TAB" in the host machine environment.

# Getting started

## Requirements

This script only works in Windows as it uses win32api to capture the key pressing.

1. [Python3.11](https://www.python.org/downloads/)
2. [pipenv](https://pipenv.pypa.io/en/latest/)

## Installation

1. Clone this repository
2. Execute `install.bat`

## Running and testing

1. Execute `execute.bat`
2. A terminal window should open and show:

```
pipenv run python main.py
INFO:__main__:Capturing keyboard events. Hold Play/Pause to exit.
INFO:__main__:Press CAPS LOCK to de-focus Amazon WorkSpaces
```

Once inside the "Amazon WorkSpaces" if you press "CAPS LOCK" the Workspace will loose
focus and you can "Alt + TAB" in your host environment.

If you hold the "Media Play/Pause" key in your keyboard the execution should
end and the terminal close (also the CAPS LOCK shortcut won't work anymore).

# FAQ

**Q**: I don't have the "Media Play/Pause" key on my keyboard how can I stop the script?
**A**: Just close the terminal window running it.

**Q**: Can I change the keys used?
**A**: Yes, you'll have to change the `main.py` script. You can find all keys [here](https://github.com/mhammond/pywin32/blob/e99541164bb65cc76b08804c7a7bbdc52afa47d4/win32/Lib/win32con.py#L969-L1084).

**Q**: How can I use "CAPS LOCK" inside the Amazon Workspaces?
**A**: You'll have to hold "SHIFT". If "CAPS LOCK" is a important key for you you should change the keys (refer to the question above).

[^1]: https://docs.aws.amazon.com/workspaces/latest/userguide/amazon-workspaces-windows-client.html#windows_shortcuts
