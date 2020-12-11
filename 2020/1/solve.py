"""Read-in routine"""
def read_in(name):
  dat   = open(name,"rb")
  liste = [int(i.rstrip()) for i in dat.readlines()]
  liste.sort()
  dat.close()
  return liste

"""Recursive find routine"""
def find(liste,refval,level):
  if level == 0: 
    return int(not refval)
  else:
    for i in range(len(liste)-level+1):
      val = liste[i]
      low = find(liste[i+1:],refval-val,level-1)
      if low!=0: break
    return low*val

# Read list
liste   = read_in("input1")
# Print result part 1
print find(liste,2020,2)
# Print result part 2
print find(liste,2020,3)
