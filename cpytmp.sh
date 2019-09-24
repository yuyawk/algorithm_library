#!/bin/bash

for i in `seq 1 20`
do
    cp template.cpp "./notetmp/note${i}tmp.cpp" -f
done
