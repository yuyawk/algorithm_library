#!/bin/bash

script_solution="./notetmp/note1tmp.cpp"
script_bruteforce="./notetmp/note2tmp.cpp"

testgenerator="./integersequence_generator_moveauto.py"
testcase="./z_midfiles/input.txt"
program_solution="./z_midfiles/solution.out"
program_bruteforce="./z_midfiles/bruteforce.out" 

echo "Compiling a script... (target)"
g++ $script_solution -g -o $program_solution
echo "Compiling a script... (brute-force)"
g++ $script_bruteforce -g -o $program_bruteforce 

cnt=1
while true
do
    python3  $testgenerator > $testcase
    ans1=$($program_solution < $testcase)
    ans2=$($program_bruteforce < $testcase)
    if [[ $ans1 != $ans2 ]]
    then
        echo "Wrong Answer"
	echo "output: $ans1"
	echo "expected: $ans2"
        exit
    else
	echo "OK(case $cnt)"
	((++cnt))
    fi
done
