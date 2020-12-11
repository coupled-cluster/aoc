"""Read-in data"""
def read_in(name):
  dat   = open(name,"rb")
  liste = dat.readlines()
  dat.close()
  passports = []
  pp        = {}
  for i in liste:
    if len(i.rstrip().split()) == 0:
      passports.append(pp)
      pp = {}
    else:
      for a in i.rstrip().split():
        key,val = a.split(":")
        pp[key]=val
  if len(pp.keys()) != 0:
    passports.append(pp)
  return passports

"""Check validity of passport"""
def check_rigged(pp,kdict):
  ok = 1
  for i in kdict.keys():
    if i not in pp.keys():
      ok = 0
    else:
      ok = int(kdict[i](pp[i]))
    if not ok: break
  return ok

"""General check routines"""
# Integer read-in and check
def make_int(string):
  try:
    vint = int(string)
    return 1,vint
  except:
    return 0,0
# Length check
def check_length(string,length):
  return len(string) == length
# Integer range check
def check_intrange(string,lower,upper):
  ok,vint = make_int(string)
  return ok and vint >= lower and vint <= upper

"""Separate checking routines"""
# default routine -> no check
def defv(string):
  return 1
# check for cbyr, ciyr, ceyr
def cbyr(string):
  return check_length(string,4) and check_intrange(string,1920,2002)
def ciyr(string):
  return check_length(string,4) and check_intrange(string,2010,2020)
def ceyr(string):
  return check_length(string,4) and check_intrange(string,2020,2030)
# check for cecl
def cecl(string):
  return string in ["amb","blu","brn","gry","grn","hzl","oth"]
# check for cpid
def cpid(string):
  return check_length(string,9) and make_int(string)[0]
# check for chcl
def chcl(string):
  refl = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
  return check_length(string,7) and string[0] == "#" and sum([1 if i in refl else 0 for i in string[1:]]) == 6
# check for chgt
def chgt(string):
  return string[-2:] == "cm" and check_intrange(string[0:-2],150,193) or string[-2:] == "in" and check_intrange(string[0:-2],59,76)


# Read in passports and set dictionaries for checks
pps  = read_in("input1")
kdict1 = {"byr":defv,"iyr":defv,"eyr":defv,"hgt":defv,"hcl":defv,"ecl":defv,"pid":defv}
kdict2 = {"byr":cbyr,"iyr":ciyr,"eyr":ceyr,"hgt":chgt,"hcl":chcl,"ecl":cecl,"pid":cpid}

# countimng
count1 = 0
count2 = 0
for i in pps:
  count1 += check_rigged(i,kdict1)
  count2 += check_rigged(i,kdict2)
# Answer part 1
print count1
# Answer part 2
print count2
