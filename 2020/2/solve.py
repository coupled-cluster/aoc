"""Read-in"""
def read_in(name):
  dat   = open(name,"rb")
  liste = [i.split() for i in dat.readlines()]
  dat.close()
  return liste

"""Policy 1"""
def check_line_1(line):
  cp  = [int(i) for i in line[0].split("-")]
  cv  = line[2].count(line[1][0])
  return int(cv in range(cp[0],cp[1]+1))

"""Policy 2"""
def check_line_2(line):
  cp  = [int(i) for i in line[0].split("-")]
  cp  = [line[2][i-1] for i in cp]
  return int(cp.count(line[1][0])==1)  

# Read in list
liste = read_in("input1")
# Count wrt. policies
count = [0,0]
for i in liste:
  count[0] += check_line_1(i)
  count[1] += check_line_2(i)
print count
