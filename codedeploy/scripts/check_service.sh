#!/bin/sh
while true
do
  # In the context of servers, 0.0.0.0 mean "all IPv4 addresses on the local machine"
  curl http://0.0.0.0/health && break
  sleep 1
done
