#proper Buffon's needle

import random,math
b=1.0
a=1.0
N=0
Nt=100000

for i in range(Nt):
  xc=random.uniform(0,b/2.0)
  dx=random.uniform(0,1)
  dy=random.uniform(0,1)
  gamma=math.sqrt(dx*dx+dy*dy)
  while gamma > 1: 
   dx=random.uniform(0,1)
   dy=random.uniform(0,1)
   gamma=math.sqrt(dx*dx+dy*dy)
  xt=xc-a/2.0*dx/gamma
  if xt <0 :
    N+=1


print 2.0*Nt/N
