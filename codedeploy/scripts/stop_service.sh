#!/bin/sh
exec 2>&1
systemctl stop app || true
