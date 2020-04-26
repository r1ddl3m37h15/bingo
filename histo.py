#!/usr/bin/env /usr/local/bin/python3
""" read STDIN for a list of integers and create a histogram """
#
# MIT License
# 
# Copyright (c) 2020 Jeff Suess
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
# 

__version__ = '0.0.2'
__author__ = 'Jeff Suess'
__license__ = 'MIT'

import sys
import statistics
import matplotlib.pyplot as plt 

# %matplotlib inline

# read a list from STDIN
data = sys.stdin.readlines()

# summary
print("Counted", len(data), "lines.")

# convert list to type int
data = list(map(int, data))

# sort it
data.sort()
# print(data)

ballbins=data[-1]-data[0]-2
print(ballbins)

print("first       " + str( data[0] ))
#print("mode        " + str( statistics.mode(data) ))
print("last        " + str( data[-1] ))
#print("mmode       " + str( statistics.multimode(data) ))
print("median      " + str( statistics.median(data) ))
print("median_low  " + str( statistics.median_low(data) ))
print("median_high " + str( statistics.median_high(data) ))
print("mean        " + str( statistics.mean(data) ))
print("var         " + str( statistics.variance(data) ))
print("pvar        " + str( statistics.pvariance(data) ))
print("stdev       " + str( statistics.stdev(data) ))
# print("normal dist " + str( statistics.NormalDist(data, mu=0.0, sigma=1.0)))


plt.title("Histogram") 
plt.xlabel("Value") 
plt.ylabel("Frequency")
plt.figure(figsize=(6,3))
plt.hist(data, bins=ballbins+3) 
#plt.hist(data, bins='auto') 
fig1 = plt.gcf()
fig1.savefig("histo.png", format='png', dpi=100)
#plt.show()
plt.close('all') 

# crude histo
for x in range(data[0]-1,data[-1]+2):
    print("-" * data.count(x) + " " + str(x) )

