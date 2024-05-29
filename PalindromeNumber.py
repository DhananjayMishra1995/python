#Given an integer x, return true if x is a palindrome, and false otherwise.
#An integer is a palindrome when it reads the same forward and backward.

#For example, 121 is a palindrome while 123 is not.

def isPalindrome(self, x: int) -> bool:
  if x<0:
      return False
  
  new_x = str(x)
  str_value = ''
  for i in range(len(new_x)-1,-1,-1):

      repeated_val =new_x[i]
      repeated_val = str(repeated_val)
      str_value = str_value+repeated_val

  int_val = int(str_value)
  if x==int_val:
      return True
  else:
      return False
