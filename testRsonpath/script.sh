#!/bin/bash

rq '$..author' crossref0.json
sleep 10
python3 jsonpath0.py
sleep 15

rq '$..author' crossref1.json
sleep 10
python3 jsonpath1.py
sleep 15

rq '$..author' crossref2.json
sleep 10
python3 jsonpath2.py
sleep 15

rq '$..author' crossref4.json
sleep 10
python3 jsonpath4.py
sleep 15

rq '$..author' crossref8.json
sleep 10
python3 jsonpath8.py
sleep 15
