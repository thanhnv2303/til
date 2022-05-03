# Kill a process occupying a port

Often when running a process on a port, we get the message that the port is already in use by some other process. To kill the process, we can use the following commands:

Linux and Mac:

```sh
sudo kill $(sudo lsof -t -i:4200)
# OR
sudo kill `sudo lsof -t -i:4200`
# OR
sudo lsof -t -i tcp:4200 | xargs kill -9
```

Windows:

```powershell
netstat -a -n -o | findStr "4200"
# Find the PID of the process then run the following
taskkill -f /pid 11128
```

Source: [Kavinda Senarathne's answer to "Port 4200 is already in use" when running the ng serve command](https://stackoverflow.com/a/64960678/10307491)
