#!/usr/bin/python3
import logging, time, argparse, yaml, sys
import boto3

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("--start",metavar='', help="Starts specific or All instanes in Config")
group.add_argument("--stop",metavar='', help="Stops specific or All instanes in Config")
group.add_argument("--backup",metavar='', help="Backup specific or All instanes in Config")
args = parser.parse_args()
with open("ec2ctl.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)
logging.basicConfig(filename=cfg['logfile'], level=logging.INFO)
logging.info("#" * 35)
logging.info('# Started at: ' + time.strftime('%Y-%m-%d %H:%M:%S #'))
logging.info("#" * 35)

class awscontrol:
    def __init__(self):
        self.ec2 = boto3.client(
            'ec2',
            aws_access_key_id=cfg['awsconfig']['aws_key_id'],
            aws_secret_access_key=cfg['awsconfig']['aws_secret'],
            region_name=cfg['awsconfig']['aws_region'],)
    def start(self, instIDs):
        try:
            self.response = self.ec2.start_instances(
                InstanceIds=[instIDs,],)
            logging.info("Started: " + instIDs)
        except:
            e = sys.exc_info()[1]
            print("ERROR: starting %s please look at the Logfile" % instIDs)
            logging.error("ERROR: %s :" % e)
    def stop(self, instIDs):
        try:
            self.ec2.stop_instances(
                InstanceIds=[instIDs,],)
            logging.info("Stopped: " + instIDs)
        except:
            e = sys.exc_info()[1]
            print("ERROR: stopping %s please look at the Logfile" % instIDs)
            logging.error("ERROR: %s :" % e)
    def backup(self, instName, instIDs):
        response = self.ec2.describe_instances(InstanceIds=[instIDs])
        for instance in response["Reservations"][0]["Instances"][0]['BlockDeviceMappings']:
            logging.info("Backup: name: " + instName + " id: " + instIDs + " Volume: " + instance["Ebs"]["VolumeId"])
            instName = instName + " vol: " + instance["DeviceName"]
            self.ec2.create_snapshot(
                VolumeId=instance["Ebs"]["VolumeId"],
                Description=instName)

def allinstances(state):
    if state == "start":
        for name, instid in cfg['instances'].items():
            logging.info(state + ": name: " + name + " id: " + instid)
            awsctl.start(instid)
    elif state == "stop":
        for name, instid in cfg['instances'].items():
            logging.info(state + ": name: " + name + " id: " + instid)
            awsctl.stop(instid)

if __name__ == "__main__":
    awsctl = awscontrol()
    if args.start is not None:
        if args.start == "all":
            allinstances("start")
        else:
            awsctl.start(args.start)
    elif args.stop is not None:
        if args.stop == "all":
            allinstances("stop")
        else:
            awsctl.stop(args.stop)
    elif args.backup is not None:
        if args.backup == "all":
            for name, instid in cfg['snapshots'].items():
                awsctl.backup(name, instid)
        else:
            awsctl.backup(args.backup, args.backup)
