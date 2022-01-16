Steps for Docker
1. Git clone:
git clone https://github.com/pranaavn/GarageMonitoring nautilus

2. sudo apt install python3

3. sudo apt install python3-pip

4. pip3 install Flask

5. pip3 install --upgrade pip virtualenv

6. pip3 install prometheus-client

7. wget https://github.com/prometheus/prometheus/releases/download/v2.0.0/prometheus-2.0.0.linux-amd64.tar.gz

8. tar xvfz prometheus-*.tar.gz

8.5. ADD TO prometheus.yml FILE

9. sudo nano /etc/systemd/system/prometheus.service
INPUT:
[Unit]
Description=Prometheus
Wants=network-online.target
After=network-online.target

[Service]
User=root
Group=root
Type=simple
ExecStart=/home/pranav/prometheus/prometheus \
    --config.file /home/pranav/prometheus/prometheus.yml \
    --storage.tsdb.path /home/pranav/prometheus/ \
    --web.console.templates=/home/pranav/prometheus/consoles \
    --web.console.libraries=/home/pranav/prometheus/console_libraries

[Install]
WantedBy=multi-user.target[Unit]

10. sudo pkill -e prometheus

11. sudo systemctl daemon-reload

12. sudo systemctl start prometheus.service

13. sudo systemctl status prometheus.service

14. nohup python3 /home/pranav/nautilus/GarageOperations.py &
