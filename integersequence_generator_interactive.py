#! python3
# -*- coding: utf-8 -*-

import random
import sys
import pyperclip

print("number of random integers:")
N = int(float(sys.stdin.readline()))
print("minimum:")
left = int(float(sys.stdin.readline()))
right = left-1
while right < left:
    print("maximum (must be greater than or equal to the minimum value):")
    right = int(float(sys.stdin.readline()))
#end while

flag_distinct = False
txt_isdistinct = ""

if N <= right - left + 1 and 1 < N:
    print("Do you make every element distinct? (y or n)")
    answer = sys.stdin.readline().strip()
    if answer.lower()[0] == "y":
        flag_distinct = True
        txt_isdistinct = "_distinct"
    #end if
#end if

if flag_distinct:
    set_el = set()
#end if

path_output = "./"
filename_output = "randintseq_{}nums_from{}_to{}{}.txt".format(N,left,right,txt_isdistinct)


str_clip = "{}\n".format(N)
for i in range(N):
    if i == N-1:
        endl = "\n"
    else:
        endl = " "
    #end if

    numgen = random.randint(left,right)

    while flag_distinct and (numgen in set_el):
        numgen = random.randint(left,right)
    #end while
    str_clip += "{}{}".format(numgen,endl)

    if flag_distinct:
        set_el.add(numgen)
    #end if
#end for
print("Generated:\n")
print(str_clip)
pyperclip.copy(str_clip)
print("Copied to your clipboard!")
print("Do you write the output to a txt file? (y or n)")
answer = sys.stdin.readline().strip()

if answer.lower()[0] == "y":
    with open(path_output+filename_output,mode="w") as file_out:
        file_out.write(str_clip)
    #end with
#end if

print("Done.")
