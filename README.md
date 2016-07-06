# fancyremote
  A python powered monitor for any azure or remote computer
  > Coded with love by Norton Pengra
  
  Inspired by https://github.com/Wiladams/REMOTE

# Setup with your remote computer
Open port `8080 - 8081` on your computer
Allow inbound TCP and UDP protocols for the port you choose.
You do not have to do this step if you use a tool like hamachi.

# Launch the Remote
The simplest way to launch the server is to:

```
git clone https://github.com/qwergram/fancyremote.git
cd fancyremote
pip install -r requirements.txt
[sudo] ./LAUNCH_SERVER.sh
```
(sudo is required if you're accessing root locations)

Finally, use your favorite browser and point it to the ip address of your computer.

# Files
## `./LAUNCH_SERVER.sh`
Run this to execute the server in the background.

## `src/fancy_remote.py`
This is the remote file browser you are able to use to view and download files on your hard drive.

## `src/cpu_monitor.py`
This file monitors by default `/proc/stat` for cpu stats, and spams processor information to 0.0.0.0:8081.
