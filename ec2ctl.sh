#!/bin/bash
# A POSIX variable
OPTIND=1         # Reset in case getopts has been used previously in the shell.
set -e
file="startstop.txt"
logfile="launch.log"

function startinst() {
  for line in $instances; do
    aws ec2 start-instances --instance-id $line --output text >> $logfile
  done
}

function stopinst() {
  for line in $instances; do
    aws ec2 stop-instances --instance-id $line --output text >> $logfile
  done
}

instances=$(cat $file)

echo "$(date)" >> $logfile

while getopts "?:ud" opt; do
  case $opt in
    u)
      startinst
      ;;
    d)
      stopinst
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      ;;
  esac
done
