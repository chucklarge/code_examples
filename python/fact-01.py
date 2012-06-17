import sys

sys.setrecursionlimit(1500)

def some_func ():
  blah = 3
  dumb = 5
  return blah, dumb

def fact(n, total=1):
  if n <= 1:
	return total
  else:
	return fact(n-1, n * total)


def main ():
  blah, dumb = some_func()
  print "hello %s\nblah = %5d\ndumb = %5d" %("chuck", blah, dumb)

  print fact(14)


  print id("hello")

if __name__== "__main__":
  main()
