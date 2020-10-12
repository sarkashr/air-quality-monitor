# air-quality-monitor


Setting up the Raspberry Pi for running the python code:
```
sudo apt update
sudo apt upgrade

sudo apt install git
sudo git clone https://github.com/sarkashr/air-quality-monitor.git

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
Note: Modify the MQTT topic and client_id in config.ini accordingly.

--------------------------------------------------------------------------------

For activating SIM7600 module:
```
sudo apt install libqmi-utils && udhcpc
```
Then adding the following line in the crontab just before the sds011-reset line:
```
@reboot python3 /home/pi/air-quality-monitor/code/sim7600_connect.py
```
Note: Modify the APN in the script accordingly(network provider).

--------------------------------------------------------------------------------

for setting up a remoteiot.com new device:
```
sudo apt -y install default-jdk
```
or
```
sudo apt -y install openjdk-11-jre-headless
```

In the RemoteIoT Dashboard go to Devices and there choose Register New Device.
Then
