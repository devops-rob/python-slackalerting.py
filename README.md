# python-slackalerting.py
Download the slacker python module by running wget https://pypi.python.org/packages/42/f9/3f3bcbe13b8c3aa4a134136cbbaa94beb1c5781f5a33b9317b45c699d453/slacker-0.9.60.tar.gz
Untar the file by running tar -xzvf slacker-0.9.60.tar.gz
run pip install slacker

Install the psutil module by yum install python-psutil -y

Enter the alert thresholds you would like to set in the variables section

For each alert, enter the slack channel name that you would like to notify in place of <slack-channel-name>

Install a crontab for this script to run at whatever poll interval you require for your monitoring. e.g. * * * * * /usr/bin/python /root/monitoring/slack_alerting.py

This script will also create a log file (/var/log/monitor.log) if it doesn't already exist and write the output of the server checks to it.
I highly recommend installing and configuring logrotate on this file
