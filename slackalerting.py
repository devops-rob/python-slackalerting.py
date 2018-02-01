#!/usr/bin/python

#Import python libraries
import psutil
import os
from slacker import Slacker
import datetime
import time

#Variables
cpu_threshold=<insert-cpu-threshold-%>
mem_threshold=<insert-memory-threshold-%>
disk_threshold=<insert-diskspace-threshold-%>
slack = Slacker('<insert-your-slack-api-token-here>')
logfile='/var/log/monitor.log'

#CPU Alerting
def cpu():
    if psutil.cpu_percent() > cpu_threshold:
        slack.chat.post_message('#<insert-slack-channel-name-here>', 'CPU ALERT - CPU usage is currently above %s percent' % cpu_threshold)
        print (time.strftime("%c") + ' - CPU ALERT - CPU usage is currently above %s percent' % cpu_threshold)
        with open(logfile, 'a') as file_handle:
            file_handle.write(time.strftime("%c") + ' - CPU ALERT - CPU usage is currently above %s percent' % cpu_threshold)
    else:
        print (time.strftime("%c") + ' - cpu is below %s percent' % cpu_threshold)
        with open(logfile, 'a') as file_handle:
            file_handle.write(time.strftime("%c") + ' - cpu is below %s percent' % cpu_threshold)
    return

#Memory Alerting
def memory():
    if psutil.virtual_memory().percent > mem_threshold:
        slack.chat.post_message('#<insert-slack-channel-name-here>', 'MEMORY ALERT - Memory usage is currently above %s percent' % mem_threshold)
        print(time.strftime("%c") + ' - MEMORY ALERT - Memory usage is currently above %s percent' % mem_threshold)
        with open(logfile, 'a') as file_handle:
            file_handle.write(time.strftime("%c") + ' - MEMORY ALERT - Memory usage is currently above %s percent' % mem_threshold)
    else:
        print(time.strftime("%c") + ' - Memory usage is below %s percent' % mem_threshold)
        with open(logfile, 'a') as file_handle:
            file_handle.write(time.strftime("%c") + ' - Memory usage is below %s percent' % mem_threshold)
    
    return

#Disk Usuage Alerting
def disk():
    if psutil.disk_usage('/').percent > disk_threshold:
        slack.chat.post_message('#<insert-slack-channel-name-here>', 'DISK SPACE ALERT - Disk space usage is currently above %s percent' % disk_threshold)
        print(time.strftime("%c") + ' - DISK SPACE ALERT - Disk space usage is currently above %s percent' % disk_threshold)
        with open(logfile, 'a') as file_handle:
            file_handle.write(time.strftime("%c") + ' - DISK SPACE ALERT - Disk space usage is currently above %s percent' % disk_threshold)
    
    else:
        print(time.strftime("%c") + ' - disk space usage is below %s percent' % disk_threshold)
        with open(logfile, 'a') as file_handle:
            file_handle.write(time.strftime("%c") + ' - disk space usage is below %s percent' % disk_threshold)

    return

#Network Packet loss alerting
def netmon():
    if psutil.net_io_counters().dropout > 0:
        slack.chat.post_message('#<insert-slack-channel-name-here>', 'PACKET LOSS ALERT - The system is currently experiencing packet loss')
        print(time.strftime("%c") + ' - PACKET LOSS ALERT - The system is currently experiencing packet loss')
        with open(logfile, 'a') as file_handle:
            file_handle.write(time.strftime("%c") + ' - PACKET LOSS ALERT - The system is currently experiencing packet loss')
    else:
        print(time.strftime("%c") + ' - No packets have been lost')
        with open(logfile, 'a') as file_handle:
            file_handle.write(time.strftime("%c") + ' - No packets have been lost')

    return

cpu()
memory()
disk()
netmon()
