docker run -td --name smartwatts-formula-corentin powerapi/smartwatts-formula -s \
    --input mongodb -n "sensor" -u "mongodb://127.0.0.1:27017" -d "powerapicorentin" -c "sensor" -m "HWPCReport" \
    --output mongodb -n "power" -u "mongodb://127.0.0.1:27017" -d "powerapicorentin" -c "powerrep" -m "PowerReport" \
    --output mongodb -n "formula" -u "mongodb://127.0.0.1:27017" -d "powerapicorentin" -c "formularep" -m "FormulaReport" \
    --disable-dram-formula --sensor-reports-frequency 500
