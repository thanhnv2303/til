# Prevent Colab Session from Disconnecting

Running long sessions on [Google Colab](https://colab.research.google.com) without any activity can cause the session to disconnect, losing all the data and variables from the earlier executed cells. This can be prevented by entering the following code into the browser console (opened by pressing <button>Ctrl</button> + <button>Shift</button> + <button>I</button>).

```javascript
function ClickConnect() {
    console.log("Working");
    document.querySelector("colab-connect-button").shadowRoot.querySelector("#connect").click()
}
setInterval(ClickConnect, 90000);
```

Source: [How to prevent Google Colab from disconnecting ?](https://medium.com/@shivamrawat_756/how-to-prevent-google-colab-from-disconnecting-717b88a128c0)
