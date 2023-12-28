#!/usr/bin/python3
import os
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument("input_dir", help="plan input file directory")
parser.add_argument("device", help="pcc device name")
parser.add_argument("config_location", help="location of pcc config")
args = parser.parse_args()

now = datetime.now()
input_file_name = "pccplan.{}.tsv".format(now.strftime("%Y-%m-%d"))

file = open("{}/{}".format(args.input_dir, input_file_name), 'r')
lines = file.readlines()

now_hour = now.strftime("%-H")
for line in lines:
    split = line.replace("\n", "").split("\t")
    hour = split[0]
    enabled = split[1] == 'true'
    if hour == now_hour:
        arg = '-on' if enabled else '-off'
        cmd = "go-pcc -device {} -config {} {}".format(args.device, args.config_location, arg)
        print(cmd)
        os.system(cmd)
        exit(0)

print("unable to find hour {} in file {}".format(now_hour, input_file_name))
exit(1)
