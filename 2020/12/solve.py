import math

"""Read-in"""
def read_in(name):
  dat   = open(name,"rb")
  liste = [i.rstrip() for i in dat.readlines()]
  dat.close()
  return [[i[0],i[1:]] for i in liste]

# Rounding routine
def rint(number,acc=0.001):
  return int(round(number+acc,0))

"""Move ferry"""
def move(pos,command,typ=0):
  ct,cv = command[0],int(command[1])
  ang   = math.radians(cv)
  lx    = rint(math.cos(ang)-1)*pos[2] - rint(math.sin(ang)*pos[3])
  ly    = rint(math.cos(ang)-1)*pos[3] + rint(math.sin(ang)*pos[2])
  rx    = rint(math.cos(-ang)-1)*pos[2] - rint(math.sin(-ang)*pos[3])
  ry    = rint(math.cos(-ang)-1)*pos[3] + rint(math.sin(-ang)*pos[2])
  if typ == 1:
    moves = {"E":[0,0,cv,0],"W":[0,0,-cv,0],"N":[0,0,0,cv],"S":[0,0,0,-cv],"F":[cv*pos[2],cv*pos[3],0,0],"L":[0,0,lx,ly],"R":[0,0,rx,ry]}
  elif typ == 0:
    moves = {"E":[cv,0,0,0],"W":[-cv,0,0,0],"N":[0,cv,0,0],"S":[0,-cv,0,0],"F":[cv*pos[2],cv*pos[3],0,0],"L":[0,0,lx,ly],"R":[0,0,rx,ry]}
  return [pos[i] + moves[ct][i] for i in range(4)]

"""Manhattan"""
def manhattan(pos):
  return abs(pos[0])+abs(pos[1])

# read instructions
liste = read_in("input1")
# Movements
pos1 = [0,0,1,0]
pos2 = [0,0,10,1]
for i in liste:
  pos1 = move(pos1,i,typ=0)
  pos2 = move(pos2,i,typ=1)
# Answer part 1
print manhattan(pos1)
# Answer part 2
print manhattan(pos2)
