"""Read-in"""
def read_in(name):
  dat   = open(name,"rb")
  liste = dat.readlines()
  dat.close()
  return [list(i.rstrip()) for i in liste]

"""Check for tree"""
def check(field,pos):
  val = field[pos[0]][pos[1]]
  if val == ".":
    return 0
  elif val == "#":
    return 1

"""Map position from continuous to finite map"""
def map(pos,width):
  newpos = list(pos)
  while newpos[1] >= width:
    newpos[1] -= width
  return newpos

"""Move the sleigh"""
def move(pos,vec,width,length=2):
  newpos = [pos[i]+vec[i] for i in range(length)]
  return map(newpos,width)

"""Counting routine"""
def count_trees(field,width,height,vec):
  pos    = [0,0]
  count = check(field,pos)
  for i in range((height-1)/vec[0]):
    pos    = move(pos,vec,width)
    count += check(field,pos)
  return count

# Read in field
field  = read_in("input1")
width  = len(field[0])
height = len(field)

# define sleigh
vecs  = [[1,1],[1,3],[1,5],[1,7],[2,1]]
prod  = 1
for i in vecs:
  count = count_trees(field,width,height,i)
  prod *= count
# Answer part 1
print count_trees(field,width,height,vecs[1])
# Answer part 2
print prod
