"""Read-in"""
def read(name="input1"):
  dat     = open(name,"rb")
  numbers = [int(i.rstrip()) for i in dat.readlines()]
  dat.close()
  return numbers

"""Recursive check of previous number sum"""
def check_pre(val,lines,depth):
  if depth == 0: 
    return int(val==0)
  okliste = []
  for i in range(len(lines)):
    cl = list(lines)
    vn = cl.pop(i)
    okliste.append(check_pre(val-vn,cl,depth-1))
  return max(okliste)

"""Get first wrong number"""
def check_first(lines,ipre=25):
  for i in range(ipre,len(lines)):
    val  = lines[i]
    refl = lines[i-ipre:i]
    ok   = check_pre(val,refl,2)
    if not ok: break
  return val

"""Find contiguous set"""
def find_set(lines,refval):
  for i in range(len(lines)):
    a   = i
    val = []
    while sum(val) < refval and a < len(lines):
      val.append(lines[a])
      a += 1
    if sum(val) == refval: break
  return val
   
# read in data 
liste = read()
# Answer part 1
val = check_first(liste)
print val
# Answer part 2
vl  = find_set(liste,val)
print min(vl)+max(vl)
