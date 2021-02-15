import random
import sys
def general():

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = 17
  rnd1 = random.randint(0, last)
  rnd2 = random.randint(0, last)

  sys.stdout.write(quotes[rnd1]),
  sys.stdout.write(quotes[rnd2])

if __name__== "__main__":
  general()
