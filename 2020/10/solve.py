"""Read-in"""
def read_in(name):
  dat   = open(name,"rb")
  liste = [0]+[int(i.rstrip()) for i in dat.readlines()]
  dat.close()
  liste.sort()
  return liste

"""Differential count"""
def dcount(liste):
  dliste = [liste[i]-liste[i-1]for i in range(1,len(liste))]+[3]
  cliste = [dliste.count(i) for i in range(4)]
  return cliste

"""Memory backtracking"""
def fast(liste,cliste,final):
  cliste[-1] = 1
  for i in range(len(liste)-2,-1,-1):
    for a in range(3):
      if i+a+1 >= len(liste) or liste[i]+3 < liste[i+a+1]: break
      cliste[i] += cliste[i+a+1]
  return cliste[0]
  
# read in
liste = read_in("input1")
# Answer part 1
dcl = dcount(liste)
print dcl[1]*dcl[3]
# Answer part 2
cliste = [0 for i in liste]
print fast(liste,cliste,liste[-1]+3)
