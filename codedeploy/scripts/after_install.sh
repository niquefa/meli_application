#!/bin/sh
exec 2>&1

mkdir -p /app
cd /app
unzip source.zip

systemctl enable app
