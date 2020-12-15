"""Perform fast iterations"""
def iterate(liste,maxi):
  index = len(liste)-1
  idict = {liste[i]:i for i in range(index)}
  val   = liste[-1]
  for i in range(index,maxi-1):
    try:
      tmp = i - idict[val]
    except:
      tmp = 0
    idict[val] = i
    val        = tmp
  return val

liste = [5,1,9,18,13,8,0]
#liste = [0,3,6]

# Answer part 1
print iterate(liste,2020)
# Answer part 2
print iterate(liste,30000000)
