file = open('example.txt', 'r',  encoding='utf-8')
lines = file.readlines()

for line in lines:
  print(line, end='')
  file.close()
  