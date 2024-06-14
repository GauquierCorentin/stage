#!/bin/bash

PERF_CGROUP="/sys/fs/cgroup/perf_event"
SYSTEM_CGROUP="$PERF_CGROUP/system"

mkdir -p $SYSTEM_CGROUP

while read pid
do
    if [ -f "/proc/$pid/cmdline" ]
    then
        if [ $(cat "/proc/$pid/cmdline" |wc -w) -gt 0 ]
        then
            echo $pid >$SYSTEM_CGROUP/cgroup.procs
        fi
    fi
done <$PERF_CGROUP/cgroup.procs
