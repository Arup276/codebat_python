Q1.
def sleep_in(weekday, vacation):
#if it is not weekday mean weekday = False 
  if not weekday or vacation:
    return True
  else:
    return False

Q2.
def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile or not a_smile and not b_smile:
      return True
    else:
      return False

Q3.
def sum_double(a, b):
#if a == b the return double of the sum.
  if a == b:
    return 2*(a+b)
  else:
    return a+b
    
Q4.
def diff21(n):
  if n > 21:
    return 2*(abs(n-21))
#asb() return the absolute value.  
  else:
    return 21 - n
    
Q5.
def parrot_trouble(talking, hour):
# if taking and the hour is less than 7 and greater than 20 then return True.  
  if talking and  (hour < 7 or hour > 20) :
    return True
  else:
    return False

Q6.
def makes10(a, b):
# sum() take a list of numbers and add them. 
  if sum([a,b]) == 10 or a == 10 or b == 10:
    return True
  else:
    return False
    
 Q7.
def near_hundred(n):
  if (abs(n-100) <= 10)  or (abs(n-200) <= 10) :
    return True
  else:
    return False
  
  Q8.
  def pos_neg(a, b, negative):
  if (a > 0 and b < 0) or (a < 0 and b > 0) and (not negative):
    return True
  elif a < 0 and b < 0 and negative:
    return True
  else:
    return False
  
  Q9.
  def not_string(str):
  if str[:3] == 'not':
    return str
  else:
    return 'not '+str
  
  Q10.
  # better way of solving this problem given in Solution.
  def missing_char(str, n):
  lst = list(str)
  lst.pop(n)
  
  
  return ''.join(lst)
