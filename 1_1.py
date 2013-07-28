# obtain Pi from Monte Carlo simulation
import random

N=0
for i in range(4000):
	x=random.uniform(-1,1)
	y=random.uniform(-1,1)
	if (x*x + y*y) < 1:
		N+=1

print N/1000.
