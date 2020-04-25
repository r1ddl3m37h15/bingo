#!/bin/bash

set -e

ballsA=`grep "INFO:checkCard" bingo.log | wc -l`
balls4=`grep "INFO:checkCard 4 balls" bingo.log | wc -l`
balls5=`grep "INFO:checkCard 5 balls" bingo.log | wc -l`
echo Bingos Total Games: $ballsA
echo Bingos won with 4 balls: $balls4
echo Bingos won with 5 balls: $balls5

# grep winner bingo.log | sed 's/INFO:winner in //' | python3 ./stats.py

test -f ./histo.png && rm ./image/histo.png

echo ....
echo AAAA
test -f ./histo.png && rm ./image/histoA.png
# grep winnerAtBall bingo.log | sed 's/INFO:winnerAtBall \([0-9]*\) with [0-9]* balls/\1/'
grep winnerAtBall bingo.log | sed 's/INFO:winnerAtBall \([0-9]*\) with [0-9]* balls/\1/' | python3 ./histo.py
#test -f ./histo.png && open -a "Google Chrome" ./image/histo.png
mv ./histo.png ./image/histoA.png

echo ....
echo 4444
test -f ./histo.png && rm ./image/histo.png
# grep winner bingo.log | sed 's/INFO:winnerAtBall //' 
grep 'with 4 balls$' bingo.log | sed 's/INFO:winnerAtBall \([0-9]*\) with 4 balls/\1/' | python3 ./histo.py
#test -f ./histo.png && open -a "Google Chrome" ./image/histo.png
mv ./histo.png ./image/histo4.png

echo ....
echo 5555
test -f ./histo.png && rm ./image/histo.png
# grep winner bingo.log | sed 's/INFO:winnerAtBall //' 
grep 'with 5 balls$' bingo.log | sed 's/INFO:winnerAtBall \([0-9]*\) with 5 balls/\1/' | python3 ./histo.py
#test -f ./histo.png && open -a "Google Chrome" ./image/histo.png
mv ./histo.png ./image/histo5.png

