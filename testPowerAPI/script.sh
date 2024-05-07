#!/bin/bash

echo "Demarrage collecte mesures"
powerapi-server -n rapl -s rapl_package-0 -r "RAPL_ENERGY_PKG:PACKAGE_ENERGY:RAPL_PKG_ENERGY" &

sleep 5

python readJson.py

killall powerapi-server

echo "Operations terminees"
