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
plt.hist(data, bins=ballbins+1) 
fig1 = plt.gcf()
fig1.savefig("histo.png", format='png', dpi=100)
#plt.show()
plt.close('all') 

# crude histo
for x in range(data[0]-1,data[-1]+2):
    print("-" * data.count(x) + " " + str(x) )

