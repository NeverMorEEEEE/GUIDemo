import os
import re
import time
import sys
import subprocess

lifeline = re.compile(r"(\d) received")
report = ("No response", "Partial Response", "Alive")

print(time.ctime())

for host in range(1, 10):
    ip = "10.84.3." + str(host)
    pingaling = subprocess.Popen(["ping", "-q", "-c 2", "-r", ip], shell=False, stdin=subprocess.PIPE,
                                 stdout=subprocess.PIPE)
    print("Testing ", ip)
    while 1:
        pingaling.stdout.flush()
        line = pingaling.stdout.readline()
        print(line)
        if not line: break
        igot = re.findall(lifeline, line)
        print(igot)
        if igot:
            print(report[int(igot[0])])

print(time.ctime())

