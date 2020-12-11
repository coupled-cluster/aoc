"""Read in"""
def read_in(name):
  dat   = open(name,"rb")
  liste = [i.rstrip() for i in dat.readlines()]
  dat.close()
  seats = [list(i) for i in liste]
  return seats

"""Find nearest seats"""
def find_near(seats,x,y,maxx,maxy,empty=0):
  dliste = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
  liste  = []
  for i in dliste:
    nx = x + i[0]
    ny = y + i[1]
    if not check_bound(nx,ny,maxx,maxy): continue
    while seats[nx][ny] == "." and empty: 
      if check_bound(nx+i[0],ny+i[1],maxx,maxy):
        nx += i[0]
        ny += i[1]
      else:
        break
    liste.append(seats[nx][ny])
  return liste

"""Check bound"""
def check_bound(x,y,maxx,maxy):
  return x >= 0 and x <= maxx and y >= 0 and y <= maxy

"""Iterative procedure"""
def iterate(seats,empty=0,maxo=4):
  change  = 0
  newseat = [list(i) for i in seats]
  maxx    = len(seats)-1
  maxy    = len(seats[0])-1
  for i in range(maxx+1):
    for a in range(maxy+1):
      liste  = find_near(seats,i,a,maxx,maxy,empty=empty)
      ocount = liste.count("#")
      if seats[i][a] == "L" and ocount == 0:
        newseat[i][a] = "#"
        change = 1
      elif seats[i][a] == "#" and ocount >= maxo:
        newseat[i][a] = "L"
        change = 1
  return change,newseat

"""Count occupied seats"""      
def count_seats(seats):
  return sum([i.count("#") for i in seats])

# Answer part 1
seats = read_in("input1")
change = 1
while change:
  change,seats = iterate(seats)
print count_seats(seats)
# Answer part 2
seats = read_in("input1")
change = 1
while change:
  change,seats = iterate(seats,empty=1,maxo=5)
print count_seats(seats)
