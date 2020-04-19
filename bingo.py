#!/usr/bin/env /usr/local/bin/python3
""" A bingo game that I wrote to learn python3 """
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
# furnished to do so, subject to the following conditions:
#
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

__version__ = '0.0.1'
__author__ = 'Jeff Suess'
__license__ = 'MIT'

import random, sys
from termcolor import colored
import os


########## global vars ##########


# column spacer
space = "   "
# headings for the called balls list and the bingo card
headings = colored("_B__" + space + "_I__" + space + "_N__" + space + "_G__" + space + "_O__","cyan")

# ball names
colb = ["B  1","B  2","B  3","B  4","B  5","B  6","B  7","B  8","B  9","B 10","B 11","B 12","B 13","B 14","B 15"]
coli = ["I 16","I 17","I 18","I 19","I 20","I 21","I 22","I 23","I 24","I 25","I 26","I 27","I 28","I 29","I 30"]
coln = ["N 31","N 32","N 33","N 34","N 35","N 36","N 37","N 38","N 39","N 40","N 41","N 42","N 43","N 44","N 45"]
colg = ["G 46","G 47","G 48","G 49","G 50","G 51","G 52","G 53","G 54","G 55","G 56","G 57","G 58","G 59","G 60"]
colo = ["O 61","O 62","O 63","O 64","O 65","O 66","O 67","O 68","O 69","O 70","O 71","O 72","O 73","O 74","O 75"]

raw=str()
idxToBall=dict()
cardcolb=list()
cardcoli=list()
cardcoln=list()
cardcolg=list()
cardcolo=list()


########## functions ##########


def flowerBox(message):
    """ print a message in a flower box """
    mlen=len(message)
    print("-" * ( 6 + mlen + 6))
    print("-" * 5 + " " + message + " " + "-" * 5)
    print("-" * ( 6 + mlen + 6))


def newcard():
    """ create a new bingo card """
    # shuffle each column to create a new card
    global cardcolb
    global cardcoli
    global cardcoln
    global cardcolg
    global cardcolo
    cardcolb = list(range(15))
    cardcoli = list(range(15,30))
    cardcoln = list(range(31,45))
    cardcolg = list(range(46,60))
    cardcolo = list(range(61,75))
    random.shuffle(cardcolb)
    random.shuffle(cardcoli)
    random.shuffle(cardcoln)
    random.shuffle(cardcolg)
    random.shuffle(cardcolo)
    # add a free space to the card
    cardcoln[2]=76


def playgame():
    """ would you like to play a game """
    global colb
    global coli
    global coln
    global colg
    global colo
    global idxToBall
    global raw

    os.system('cls||clear')
    print("")
    print("")
    print("")
    print("")
    flowerBox("New Game")
    print("")

    # get a new list of all balls
    allballs=colb + coli + coln + colg + colo
    # print(allballs)

    # index the new balls
    idxToBall = { i : allballs[i] for i in range(0, len(allballs) ) }

    # add a Free space to the end of the list and pull it
    idxToBall[76]="Free"
    print(idxToBall[76])

    pullball(76)

    # print("")
    # print("idxToBall")
    # print(idxToBall)

    # shuffle a list of numbers
    pullOrder=list(range(75))
    random.shuffle(pullOrder)
    print("")
    print(pullOrder)

    # loop through the list of pulled balls
    for x in range(75):
        os.system('cls||clear')
        # print(pullOrder[x])
        pullball(pullOrder[x])
        printcalled()
        printcard()
        print("")
        print(str(x+1) + " balls called")
        print("Press <Enter> to draw again, enter \"b\" for a Bingo or enter \"q\" to quit.")
        raw=input()
        print(raw)
        if str(raw) == "":
            continue
        if str(raw) == "b":
            flowerBox("BINGO!")
            break
        if str(raw) == "q":
            flowerBox("Game Over")
            exit()
        if str(raw) == "x":
            flowerBox("You Died")
            exit()
    print("Press <Enter> to play again, enter \"n\" for a new Bingo card or enter \"q\" to quit.")
    raw=input()
    print(raw)
    if str(raw) == "q":
        flowerBox("Game Over")
        exit()
    if str(raw) == "x":
        flowerBox("You Died")
        exit()
    if str(raw) == "n":
        newcard()


def printcalled():
    """ print the called ball list. called ball will be green """
    global headings
    global space
    print("")
    # print(headings)
    # for x in range(15):
    #     print(colb[x] + space + coli[x] + space + coln[x] + space + colg[x] + space + colo[x])
    print(headings)
    for x in range(15):
        print(idxToBall[x] + space + idxToBall[x+15] + space + idxToBall[x+30] + space + idxToBall[x+45] + space + idxToBall[x+60])


def printcard():
    """ print the bingo card. called balls will be green """
    global headings
    global space
    print("")
    # for x in range(5):
    #     print( str(cardcolb[x]) + space + str(cardcoli[x]) + space + str(cardcoln[x]) + space + str(cardcolg[x]) + space + str(cardcolo[x]))
    print(headings)
    for x in range(5):
        print( idxToBall[cardcolb[x]] + space + idxToBall[cardcoli[x]] + space + idxToBall[cardcoln[x]] + space + idxToBall[cardcolg[x]] + space + idxToBall[cardcolo[x]])


def pullball(ball):
    """ mark a ball as pulled and print its name. make the ball's name green."""
    # print(ball)
    global idxToBall
    idxToBall[ball] = colored( idxToBall[ball], "green" )
    print("")
    print("")
    print(idxToBall[ball])

     
########## main ##########


newcard()
while True:
    playgame()

