import csv
import matplotlib.pyplot as plt
import datetime

# Read data from CSV
timestamps = []
power = []

with open('folderCSV/simd/donnees_debiansimd_cr4.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        timestamps.append(row['timestamp'])
        power.append(float(row['power']))

# Convert timestamp strings to datetime objects
timestamps = [datetime.datetime.strptime(ts, "%Y-%m-%d %H:%M:%S.%f") if '.' in ts else datetime.datetime.strptime(ts, "%Y-%m-%d %H:%M:%S") for ts in timestamps]

# Plotting the data
plt.plot(timestamps, power)
plt.xlabel('Timestamp')
plt.ylabel('Power')
plt.title('Power over Time (target: debianrq)')

# Set the x-ticks to display only 10% of the timestamps
step = max(1, len(timestamps) // 10)
plt.xticks(ticks=timestamps[::step], labels=[ts.strftime("%Y-%m-%d %H:%M:%S") for ts in timestamps[::step]], rotation=45)

plt.tight_layout()
plt.show()
