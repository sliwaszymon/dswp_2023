import re, datetime, csv
import numpy as np

dates, ips, users, comms = [], [], [], []
with open('auth.log', 'r', newline='', encoding='utf-8') as file:
    for line in file:
        dates.append(re.findall(re.compile(r'[A-Z][a-z]{2}\s{1,2}\d{1,2}\s\d{2}:\d{2}:\d{2}'), line))
        ips.append(re.findall(re.compile(r'\d\sip-\d{1,3}-\d{1,3}-\d{1,3}-\d{1,3}'), line))
        users.append(re.findall(re.compile(r'-\d{1,3}\s\w+-?\w+\[?\d*\]?:\s'), line))
        comms.append(re.findall(re.compile(r'-\d{1,3}\s\w+-?\w+\[?\d*\]?:\s.+\n'), line))

dates = [datetime.datetime.strptime(date,'%b %d %H:%M:%S').replace(year=2023).strftime('%Y-%m-%d %H:%M:%S') for date in np.array(dates).flatten()]
ips = [ip[5:].replace("-",".") for ip in np.array(ips).flatten()]
users = [user[5:] for user in np.array(users).flatten()]
comms = [com[com.find(": ")+2:] for com in np.array(comms).flatten()]
comms = ["\""+com[:-1]+"\"" for com in comms]

with open('zad2.csv', 'w', newline='') as csvf:
    writer = csv.writer(csvf, delimiter=";")
    for x in zip(dates, ips, users, comms):
        writer.writerow(x)