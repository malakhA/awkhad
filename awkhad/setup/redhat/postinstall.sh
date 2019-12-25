#!/bin/sh

set -e

AWKHAD_CONFIGURATION_DIR=/etc/awkhad
AWKHAD_CONFIGURATION_FILE=$AWKHAD_CONFIGURATION_DIR/awkhad.conf
AWKHAD_DATA_DIR=/var/lib/awkhad
AWKHAD_GROUP="awkhad"
AWKHAD_LOG_DIR=/var/log/awkhad
AWKHAD_LOG_FILE=$AWKHAD_LOG_DIR/awkhad-server.log
AWKHAD_USER="awkhad"

if ! getent passwd | grep -q "^awkhad:"; then
    groupadd $AWKHAD_GROUP
    adduser --system --no-create-home $AWKHAD_USER -g $AWKHAD_GROUP
fi
# Register "$AWKHAD_USER" as a postgres user with "Create DB" role attribute
su - postgres -c "createuser -d -R -S $AWKHAD_USER" 2> /dev/null || true
# Configuration file
mkdir -p $AWKHAD_CONFIGURATION_DIR
# can't copy debian config-file as addons_path is not the same
if [ ! -f $AWKHAD_CONFIGURATION_FILE ]
then
    echo "[options]
; This is the password that allows database operations:
; admin_passwd = admin
db_host = False
db_port = False
db_user = $AWKHAD_USER
db_password = False
addons_path = /usr/lib/python3.6/site-packages/awkhad/addons
" > $AWKHAD_CONFIGURATION_FILE
    chown $AWKHAD_USER:$AWKHAD_GROUP $AWKHAD_CONFIGURATION_FILE
    chmod 0640 $AWKHAD_CONFIGURATION_FILE
fi
# Log
mkdir -p $AWKHAD_LOG_DIR
chown $AWKHAD_USER:$AWKHAD_GROUP $AWKHAD_LOG_DIR
chmod 0750 $AWKHAD_LOG_DIR
# Data dir
mkdir -p $AWKHAD_DATA_DIR
chown $AWKHAD_USER:$AWKHAD_GROUP $AWKHAD_DATA_DIR

INIT_FILE=/lib/systemd/system/awkhad.service
touch $INIT_FILE
chmod 0700 $INIT_FILE
cat << EOF > $INIT_FILE
[Unit]
Description=Awkhad Open Source ERP and CRM
After=network.target

[Service]
Type=simple
User=awkhad
Group=awkhad
ExecStart=/usr/bin/awkhad --config $AWKHAD_CONFIGURATION_FILE --logfile $AWKHAD_LOG_FILE
KillMode=mixed

[Install]
WantedBy=multi-user.target
EOF
