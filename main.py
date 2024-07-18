#A Familiar Face: The with Statement
try:
  open_file = open('file_name.txt', 'r')
  print(open_file.read())
finally:
  open_file.close()

with open('file_name.txt','r') as open_file:
  print(open_file.read())
