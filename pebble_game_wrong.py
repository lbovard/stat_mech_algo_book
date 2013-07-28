#example to illustrate why naive pebble game is wrong

from random import randint
grid={1:[2,4],2:[1,3,5],3:[2,6],4:[1,5,7],
      5:[2,4,6,8],6:[3,5,9],7:[4,8],8:[5,7,9],
      9:[6,8]}

Nt=10000
pos=1
visit=[0 for x in range(0,10)]
for i in range(Nt):
  #generate one of the possible neighbours
  new_pos=randint(0,len(grid[pos])-1)
  pos=grid[pos][new_pos]
  visit[pos]+=1

#note the probabilities are NOT equal!!
print map(lambda x: float(x)/float(Nt), visit[1:10])
