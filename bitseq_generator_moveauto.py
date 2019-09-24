#! python3
# -*- coding: utf-8 -*-

import random
import sys

Nleft = 2
Nright = 1000
flag_output = False

N = random.randint(Nleft,Nright)
path_output = "./"
filename_output = "input.txt"

str_clip = ""
for _ in range(N):
    str_clip += "{}".format(random.randint(0,1))
#end for

print(str_clip)

if flag_output:
    with open(path_output+filename_output,mode="w") as file_out:
        file_out.write(str_clip)
    #end with
#end if
