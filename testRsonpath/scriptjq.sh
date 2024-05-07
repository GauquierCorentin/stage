#!/bin/bash

rq '$..author' crossref0.json
sleep 5
jq '.. | objects | .author' crossref0.json
sleep 8

rq '$..author' crossref1.json
sleep 5
jq '.. | objects | .author' crossref1.json
sleep 8

rq '$..author' crossref2.json
sleep 5
jq '.. | objects | .author' crossref2.json
sleep 8

rq '$..author' crossref4.json
sleep 5
jq '.. | objects | .author' crossref4.json
sleep 8

rq '$..author' crossref8.json
sleep 5
jq '.. | objects | .author' crossref8.json
sleep 8
