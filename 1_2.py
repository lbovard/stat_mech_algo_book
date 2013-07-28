# use Metropolis alogirhtm to compute pi
import random

delta=0.3
N=0
x=1
y=1

for i in range(4000):
	dx=random.uniform(-delta,delta)
	dy=random.uniform(-delta,delta)
	if abs(x+dx) < 1 and abs(y+dy) <1:
		x=x+dx
		y=y+dy
	if (x*x+y*y) <1:
		N+=1

print N/1000.0
