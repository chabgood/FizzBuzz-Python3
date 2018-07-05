for i in range(1, 100):
  x = ''
  if i%3 == 0:
      x += 'Fizz'
  if i%5 == 0:
    x += 'Buzz'
  print(i if not x else x)
