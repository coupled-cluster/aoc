"""Read-in"""
def read_in(name):
  dat   = open(name,"rb")
  lines = [i.rstrip() for i in dat.readlines()]
  dat.close()
  classes = {}
  for i in range(lines.index("")):
    sl = lines[i].split(":")
    rl = [range(int(a.split("-")[0]),int(a.split("-")[1])+1) for a in sl[1].replace(" ","").split("or")]
    classes[sl[0]] = rl[0]+rl[1]
  ticket  = [int(a) for a in lines[lines.index("your ticket:")+1].split(",")]
  tickets = [[int(a) for a in lines[i].split(",")] for i in range(lines.index("nearby tickets:")+1,len(lines))]
  return classes, ticket, tickets

"""Create whitelist of values"""
def make_raster(classes):
  whitelist = []
  for i in classes:
    whitelist += [a for a in classes[i] if a not in whitelist]
  whitelist.sort()
  return whitelist

"""Check values"""
def checksum(tickets,classes):
  whitelist = make_raster(classes)
  return sum([sum([a for a in i if a not in whitelist]) for i in tickets])

"""Find valid tickets"""
def valid_tickets(classes,ticket,tickets):
  whitelist = make_raster(classes)
  vtickets  = [ticket]+[i for i in tickets if len([a for a in i if a not in whitelist])==0]
  return vtickets

"""Assign classes"""
def assign_classes(classes,tickets):
  oks = [classes.keys() for i in tickets[0]]
  for i in range(len(oks)):
     for a in classes:
       if len([1 for e in tickets if e[i] not in classes[a]]) != 0:
         oks[i].pop(oks[i].index(a))
  ioks = [[len(oks[i]),oks[i],i] for i in range(len(oks))]
  ioks.sort()
  dioks = [[ioks[0][2],ioks[0][1][0]]]+[[ioks[i][2],[a for a in ioks[i][1] if a not in ioks[i-1][1]][0]]  for i in range(1,len(ioks))]
  dioks.sort()
  return [i[1] for i in dioks]

classes, ticket,tickets = read_in("input1")
vtickets = valid_tickets(classes,ticket,tickets)
# Answer part 1
print checksum(tickets,classes)
# Answer part 2
oks     = assign_classes(classes,vtickets)
iticket = [ticket[i] for i in range(len(oks)) if "departure" in oks[i]]
result  = reduce((lambda x, y: x * y), iticket)
print result
