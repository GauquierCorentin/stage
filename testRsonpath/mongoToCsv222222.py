import pymongo
import csv
import matplotlib.pyplot as plt
import datetime

client = pymongo.MongoClient("127.0.0.1", 27017)
db = client["powerapicorentin"]
collection = db["powerrep"]

donnees = []

# Filter documents with target: "/222222"
query = {"target": "/222222"}
for document in collection.find(query):
    document_copy = document.copy()  # Create a copy of the document to avoid modifying the original
    # If the 'timestamp' field exists and is of type 'datetime.datetime', convert it to a string
    if 'timestamp' in document_copy and isinstance(document_copy['timestamp'], datetime.datetime):
        document_copy['timestamp'] = str(document_copy['timestamp'])
    donnees.append(document_copy)

with open('donnees.csv', 'w', newline='') as csvfile:
    fieldnames = list(donnees[0].keys())
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for document in donnees:
        writer.writerow(document)

timestamps = []
power = []

for document in donnees:
    timestamps.append(document['timestamp'])
    power.append(document['power'])

plt.plot(timestamps, power)
plt.xlabel('Timestamp')
plt.ylabel('Power')
plt.title('Power over Time')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

