Q1.
def hello_name(name):
  return 'Hello'+' '+name+'!'

Q2.
def make_abba(a, b):
  return a+b+b+a

Q3.
def make_tags(tag, word):
  return '<'+tag+'>'+word+'</'+tag+'>'

Q4.
def make_out_word(out, word):
  return out[:2]+word+out[2:]

Q5.
def extra_end(str):
  return 3*str[-2:]

Q6.
def first_two(str):
  if len(str) < 2:
    return str
  return str[:2]

Q7.
def first_half(str):
  return str[:len(str)/2]

Q8.
def without_end(str):
  return str[1:-1]

Q9.
def combo_string(a, b):
  if len(a) < len(b):
    return a+b+a
  return b+a+b

Q10.
def non_start(a, b):
  return a[1:]+b[1:]

Q11.
def left2(str):
  return str[2:]+str[:2]

