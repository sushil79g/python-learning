# Paste your function here
def closest_power(base, num):
  power = 0
  total =0
  while total <= num:
    power += 1
    total = base**power
  next = power - 1
  if (base**power)-num >= num-(base**next):
    return(next)
  else:
    return(power)