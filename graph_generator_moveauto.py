#! python3
# -*- coding: utf-8 -*-

import random
import sys
import numpy as np
import pyperclip

class UnionFind(): #size-based
    
    def __init__(self, n):
        self.n = n
        self.parent = np.array([ i for i in range(n) ])
        self.treesize = np.array([1]*(n))
    #end def(__init__)
        
    def root(self, x):
        if(self.parent[x] == x):
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]
        #end if
    #end def(root)
    
    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if (x == y):
            return 
        elif (self.treesize[x] > self.treesize[y]):
            self.treesize[x] += self.treesize[y]
            self.parent[y] = x
        else:
            self.treesize[y] += self.treesize[x]
            self.parent[x] = y
        #end if
    #end def(unite)
            
    def sametree(self, x, y):
        return self.root(x) == self.root(y)
    #end def(sametree)
    
    def gettreesize(self, x):
        return self.treesize[self.root(x)]
    #end def(gettreesize)
    
#end def(class UnionFind)

Nleft = 9
Nright = 30
N = random.randint(Nleft,Nright)

flag_output = False
flag_istree = False
flag_allowmultipleedge = False
flag_allowselfloop = False
flag_1indexed = True
flag_isconnected = True
flag_isdirected = False
flag_printNandM = True
flag_copyclipboard = False

Mleft = 1
Mright = 2*N

if flag_istree:
    M = N-1
else:
    M = random.randint(Mleft,Mright)
#end if

if flag_1indexed:
    shift = 1
else:
    shift = 0
#end if


path_output = "./"
filename_output = "input.txt"

notused = np.array([ np.array([ True for _ in range(N)]) for __ in range(N) ])

union_find = UnionFind(N)


def make_an_edge():
    global notused
    point0 = random.randint(0,N-1)
    point1 = random.randint(0,N-1)

    while ( ( not flag_allowselfloop and point0 == point1)
            or ( not flag_allowmultipleedge and not notused[point0][point1]) ):
        point0 = random.randint(0,N-1)
        point1 = random.randint(0,N-1)
    #end while

    if ( not flag_allowmultipleedge ):
        notused[point0][point1] = False
        if ( not flag_isdirected ):
            notused[point1][point0] = False
        #end if
    #end if
    return point0,point1
#end def




str_clip = ""


if flag_isconnected:
    M = 0
    while True:
        p0,p1 = make_an_edge()
        str_clip += "{} {}\n".format(p0+shift,p1+shift)
        M += 1
        union_find.unite(p0,p1)
        if union_find.gettreesize(0) == N:
            break
        #end if
    #end while
else:
    for _ in range(M):
        p0 = 0
        p1 = 0
        if flag_istree:
            while ( union_find.sametree(p0,p1) ):
                p0,p1 = make_an_edge()
            #end while
            union_find.unite(p0,p1)
        else:
            p0,p1 = make_an_edge()
        #end if
        str_clip += "{} {}\n".format(p0+shift,p1+shift)
    #end for
#end if

if flag_printNandM:
    str_clip = "{} {}\n".format(N,M) + str_clip
#end if


print(str_clip)

if flag_copyclipboard:
    pyperclip.copy(str_clip)
#end if

if flag_output:
    with open(path_output+filename_output,mode="w") as file_out:
        file_out.write(str_clip)
    #end with
#end if
