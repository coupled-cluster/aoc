"""Read-in"""
def read_in(name):
  dat   = open(name,"rb")
  liste = dat.readlines()
  dat.close()
  return [list(i.rstrip()) for i in liste]

"""Counting routine"""
def count_trees(field,width,height,vec):
  pos   = [0,0]
  count = int(field[pos[0]][pos[1]] == "#")
  for i in range((height-1)/vec[0]):
    pos = [pos[i]+vec[i] for i in range(len(pos))]
    while pos[1] >= width:
      pos[1] -= width
    count += int(field[pos[0]][pos[1]] == "#")
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
