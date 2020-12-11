"""Read-in"""
def read_in(name):
  dat   = open(name,"rb")
  liste = dat.readlines()
  dat.close()
  return liste

"""Policy 1"""
def check_line_1(line):
  sl  = line.split()
  cp  = [int(i) for i in sl[0].split("-")]
  cv  = sl[2].count(sl[1][0])
  if cv in range(cp[0],cp[1]+1):
    return 1
  else:
    return 0

"""Policy 2"""
def check_line_2(line):
  sl  = line.split()
  cp  = [int(i) for i in sl[0].split("-")]
  cp  = [sl[2][i-1] for i in cp]
  if cp.count(sl[1][0]) == 1: 
    return 1
  else:
    return 0


# Read in list
liste = read_in("input1")

# Count wrt. policies
countp1 = 0
countp2 = 0
for i in liste:
  countp1 += check_line_1(i)
  countp2 += check_line_2(i)
# Print counts
print countp1
print countp2
