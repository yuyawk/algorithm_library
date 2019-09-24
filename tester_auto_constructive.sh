#!/bin/bash

script_solution="./notetmp/note14tmp.cpp"
script_bruteforce="./notetmp/note1tmp.cpp"

testcase="./z_midfiles/input.txt"
midcase="./z_midfiles/input2.txt"
program_solution="./z_midfiles/solution.out"
program_bruteforce="./z_midfiles/bruteforce.out" 

echo "Compiling a script... (target)"
g++ $script_solution -g -o $program_solution
echo "Compiling a script... (brute-force)"
g++ $script_bruteforce -g -o $program_bruteforce 

cnt=3
while true
do
    echo $cnt > $testcase
    echo $($program_solution < $testcase) > $midcase
    echo "N=$cnt"
    echo $($program_bruteforce < $midcase)
    ((++cnt))
done
