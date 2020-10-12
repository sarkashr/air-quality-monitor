# air-quality-monitor


Setting up the Raspberry Pi for running the python code:
```
sudo apt update
sudo apt upgrade
sudo apt install python3-pip
sudo pip3 install wheel
sudo pip3 install -r /home/pi/air-quality-monitor/code/requirements.txt
```

Setting up the cron table entries:
```
sudo crontab -e
```
then add the following lines to the end of crontab file:
```
@reboot python3 /home/pi/air-quality-monitor/code/sds011-reset.py
@reboot python3 /home/pi/air-quality-monitor/code/read_and_publish.py &
```
