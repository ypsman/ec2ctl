# still in development
# ec2ctl.sh
a small Bash script to start and Stop a list of <br>
AWS ec2 instances.<br>
The Output is logged to a File called *launch.log*.<br>
Errors will output to stderr.

#### Usage:
Put your instance-ids in a file called startstop.txt and <br>
put it in the same Directory as the ec2ctl.sh script.

**statstop.txt**

    i-123456789
    i-abcdefghi

Just start *ec2ctl.sh* with one of the Parameters.

    ec2ctl.sh -u  # start all instances
    ec2ctl.sh -d  # stops all instances



#### Cronjob Example:
To run the instances only Monday till Friday <br>
and between 7:00 and 18:00

    0  7 * * MON-FRI root /opt/ec2ctl/ec2ctl.sh -u
    0 18 * * MON-FRI root /opt/ec2ctl/ec2ctl.sh -d
