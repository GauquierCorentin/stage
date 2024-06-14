import pymongo
import csv
import matplotlib.pyplot as plt
import datetime

client = pymongo.MongoClient("localhost", 27017)  # Assuming default port 27017
db = client["powerapicorentin"]
collection = db["powerrep"]

donnees = []

# Define the start and end timestamps to the minute
start_timestamp = datetime.datetime(2024, 6, 14, 7, 0, 12)  # Replace with your start date and time
end_timestamp = datetime.datetime(2024, 6, 14, 7, 0, 16)    # Replace with your end date and time

# Filter documents with target: "debianrq" and within the specified timestamp range
filtered_cursor = collection.find({
    "target": "debianrq",
    "timestamp": {"$gte": start_timestamp, "$lt": end_timestamp}
})

for document in filtered_cursor:
    document_copy = document.copy()  # Create a copy for safety
    # If 'timestamp' exists and is datetime, convert to string
    if 'timestamp' in document_copy and isinstance(document_copy['timestamp'], datetime.datetime):
        document_copy['timestamp'] = str(document_copy['timestamp'])
    donnees.append(document_copy)

# Write filtered data to CSV (optional)
with open('donnees_debianrq.csv', 'w', newline='') as csvfile:
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
plt.title('Power over Time (target: debianrq)')

# Set the x-ticks to display only 10% of the timestamps
step = max(1, len(timestamps) // 10)
plt.xticks(ticks=timestamps[::step], labels=timestamps[::step], rotation=45)

plt.tight_layout()
plt.show()
