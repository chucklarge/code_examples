
i = 0.0

step = .01
while True:
  print i
  i += step
  if (i > 10.0): i = 10.0; step = -0.01
  if (i < 0.0):  i = 0.0; step = .01


