#!/bin/bash

docker run -td --name smartwatts-mongodb-corentin --network network_corentin -v /home/spirals/smartwatts-mongo-data:/data/db -p 127.0.0.1:27017:27017 mongo

sleep 5

docker run -td --name smartwatts-formula-corentin --network network_corentin gfieni/powerapi:smartwatts -s \
    --input mongodb -n "sensor" -u "mongodb://smartwatts-mongodb-corentin" -d "powerapicorentin" -c "sensor" -m "HWPCReport" \
    --output mongodb -n "power" -u "mongodb://smartwatts-mongodb-corentin" -d "powerapicorentin" -c "powerrep" -m "PowerReport" \
    --output mongodb -n "formula" -u "mongodb://smartwatts-mongodb-corentin" -d "powerapicorentin" -c "formularep" -m "FormulaReport" \
    --formula smartwatts --cpu-ratio-min 4 --cpu-ratio-max 42 --cpu-ratio-base 19 --disable-dram-formula --sensor-reports-frequency 500

docker run -td --privileged --user root --name smartwatts-sensor-corentin --network network_corentin \
        -v /sys:/sys -v /var/lib/docker/containers:/var/lib/docker/containers:ro \
        gfieni/hwpc-sensor:stable \
        -n "$(hostname -f)" \
        -r "mongodb" -U "mongodb://smartwatts-mongodb-corentin" -D "powerapicorentin" -C "sensor" \
        -s "rapl" -o -e "RAPL_ENERGY_PKG" \
        -s "msr" -e "TSC" -e "APERF" -e "MPERF" \
        -c "core" -e "CPU_CLK_UNHALTED:REF_P" -e "CPU_CLK_UNHALTED:THREAD_P" -e "LLC_MISSES" -e "INSTRUCTIONS_RETIRED" \
        -f 500
