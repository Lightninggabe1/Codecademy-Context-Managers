#A Familiar Face: The with Statement
try:
  open_file = open('file_name.txt', 'r')
  print(open_file.read())
finally:
  open_file.close()

with open('file_name.txt','r') as open_file:
  print(open_file.read())

#Class Based Context Managers
# Write your code below: 
class PoemFiles:
  def __init__(self):
    print('Creating Poems!')
  def __enter__(self):
    print('Opening poem file')
  def __exit__(self,*exc):
    print('Closing poem file')

with PoemFiles() as manager:
  print('Hope is the thing with feathers')
