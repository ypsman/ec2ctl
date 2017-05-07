# ec2ctl
Python3 script for start, stop and snapshot a list or a single EC2 Instance.<br>
It Creates snapshots from all Volumes of a Instance.<br>
Snapshots Description is **InstanceName /DeviceName**.

#### Config:
Rename the **example-ec2ctl.yml** to **ec2ctl.yml** <br>
Insert your aws Credential in the Config File under awsconfig.

options in Config File:

    logfile: ec2ctl.log             # logfilename (default: ec2ctl.log)
    awsconfig:
      aws_key_id: youre_awskey
      aws_secret: youre_awssecret
      aws_region: aws_region
    instanes:                       # List of Instances to Start and Stop
      first_inst: i-123456
      second_instance: i-56789
    snapshots:                      # List of Instance for snapshots
      database_inst: i-123456
      webserver_instance: i-56789

#### Example usage:

    ec2ctl.py --start all          # starting all instances in config
    ec2ctl.py --start i-123456     # start single Instance
    ec2ctl.py --stop all           # stopping all instances in config
    ec2ctl.py --stop i-123456      # stops a single Instance
    ec2ctl.py --backup all         # snapshots all instances in config
    ec2ctl.py --backup i-123456    # snapshots a Instance

#### install:
dependencies:

    pip3 install -r requirements.txt
