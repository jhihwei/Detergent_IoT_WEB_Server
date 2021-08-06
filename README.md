# 洗衣精販售機IoT-Server

## 安裝

### 開機啟動反向SSH代理
```sh
    [Unit]
    Description=SSH 反向代理

    [Service]
    User=root #以哪位角色執行，涉及Service的執行環境
    ExecStart=/usr/bin/ssh -CNL *:9500:localhost:9320 localhost -CNL *:9501:localhost:9321 localhost -CNL *:9502:localhost:9322 localhost -CNL *:9503:localhost:9323 localhost -CNL *:9504:localhost:9324 localhost
    Type=simple
    Restart=always
    RestartSec=1min

    [Install]
    WantedBy=multi-user.target
```

```sh
    [Unit]
    Description=Detergent Django

    [Service]
    User=user
    ExecStart=/usr/bin/python3 /home/user/django_wash_machine/manage.py runserver 0:8000
    ExecReload=/bin/kill -HUP $MAINPID
    KillMode=process
    IgnoreSIGPIPE=true
    Restart=always
    RestartSec=3
    Type=simple

    [Install]
    WantedBy=multi-user.target
```