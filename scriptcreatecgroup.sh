#!/bin/bash

sudo cgcreate -g perf_event:222222

nano

sleep 2

pid=$!

sudo cgclassify -g perf_event:222222 $pid
