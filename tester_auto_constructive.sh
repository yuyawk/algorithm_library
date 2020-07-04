#!/bin/bash

script_solution="./notetmp/note1tmp.cpp"
script_bruteforce="./notetmp/note2tmp.cpp"

testcase="./z_midfiles/input.txt"
midcase="./z_midfiles/input2.txt"
program_solution="./z_midfiles/solution.out"
program_bruteforce="./z_midfiles/bruteforce.out" 

echo "Compiling a script... (target)"
g++ $script_solution -g -o $program_solution
echo "Compiling a script... (brute-force)"
g++ $script_bruteforce -g -o $program_bruteforce 

cnt=0
while true
do
    echo $cnt > $testcase
    echo $($program_solution < $testcase) > $midcase
    echo "N=$cnt"
    res=$($program_bruteforce < $midcase)

    if [[ $cnt != $res ]]
    then
	echo "Wrong Answer"
	echo "output: $res"
	echo "expected: $cnt"
        exit
    else
	echo "OK(case K=$cnt)"
	((++cnt))
    fi
done
