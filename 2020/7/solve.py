"""Read-in"""
def read_input(filename):
  dat = open(filename,"rb")
  liste = [i.rstrip() for i in dat.readlines()]
  dat.close()
  kdict = {}
  for i in range(len(liste)):
    rdict = {" contain ":",",".":"",", ":","," bags":""," bag":""}
    for a in rdict:
      liste[i] = liste[i].replace(a,rdict[a])
    sl = liste[i].split(",")
    kl = []
    for a in range(1,len(sl)):
      if sl[a] != "no other":
        count = int(sl[a].split()[0])
        color = sl[a].replace(str(count)+" ","")
        kl.append([color,count])
    kdict[sl[0]] = kl
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

"""Recursive bag find"""
def recursive_find(kdict,val,liste):
  nl = find_bag(kdict,val) 
  for i in nl:
    if i not in liste:
      liste.append(i)
      recursive_find(kdict,i,liste)

"""Recursive count"""
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
