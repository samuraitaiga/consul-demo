#!/bin/bash

PID_FILE=/var/run/haproxy.pid

/usr/local/bin/gen-haconfig

if [ -e $PID_FILE ]
then
  pid=`cat $PID_FILE`
  haproxy -f /etc/haproxy/haproxy.cfg -p $PID_FILE -sf $pid
else
  haproxy -f /etc/haproxy/haproxy.cfg -p $PID_FILE
fi

echo haconfig refreshed!!
