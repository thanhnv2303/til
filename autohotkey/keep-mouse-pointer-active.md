# Moving the mouse pointer to keep screen active

Often due to inactivity, the PC may automatically turn the screen off. This can be annoying when working. So, the following snippet would keep the screen on by moving the pointer by a little and doing a mouse click every 10 seconds.

```ahk
Loop
{
    ; Move mouse
    MouseMove, 1, 0, 0, R
    ; Replace mouse to its original location
    MouseMove, -1, 0, 0, R
    ; Left Click once
    Click
    ; Wait before moving the mouse again
    Sleep, 10000
}
```

Source: [Simple script to move mouse 1px ?](https://www.reddit.com/r/AutoHotkey/comments/idriwu/comment/g2cnlrw/?utm_source=share&utm_medium=web2x&context=3)
