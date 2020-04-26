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

__version__ = '0.0.2'
__author__ = 'Jeff Suess'
__license__ = 'MIT'

import random, sys
from termcolor import colored
import os
import logging
import time
import argparse


########## global vars ##########



# column spacer
spacer = "   "
# heading for the called balls list and the bingo card
headings = colored("_B_" + spacer + "_I_" + spacer + "_N_" + spacer + "_G_" + spacer + "_O_","cyan")

# ball names
colb = ["B-1","B-2","B-3","B-4","B-5","B-6","B-7","B-8","B-9","B10","B11","B12","B13","B14","B15"]
coli = ["I16","I17","I18","I19","I20","I21","I22","I23","I24","I25","I26","I27","I28","I29","I30"]
coln = ["N31","N32","N33","N34","N35","N36","N37","N38","N39","N40","N41","N42","N43","N44","N45"]
colg = ["G46","G47","G48","G49","G50","G51","G52","G53","G54","G55","G56","G57","G58","G59","G60"]
colo = ["O61","O62","O63","O64","O65","O66","O67","O68","O69","O70","O71","O72","O73","O74","O75"]
freespace = ["F-S"]
# make FreeSpace 0 so b1 is 1 etc...
allballs=freespace + colb + coli + coln + colg + colo

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
pullOrder=list()



########## functions ##########



def flowerBox(message):
    """ print a message in a flower box """
    mlen=len(message)
    print("")
    print("-" * ( 6 + mlen + 6))
    print("-" * 5 + " " + message + " " + "-" * 5)
    print("-" * ( 6 + mlen + 6))
    logging.info('event %s',message)



def mixTheBalls():
    """ shuffle a list of numbers """
    global idxToBall
    global pullOrder

    # create a fresh list of balls, pulled balls will be change to green
    # index the new balls 
    idxToBall = { i : allballs[i] for i in range(0, len(allballs) ) }
    # print(idxToBall)

    pullOrder=list(range(1,76))
    random.shuffle(pullOrder)
    logging.debug('new pull order for balls %s ',pullOrder)
    # add free space to begining
    pullOrder.insert(0,0)



def newCard(cardNumber=1):
    """ create a new bingo card """
    cardNumber += 1
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
    cardcoln[2]=0
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

    # win combos that are on the card
    winners=[cardcolb,cardcoli,[cardcoln[0],cardcoln[1],cardcoln[3],cardcoln[4]],cardcolg,cardcolo, \
             [cardcolb[0],cardcoli[0],cardcoln[0],cardcolg[0],cardcolo[0]], \
             [cardcolb[1],cardcoli[1],cardcoln[1],cardcolg[1],cardcolo[1]], \
             [cardcolb[2],cardcoli[2],cardcolg[2],cardcolo[2]], \
             [cardcolb[3],cardcoli[3],cardcoln[3],cardcolg[3],cardcolo[3]], \
             [cardcolb[4],cardcoli[4],cardcoln[4],cardcolg[4],cardcolo[4]], \
             [cardcolb[0],cardcoli[1],cardcolg[3],cardcolo[4]], \
             [cardcolb[4],cardcoli[3],cardcolg[1],cardcolo[0]], \
             [cardcolb[0],cardcolb[4],cardcolo[0],cardcolo[4]]]
    # print(winners)
    return {'B':cardcolb, 'I':cardcoli, 'N':cardcoln, 'G':cardcolg, 'O':cardcolo, 'card': cardNumber}



def checkCard(x):
    """ play fast a game """
    global allballs
    global winners
    global idxToBall
    global rawinput
    global pullOrder
    # check for a bingo
    # print(pullOrder[:x+1])
    for j in winners:
        # print("   " + str(len(j)) + "   " + str(j))
        # print("    " + str(len(set(j).intersection(pullOrder[:x+1]))) + "   " + str(set(j).intersection(pullOrder[:x+1])))
        if len(j) == len(set(j).intersection(pullOrder[:x+1])):
            # we have a winner. game over.
            if args.games == None:
                flowerBox("BINGO!")
                print("\a")
            lBingo = []
            for k in j:
                # green
                print(idxToBall[k],end=' ')
                # for log without esc codes 
                lBingo.append(allballs[k])
            # new line for loop above
            print("")
            logging.info('winnerAtBall %s with %s balls',x+1,str(len(lBingo)))
            logging.info('lastBall %s',str(allballs[pullOrder[x]]))
            logging.info('checkCard %s balls: %s',str(len(lBingo)),str(lBingo))
            return 1
    return 0



def playGameA():
    """ play fast a game """
    global allballs
    global winners
    global idxToBall
    global rawinput
    global pullOrder

    mixTheBalls()

    for x in range(4):
        pullBall(pullOrder[x])
    for x in range(4,76):
        pullBall(pullOrder[x])
        if checkCard(x):
            return



def playGameUI():
    """ would you like to play a game """
    global allballs
    global winners
    global idxToBall
    global rawinput
    global pullOrder

    os.system('clear||cls')
    flowerBox("New Game")

    mixTheBalls()

    # pull free space and the first 4 balls

    for x in range(4):
        pullBall(pullOrder[x])

    # loop through the list of pulled balls
    for x in range(4,76):
        pullBall(pullOrder[x])

        printCalled()

        print("")
        print(str(x) + " balls called")

        print("")
        for n in range(1,x+1):
            print(idxToBall[pullOrder[n]], end='  ')
            if (n % 10)==0:
                print("")
        print("")
            
        printCard()

        if checkCard(x):
            time.sleep(2)
            return

        print("")
        print("Press <Enter> to draw again, or enter \"q\" to quit.")
        rawinput=input()
        if str(rawinput) == "":
            os.system('clear||cls')
            continue
        if str(rawinput) == "q":
            flowerBox("Game Over")
            exit()
        # if str(rawinput) == "x":
            flowerBox("You Died")
            exit()



def printCalled():
    """ print the called ball list. called ball will be green """
    global headings
    global spacer

    print("")
    print(headings)
    for x in range(1,16):
        print(idxToBall[x] + spacer + \
              idxToBall[x+15] + spacer + \
              idxToBall[x+30] + spacer + \
              idxToBall[x+45] + spacer + \
              idxToBall[x+60])



def printCard():
    """ print the bingo card. called balls will be green """
    global headings
    global spacer

    print("")
    print(headings)
    for x in range(5):
        print( idxToBall[cardcolb[x]] + spacer + \
               idxToBall[cardcoli[x]] + spacer + \
               idxToBall[cardcoln[x]] + spacer + \
               idxToBall[cardcolg[x]] + spacer + \
               idxToBall[cardcolo[x]])



def pullBall(ball):
    """ mark a ball as pulled and print its name. make the ball's name green."""
    global idxToBall

    idxToBall[ball] = colored( idxToBall[ball], "green" )

    print("")
    print(idxToBall[ball])


     
########## main ##########


logging.basicConfig(format='%(levelname)s:%(message)s', filename='bingo.log', level=logging.DEBUG)

parser = argparse.ArgumentParser(description='Bingo Game')
parser.add_argument('-g', '--games', type=int, 
                    help='AutoPlay i Games')
args = parser.parse_args()

if args.games == None:
    newCard()
    while True:
        playGameUI()
        # play again with or without a new card
        print("")
        print("Press <Enter> to play again, enter \"n\" for a new Bingo card or enter \"q\" to quit.")
        rawinput=input()
        if str(rawinput) == "q":
            flowerBox("Game Over")
            exit()
        if str(rawinput) == "x":
            flowerBox("You Died")
            exit()
        if str(rawinput) == "n":
            newCard()
else:
    for a in range(args.games):
       newCard()
       playGameA()

