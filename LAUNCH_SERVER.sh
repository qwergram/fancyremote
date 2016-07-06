echo '==> !LAUNCHING FANCY REMOTE! <=='
python3 src/fancy_remote.py > /dev/null 2>&1 &
python3 src/cpu_monitor.py > /dev/null 2>&1 &
echo check 0.0.0.0:8080
