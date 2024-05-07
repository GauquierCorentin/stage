import pymongo
import csv
import matplotlib.pyplot as plt
import datetime

client = pymongo.MongoClient("localhost", 27019)
db = client["powerapicorentin"]
collection = db["powerrep"]

donnees = []

for document in collection.find():
    document_copy = document.copy()  # Créer une copie du document pour éviter de modifier l'original
    # Si le champ 'timestamp' existe et est de type 'datetime.datetime', le convertir en chaîne de caractères
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
