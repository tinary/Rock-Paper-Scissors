import math;
import random;

# get moves for computer for rock-paper-scissors game
def rps_get_move(move_type):
  if (move_type == "random"):
    x = random.randint(1,3)
    if x==1:
      return "rock"
    elif x==2:
      return "paper"
    else:
      return "scissors"
  else:
    return move_type

# the golden ratio
phi = (1.0 + math.sqrt(5.0))/2.0

# compute the n-th Fibonacci number
def fib(n):
  if n<=0:
    return 0
  elif n==1:
    return 1
  else:
    i = 1          # index for looping
    a,b = 1,0      # current consecutive fib numbers
    while (i < n):
      i = i + 1
      a,b = a+b, a
    return a
  