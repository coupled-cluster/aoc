"""Read in"""
def read_in(name):
  dat   = open(name,"rb")
  lines = [i.rstrip() for i in dat.readlines()]
  dat.close()
  time = int(lines[0])
  bus  = ["x" if i=="x" else int(i) for i in lines[1].split(",")]
  return time,bus

"""Calculate modulus for busses"""
def find_fast(bus,time):
  rbus  = [i for i in bus if i!="x"]
  liste = [i-time%i if time%i!=0 else 0 for i in bus if i!="x"]
  minv  = min(liste)
  mini  = liste.index(minv)
  return minv*rbus[mini]

"""Find minimum offset"""
def find_min(bus):
  rbus      = [[bus[i],i] for i in range(len(bus)) if bus[i]!="x"]
  freq, off = 1,0
  for i in rbus:
    val = (off+freq+i[1])%i[0]
    j   = 1
    while val != 0:
      j  += 1
      val = (off+j*freq+i[1])%i[0]
    freq,off = freq*i[0],off+j*freq
  return off

# Read input
time,bus = read_in("input1")

# Answer part 1
print find_fast(bus,time)
# Answer day 13
print find_min(bus)
