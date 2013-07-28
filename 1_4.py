# buffon's needle
import random,math
N=0
Nt=100000
a=1;b=1
for i in range(Nt):
  xc=random.uniform(0.,b/2.0)
  phi=random.uniform(0.,math.pi/2)
  
  xt=xc-a/2.0*math.cos(phi)
  if xt<0:
    N+=1

print 2.0*Nt/N
