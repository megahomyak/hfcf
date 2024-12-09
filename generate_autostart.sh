#!/bin/sh
mkdir -p ~/.config/systemd/user
cat > ~/.config/systemd/user/hfcf.service << EOF
[Unit]

[Service]
ExecStart=$(which poetry) run python run.py
WorkingDirectory=$(pwd)

[Install]
WantedBy=graphical-session.target
EOF
systemctl --user daemon-reload
systemctl --user enable hfcf
systemctl --user start hfcf
