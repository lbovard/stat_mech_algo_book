#algorithm 1.6
from random import randint
grid={1:[2,4,0,0],2:[3,5,1,0],3:[0,6,2,0],
      4:[5,7,0,1],5:[6,8,4,2],6:[0,9,5,3],
      7:[8,0,0,4],8:[9,0,7,5],9:[0,0,8,6]}

Nt=100000
pos=1
visit=[0 for x in range(0,10)]
for i in range(Nt):
  #generate one of the possible neighbours
  new_pos=grid[pos][randint(0,3)]
  #check if the site is a new site, 0=same site
  if new_pos is 0:
    visit[pos]+=1
  else:
    pos=new_pos
    visit[pos]+=1 

#note the probabilities are NOT equal!!
print map(lambda x: float(x)/float(Nt), visit[1:10])
