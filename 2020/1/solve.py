"""Read-in routine"""
def read_in(name):
  dat   = open(name,"rb")
  liste = [int(i.rstrip()) for i in dat.readlines()]
  liste.sort()
  dat.close()
  return liste

"""Recursive find routine"""
def find(liste,refval,level):
  # Check if sum is correct (reduced refval is zero)
  if level == 0:
    if refval == 0:
      return 1
    else:
      return 0
  # go through remaining list and recursive call with reduced refavl
  else:
    for i in range(len(liste)-level+1):
      val = liste[i]
      low = find(liste[i+1:],refval-val,level-1)
      if low!=0: break
    if low:
      return low*val
    else:
      return 0

# Read list
liste   = read_in("input1")
# Print result part 1
print find(liste,2020,2)
# Print result part 2
print find(liste,2020,3)
