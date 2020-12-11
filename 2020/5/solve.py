"""Read-in"""
def read_in(name):
  dat   = open(name,"rb")
  liste = [i.rstrip() for i in dat.readlines()]
  dat.close()
  return liste

"""Convert string into row, seat and id"""
def convert(line):
  ri = int("".join(["0" if line[i] == "F" else "1" for i in range(7)]),2)
  si = int("".join(["0" if line[i] == "L" else "1" for i in range(7,10)]),2)
  id = 8*ri+si
  return ri,si,id

# read in list and convert it
liste = read_in("input1")
idl   = [convert(i)[2] for i in liste]
idl.sort()

# Answer part 1
print idl[-1]
# Answer part 2
for i in range(1,len(idl)-1):
  if idl[i] != idl[i+1]-1:
    print idl[i+1]-1
    break
