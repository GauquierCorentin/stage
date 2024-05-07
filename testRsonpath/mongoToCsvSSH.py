import pymongo
import csv
import paramiko
import subprocess
import matplotlib.pyplot as plt
import time

ssh_host = '193.51.235.150'
ssh_port = 22
ssh_username = 'powerapi'
ssh_password = 'powerapi'
forwarding_port = 27018  # Port local vers lequel MongoDB sera redirigé

mongo_host = 'localhost'
mongo_port = forwarding_port
mongo_db = 'powerapicorentin'
mongo_collection = 'formularep'

ssh_command = f"ssh -L {forwarding_port}:127.0.0.1:27017 {ssh_username}@{ssh_host} -p {ssh_port}"
subprocess.Popen(ssh_command, shell=True)
time.sleep(15)  # Attendre que la connexion SSH soit établie

client = pymongo.MongoClient(mongo_host, mongo_port, serverSelectionTimeoutMS=5000)
db = client[mongo_db]
collection = db[mongo_collection]

donnees = list(collection.find())

with open('donnees.csv', 'w', newline='') as csvfile:
    fieldnames = list(donnees[0].keys())
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for document in donnees:
        writer.writerow(document)

timestamps = []
pkg_frequencies = []

for document in donnees:
    timestamps.append(document['timestamp']['$date'])
    pkg_frequencies.append(document['metadata']['pkg_frequency'])

plt.plot(timestamps, pkg_frequencies)
plt.xlabel('Timestamp')
plt.ylabel('PKG Frequency')
plt.title('PKG Frequency over Time')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

client.close()
