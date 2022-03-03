# Open Windows Terminal with the Linux Shortcut

The Terminal can be opened in Linux by pressing the <button>Ctrl</button> + <button>Alt</button> + <button>T</button> button combination. Similar shortcut can be created in Windows by using the following script in AutoHotkey.

```ahk
SwitchToWindowsTerminal()
{
  windowHandleId := WinExist("ahk_exe WindowsTerminal.exe")
  windowExistsAlready := windowHandleId > 0

  ; If the Windows Terminal is already open, determine if we should put it in focus or minimize it.
  if (windowExistsAlready = true)
  {
    activeWindowHandleId := WinExist("A")
    windowIsAlreadyActive := activeWindowHandleId == windowHandleId

    if (windowIsAlreadyActive)
    {
      ; Minimize the window.
      WinMinimize, "ahk_id %windowHandleId%"
    }
    else
    {
      ; Put the window in focus.
      WinActivate, "ahk_id %windowHandleId%"
      WinShow, "ahk_id %windowHandleId%"
    }
  }
  ; Else it's not already open, so launch it.
  else
  {
    Run wt
  }
}

; Hotkey to use Ctrl+Alt+T to launch/restore the Windows Terminal.
^!t::SwitchToWindowsTerminal()
```

Source: [Bring up the Windows Terminal in a keystroke](https://blog.danskingdom.com/Bring-up-the-Windows-Terminal-in-a-keystroke/)
