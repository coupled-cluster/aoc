"""Read in"""
def read_in(name):
  # read raw data
  dat = open(name,"rb")
  liste = [i.rstrip() for i in dat.readlines()]
  dat.close()
  # split into groups
  groups = [" " if len(i)==0 else i+"," for i in liste]
  if groups[-1] == " ": groups = groups[:-1]
  groups = [i.split(",")[:-1] for i in "".join(groups).split(" ")]
  return groups

"""yes per group - version 1"""
def get_yes1(gp):
  return len(list(dict.fromkeys(list("".join(gp)))))

"""yes per group - version 2"""
def get_yes2(gp):
  refl = [chr(i) for i in range(97,123)]
  totl = list("".join(gp))
  return [totl.count(i) for i in refl].count(len(gp))

# Read in groups    
groups = read_in("input1")
# Counting
count1 = 0
count2 = 0
for i in groups:
  count1 += get_yes1(i)
  count2 += get_yes2(i)
# Answer part 1
print count1
# Answer part 2
print count2
