Q1.
def cigar_party(cigars, is_weekend):
  if not is_weekend and  60 >= cigars >= 40:
    return True
  elif is_weekend and cigars >= 40:
    return True
  else:
    return False

Q2.
def date_fashion(you, date):
  if you <= 2 and date >= 2 or you >= 2 and date <= 2 :
    return 0
  elif you >= 5 and date >= 8 or you >=8 and date >= 5:
    return 2
  else:
    return 1

Q3.
def squirrel_play(temp, is_summer):
  if not is_summer and 90 >= temp >= 60:
    return True
  elif is_summer and 100 >= temp >=60:
    return True
  else:
    return False

Q4.
def caught_speeding(speed, is_birthday):
  if not is_birthday:
    if speed <= 60:
      return 0
    if 80 >= speed >=61:
      return 1
    if speed >= 81:
      return 2
  if is_birthday:
    if speed <= 65:
      return 0
    if 85 >= speed >=61:
      return 1
    if speed >= 86:
      return 2

Q5.
def sorta_sum(a, b):
  sums = a+b
  if 19 >= sums >= 10:
    return 20
  else:
    return sums
    
Q6.
def alarm_clock(day, vacation):
  if not vacation:
    if 5 >= day >=1 :
      return '7:00'
    else:
      return '10:00'
  if vacation:
    if 5 >= day >=1:
      return '10:00'
    else:
      return 'off'

Q7.
def love6(a, b):
  sums = a + b
  diff = abs(a-b)
  if a == 6 or b == 6:
    return True
  if sums == 6 or diff == 6:
    return True
  else:
    return False
  
Q8.
def in1to10(n, outside_mode):
  if not outside_mode and 10 >= n >= 1:
    return True
  if outside_mode and (10 <= n or n <= 1):
    return True
  else:
    return False
    
Q9.
def near_ten(num):
  near = num%10 
  if near < 3 or near == 9 or near == 8:
    return True
  else:
    return False
