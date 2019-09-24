#! python3
# -*- coding: utf-8 -*-

import random
import sys
import pyperclip

char_road = '.'
char_wall = '#'

print("Height of the maze:")
H = int(float(sys.stdin.readline()))
print("Width of the maze:")
W = int(float(sys.stdin.readline()))

path_output = "./"
filename_output = "maze_H{}W{}.txt".format(H,W)

print("Objective")
print("1 : random maze")
print("2 : random maze with specific start and goal")
print("3 : all roads")
print("4 : all walls")
print("5 : exit")
print("\nInput the command number:")

obj_num = int(float(sys.stdin.readline()))


if obj_num == 1 or obj_num == 2:

    sy = -1
    sx = -1
    gy = -1
    gx = -1
    char_s = '.'
    char_g = '.'
    
    if obj_num == 2:
        print("start (input in the form of \'y x\',")
        print("where 0 <= y < {} and 0 <= x < {}):".format(H,W))
        sy,sx = map(int,sys.stdin.readline().split())
        print("goal (input like \'y x\',")
        print("where 0 <= y < {} and 0 <= x < {}):".format(H,W))
        gy,gx = map(int,sys.stdin.readline().split())

        print("Do you specify the start and the goal with alphabetical letters? (y or n)")
        ans_sg = sys.stdin.readline().strip()
        if ans_sg.lower()[0] == "y":
            print("Using lowercase(s and g)? (y or n)")
            ans_sg2 = sys.stdin.readline().strip()
            if ans_sg2.lower()[0] == "y":
                char_s = 's'
                char_g = 'g'
            else:
                char_s = 'S'
                char_g = 'G'
            #end if
        #end if
    #end if

    maze = [ "" for _ in range(H) ]
    for y in range(H):
        for x in range(W):
            randval = random.random()

            if y == sy and x == sx:
                maze[y] += char_s
            elif y == gy and x == gx:
                maze[y] += char_g
            elif randval < 0.7:
                maze[y] += char_road
            else:
                maze[y] += char_wall
            #end if
        #end for
    #end for
elif obj_num == 3:
    maze = [ char_road * W for _ in range(H) ]
elif obj_num == 4:
    maze = [ char_wall * W for _ in range(H) ]
else:
    print("exit")
    sys.exit()
#end if


str_clip = ""
for y in range(H):
    str_clip += maze[y] + "\n"
    print(maze[y])
#end for

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
