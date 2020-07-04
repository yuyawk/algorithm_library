#! python3
# -*- coding: utf-8 -*-

import random
import sys

Nmin = 4
Nmax = 5
leftmin = 1
leftmax = 1
rightmax = 1e9
flag_printN = True
flag_distinct = False
flag_outputfile = False


N = random.randint(Nmin,Nmax)
left = random.randint(leftmin,leftmax)
right = random.randint(left,rightmax)

while flag_distinct and  N > right - left + 1:
    left = random.randint(leftmin,leftmax)
    right = random.randint(left,rightmax)
#end if

path_output = "./"
filename_output = "input.txt"

if flag_distinct:
    set_el = set()
#end if

str_clip = ""
if flag_printN:
    str_clip = "{}\n".format(N)
#end if
for i in range(N):
    if i == N-1:
        endl = ""
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
print(str_clip)

if flag_outputfile:
    with open(path_output+filename_output,mode="w") as file_out:
        file_out.write(str_clip)
    #end with
#end if

    
