"""Read-in"""
def read_in(name):
  dat = open(name,"rb")
  lines = [i.rstrip().split() for i in dat.readlines()]
  dat.close()
  return lines

# run program
def run(lines,start=0):
  liste = []
  val   = 0
  while 1:
    if start >= len(lines) or start in liste:
      break
    liste.append(start)
    op,count = lines[start]
    start   += 1
    if op == "acc": val   += int(count)
    if op == "jmp": start += int(count)-1
  suc = int(start==len(lines))
  return suc, val

# read in
lines = read_in("input1")
# answer part 1
print run(lines)[1]
# try all exchanges
for i in range(len(lines)):
  suc = 0
  val = 0
  if lines[i][0] == "jmp":
    lines[i][0] = "nop"
    suc,val = run(lines)
    lines[i][0] = "jmp"
  elif lines[i][0] == "nop":
    lines[i][0] = "jmp"
    suc,val = run(lines)
    lines[i][0] = "nop"
  if suc:
    break
# answer part 2
print val
