"""Read-in"""
def read_input(filename):
  # raw data
  dat = open(filename,"rb")
  liste = [i.rstrip() for i in dat.readlines()]
  dat.close()
  # Put into dictionary
  kdict = {}
  for i in range(len(liste)):
    sl = liste[i].replace(" contain ",",")
    sl = sl.replace(".","")
    sl = sl.replace(", ",",")
    sl = sl.replace(" bags","")
    sl = sl.replace(" bag","")
    sl = sl.split(",")
    key = sl[0]
    kl  = []
    for a in range(1,len(sl)):
      if sl[a] != "no other":
        count = int(sl[a].split()[0])
        color = sl[a].replace(str(count)+" ","")
        kl.append([color,count])
    kdict[key] = kl
  return kdict

"""Find contained bag"""
def find_bag(kdict,name):
  liste = []
  for i in kdict:
    for a in kdict[i]:
      if a[0] == name:
        liste.append(i)
        break
  return liste

"""recursive bag find"""
def recursive_find(kdict,val,liste):
  nl = find_bag(kdict,val) 
  for i in nl:
    if i not in liste:
      liste.append(i)
      recursive_find(kdict,i,liste)

"""recursive count"""
def rec_count(kdict,val):
  nl    = kdict[val]
  count = 1
  if len(nl) != 0:
    count = 1+sum([rec_count(kdict,i[0])*i[1] for i in nl])
  return count
      

# read in dictionary
kdict = read_input("input1")
# first answer
tliste = []
recursive_find(kdict,"shiny gold",tliste)
print len(tliste)
# second answer
print rec_count(kdict,"shiny gold") - 1
