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
import logging
logging.basicConfig(format='%(levelname)s:%(message)s', filename='bingo.log', level=logging.DEBUG)



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
freespace = ["Free"]
allballs=colb + coli + coln + colg + colo + freespace

rawinput=str()
# index of all names. balls (0-74) and freespace (75). called are set to green.
idxToBall=dict()
# list of balls on a card. uses index to get names.
cardcolb=list()
cardcoli=list()
cardcoln=list()
cardcolg=list()
cardcolo=list()
winners=list()



########## functions ##########



def flowerBox(message):
    """ print a message in a flower box """
    mlen=len(message)
    print("-" * ( 6 + mlen + 6))
    print("-" * 5 + " " + message + " " + "-" * 5)
    print("-" * ( 6 + mlen + 6))
    logging.info('event %s',message)



def newcard():
    """ create a new bingo card """
    # TODO list of card objects
    # shuffle each column to create a new card
    global cardcolb
    global cardcoli
    global cardcoln
    global cardcolg
    global cardcolo
    global winners
    # load a list of numbers matching index into the columns
    cardcolb = list(range(15))
    cardcoli = list(range(15,30))
    cardcoln = list(range(31,45))
    cardcolg = list(range(46,60))
    cardcolo = list(range(61,75))
    # shuffle the columns
    random.shuffle(cardcolb)
    random.shuffle(cardcoli)
    random.shuffle(cardcoln)
    random.shuffle(cardcolg)
    random.shuffle(cardcolo)
    # add a free space to the card
    cardcoln[2]=75
    # keep first 5
    cardcolb[5:]=[]
    cardcoli[5:]=[]
    cardcoln[5:]=[]
    cardcolg[5:]=[]
    cardcolo[5:]=[]
    # log it
    logging.debug('new card col b %s ',cardcolb)
    logging.debug('new card col i %s ',cardcoli)
    logging.debug('new card col n %s ',cardcoln)
    logging.debug('new card col g %s ',cardcolg)
    logging.debug('new card col o %s ',cardcolo)
    # win combos
    winners=[cardcolb,cardcoli,[cardcoln[0],cardcoln[1],cardcoln[3],cardcoln[4]],cardcolg,cardcolo, \
             [cardcolb[0],cardcoli[0],cardcoln[0],cardcolg[0],cardcolo[0]], \
             [cardcolb[1],cardcoli[1],cardcoln[1],cardcolg[1],cardcolo[1]], \
             [cardcolb[2],cardcoli[2],cardcolg[2],cardcolo[2]], \
             [cardcolb[3],cardcoli[3],cardcoln[3],cardcolg[3],cardcolo[3]], \
             [cardcolb[4],cardcoli[4],cardcoln[4],cardcolg[4],cardcolo[4]], \
             [cardcolb[0],cardcoli[1],cardcolg[3],cardcolo[4]], \
             [cardcolb[4],cardcoli[3],cardcolg[1],cardcolo[0]], \
             [cardcolb[0],cardcolb[4],cardcolo[0],cardcolo[4]]]
    print(winners)



def playgame():
    """ would you like to play a game """
    global allballs
    global winners
    global idxToBall
    global rawinput

    # os.system('clear||cls')
    print("")
    print("")
    print("")
    print("")
    flowerBox("New Game")
    print("")

    # create a fresh list of balls, pulled balls will be change to green
    # index the new balls 
    idxToBall = { i : allballs[i] for i in range(0, len(allballs) ) }
    # print(idxToBall)
    # pull free space
    pullball(75)

    # shuffle a list of numbers
    pullOrder=list(range(75))
    random.shuffle(pullOrder)
    logging.debug('new pull order for balls %s ',pullOrder)

    # loop through the list of pulled balls
    for x in range(75):
        # print(pullOrder[x])
        pullball(pullOrder[x])
        printcalled()
        printcard()
        print("")
        print(str(x+1) + " balls called")

        # check for a bingo
        # print(pullOrder[:x+1])
        for j in winners:
            # print("   " + str(len(j)) + "   " + str(j))
            # print("    " + str(len(set(j).intersection(pullOrder[:x+1]))) + "   " + str(set(j).intersection(pullOrder[:x+1])))
            if len(j) == len(set(j).intersection(pullOrder[:x+1])):
                flowerBox("BINGO!")
                for k in j:
                    # print(k)
                    print(idxToBall[k], end='  ')
                print("")

        print("Press <Enter> to draw again, enter \"b\" for a Bingo or enter \"q\" to quit.")
        rawinput=input()
        if str(rawinput) == "":
            os.system('clear||cls')
            continue
        if str(rawinput) == "b":
            flowerBox("BINGO!")
            break
        if str(rawinput) == "q":
            flowerBox("Game Over")
            exit()
        if str(rawinput) == "x":
            flowerBox("You Died")
            exit()

    # play again with or without a new card
    print("Press <Enter> to play again, enter \"n\" for a new Bingo card or enter \"q\" to quit.")
    rawinput=input()
    if str(rawinput) == "q":
        flowerBox("Game Over")
        exit()
    if str(rawinput) == "x":
        flowerBox("You Died")
        exit()
    if str(rawinput) == "n":
        newcard()



def printcalled():
    """ print the called ball list. called ball will be green """
    global headings
    global space
    print("")
    print(headings)
    for x in range(15):
        print(idxToBall[x] + space + \
              idxToBall[x+15] + space + \
              idxToBall[x+30] + space + \
              idxToBall[x+45] + space + \
              idxToBall[x+60])



def printcard():
    """ print the bingo card. called balls will be green """
    global headings
    global space
    print("")
    print(headings)
    for x in range(5):
        print( idxToBall[cardcolb[x]] + space + \
               idxToBall[cardcoli[x]] + space + \
               idxToBall[cardcoln[x]] + space + \
               idxToBall[cardcolg[x]] + space + \
               idxToBall[cardcolo[x]])



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

