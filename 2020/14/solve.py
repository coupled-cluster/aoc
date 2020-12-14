"""Read in"""
def read_in(name):
  dat   = open(name,"rb")
  lines = [i.rstrip() for i in dat.readlines()]
  dat.close()
  return lines

"""Makes binary with specific legth"""
def lbin(integer,length):
  val = str(bin(integer))[2:]
  val  = "".join(["0" for i in range(length-len(val))]) + val
  return val

"""Recusive list of possible values"""
def rec_genlist(rmem,liste,val):
  if len(rmem) == 0:
    liste.append(int(val,2))
    return
  cmem = list(rmem)
  pval = cmem.pop(0)
  if pval in ["0","1"]:
    rec_genlist(cmem,liste,val+pval)
  else:
    rec_genlist(cmem,liste,val+"0")
    rec_genlist(cmem,liste,val+"1")

"""Execute lines"""
def execute(lines,version=1):
  mems = {}
  mask = "".join(["X" for i in range(36)])
  for i in lines:
    sl = i.split()
    if sl[0] == "mask":
      mask = sl[2]
      continue
    val  = int(sl[2])
    mem  = int(sl[0].replace("[","]").split("]")[1])
    fmem = []
    if version==1:
      val  = lbin(val,36)
      val  = int("".join([val[i] if mask[i]=="X" else mask[i] for i in range(36)]),2)
      fmem.append(mem)
    elif version == 2:
      mem  = lbin(mem,36)
      mem  = [mem[i] if mask[i]=="0" else mask[i] for i in range(36)]
      rec_genlist(mem,fmem,"")
    for a in fmem:
      mems[a] = val
  return mems.values()

# Read in lines
lines = read_in("input1")
# Answer part 1
vals = execute(lines,version=1)
print sum(vals)
# Answer part 2
vals = execute(lines,version=2)
print sum(vals)
