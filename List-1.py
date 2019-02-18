# Their are many different way or code to solve this problems.

Q1.
def first_last6(nums):
  if nums[0] == 6 or nums[len(nums)-1] == 6:
    return True
  return False

Q2.
def same_first_last(nums):
  if len(nums) >= 1 and nums[0] == nums[len(nums)- 1]:
    return True
  return False

Q3.
def make_pi():
  return [3,1,4]

Q4.
def common_end(a, b):
  if a[0] == b[0] or a[len(a)-1] == b[len(b)-1]:
    return True
  return False

Q5.
def sum3(nums):
  sums = 0
  for i in nums:
    sums += i
  return sums

Q6.
def rotate_left3(nums):
  return [nums[1],nums[2],nums[0]]

Q7.
def reverse3(nums):
  nums.reverse()
  return nums

Q8.
def max_end3(nums):
  st = nums[0]
  ls = nums[len(nums)-1]
  if st > ls:
    return [st,st,st]
  if ls > st:
    return [ls,ls,ls]
  if ls is st:
    return [ls,st,ls]

  Q9.
  def sum2(nums):
  if len(nums) == 0:
    return 0
  else:
    r = nums[:2]
    return sum(r)
  
  Q10.
  def middle_way(a, b):
  return [a[1],b[1]]

Q11.
def make_ends(nums):
  return [nums[0],nums[len(nums)-1]] # if their is one one element then len(nums) = 1 ,so 1-1 = 0 it will retrun oth element

Q12.
# 1.
def has23(nums):
  for i in nums:
    if i == 2 or i == 3:
      return True
  return False
# 2.
def has23(nums):
  nd = nums.count(2)
  rd = nums.count(3)
  if nd or rd:
    return True
  return False
