import os
import re
import time
import sys
import subprocess

lifeline = re.compile(r"(\d) received")
report = ("No response", "Partial Response", "Alive")

ip = '10.80.79.12';
pingaling = subprocess.Popen(["ping", "-q", "-c 2", "-r", ip], shell=False, stdin=subprocess.PIPE,
                                 stdout=subprocess.PIPE)
print("Testing ", ip)
while 1:
    pingaling.stdout.flush()
    line = pingaling.stdout.readline()
    print(type(line))

    if not line: break
    igot = re.findall(lifeline, line)
    if igot:
        print(report[int(igot[0])])

print(pingaling)