#! python3
# -*- coding: utf-8 -*-

import random
import sys

left = 1
right = 1e5
flag_outputfile = False

N = random.randint(left,right)

path_output = "./"
filename_output = "input.txt"

print(N)

if flag_outputfile:
    with open(path_output+filename_output,mode="w") as file_out:
        file_out.write("{}".format(N))
    #end with
#end if
