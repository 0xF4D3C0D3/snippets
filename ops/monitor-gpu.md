## monitor.sh
```bash
#!/bin/bash
nvidia-smi >> monitor-gpu.log
```

## /etc/systemd/system/monitor-gpu.timer
```bash
[Unit]
Description=Run monitor-gpu every 2 seconds

[Timer]
OnActiveSec=2s
OnUnitActiveSec=2s
AccuracySec=100ms

[Install]
WantedBy=timers.target
```

## /etc/systemd/system/monitor-gpu.service
```bash
[Unit]
Description=Monitoring nvidia-smi GPU status

[Service]
Type=oneshot
WorkingDirectory=/var/log/.../monitor_gpu
ExecStart=/var/log/.../monitor_gpu/monitor.sh
Restart=no

[Install]
WantedBy=multi-user.target
```

## /etc/logrotate.d/monitor_gpu
```bash
/var/log/.../monitor_gpu/monitor-gpu.log {
  daily
  dateext
  rotate 14
  compress
}
```

## check status
```bash
sudo systemctl status monitor-gpu.service
sudo systemctl status monitor-gpu.timer
```

## apply changes
```bash
sudo systemctl daemon-reload
```

## logrotate logs
```bash
less /var/lib/logrotate/status
```
