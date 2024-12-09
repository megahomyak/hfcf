#!/bin/sh
DIR="$1"
if [ "$DIR" = "" ]; then
>&2 echo "Directory wasn't passed"
else
cat > ~/.config/autostart/hfcf.desktop << EOF
[Desktop Entry]
Exec=sh -c 'cd ${DIR} && poetry run python run.py'
Terminal=false
Type=Application
Name=hfcf
EOF
fi
