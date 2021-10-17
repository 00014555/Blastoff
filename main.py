import sys

# count down function
def countdown(n):
  if n <= 0:
    print('Blastoff!')
  else:
    print(n)
    countdown(n-1)

# count up function
def countup(n):
  if n >= 0:
    print('Blastoff!')
  else:
    print(n)
    countup(n+1)

# ask user to enter number
if sys.version_info[0] == 3:
  num = input('>>> count up  ')
else:
  num = input('>>> count up  ')

# convert string to number
num = int(num)


if num < 0:
  # count up negative number
  countup(num)
else:
  print('Blastoff!')
