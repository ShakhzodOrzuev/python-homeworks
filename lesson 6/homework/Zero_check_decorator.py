def check(func):
   def wrap(arg, k):
      try:
         func(arg, k)
      except ZeroDivisionError:
         print('Cannot be divided')
   return wrap
a = int(input('enter divisible: '))
b = int(input('enter divisor: '))
@check
def div(a, b):
   print(a/b)
div(a,b)