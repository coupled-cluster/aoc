"""Read-in"""
def read_in(name):
  dat   = open(name,"rb")
  lines = [i.rstrip().replace("(","( ").replace(")"," )").split() for i in dat.readlines()]
  dat.close()
  return lines

"""Recusive generation of tree structure"""
def generate(sl,pdict={"(":1,")":-1}):
  if "(" in sl:
    pl    = [pdict[i] if i in pdict.keys() else 0 for i in sl]
    psl   = [sum(pl[:i]) for i in range(len(pl))]
    liste = []
    i     = 0
    while i < len(pl):
      if pl[i] != 0:
        subl = []
        while i < len(pl)-1 and psl[i+1] != 0:
          i += 1
          subl.append(sl[i])
        liste.append(generate(subl[:-1]))
      else:
        liste.append(sl[i])
      i += 1
    return liste
  else:
    return sl

"""Recursive evaluation of tree structure"""
def evaluate(tree,typ=0):
  if type(tree) == list:
    # Addition first
    if typ == 1:
      vl = [evaluate(tree[0],typ=typ)]
      for i in range(1,len(tree),2):
        op  = tree[i]
        dv  = evaluate(tree[i+1],typ=typ)
        if op == "+":
          vl[-1] += dv
        else:
          vl.append(op)
          vl.append(dv)
    else:
      vl = list(tree)
    # Remaining operations
    val = evaluate(vl[0],typ=typ)
    for i in range(1,len(vl),2):
      op = vl[i]
      dv = evaluate(vl[i+1],typ=typ)
      if op == "+":
        val += dv
      elif op == "*":
        val *= dv
    return val
  else:
    return int(tree)

# Read in
lines = read_in("input1")
# Evaluation
val1  = 0
val2  = 0
for i in lines: 
  tree  = generate(i)
  val1 += evaluate(tree,typ=0)
  val2 += evaluate(tree,typ=1)
# Answer part 1
print val1
# Answer part 2
print val2
