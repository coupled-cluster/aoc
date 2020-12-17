"""Read in"""
def read_in(name,length=3):
  dat    = open(name,"rb")
  lines  = [i.rstrip() for i in dat.readlines()]
  dat.close()
  active = []
  for i in range(len(lines)):
    for a in range(len(lines[i])):
      if lines[a][i] == "#": active.append([a,i]+[0 for e in range(length-2)])
  return active

"""Recursive generate neighbor coordinates"""
def find_neighbors(coord):
  if len(coord) == 0:
    return [[]]
  ncoords = []
  for i in range(coord[0]-1,coord[0]+2):
    ncoords += [[i] + a for a in find_neighbors(coord[1:])]
  return ncoords
  
"""Update"""
def update(active,length=3):
  xliste = []
  for i in active:
    neighs = find_neighbors(i)
    neighs.remove(i)
    xliste += neighs 
  xliste.sort()
  clist = [[],[]]
  i     = 0
  while len(xliste) > i:
    act   = xliste[i]
    count = 0
    while len(xliste) > i and xliste[i] == act:
      i     += 1
      count += 1
    if count in [2,3]:
      clist[count-2].append(act)
  nactive = []
  for i in active:
    if i in clist[0]+clist[1]:
      nactive.append(i)
  for i in clist[1]:
    if i not in active:
      nactive.append(i)
  return nactive
    
active3 = read_in("input1",length=3)
active4 = read_in("input1",length=4)
for i in range(6):
  active3 = update(active3,length=3)
  active4 = update(active4,length=4)
# Answer part 1
print len(active3)
# Answer part 2
print len(active4)
