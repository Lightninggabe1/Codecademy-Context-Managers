#Introduction to Resource Management
#1/10 in Context Managers
with open("file_name.txt", "w") as file:
   file.write("How you gonna win when you ain't right within?")
#A Familiar Face: The with Statement
#2/10 in Context Managers
try:
  open_file = open('file_name.txt', 'r')
  print(open_file.read())
finally:
  open_file.close()

with open('file_name.txt','r') as open_file:
  print(open_file.read())

#Class Based Context Managers
#3/10 in Context Managers
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

#Class Based Context Managers II:
#3/10 in Context Managers
# Write your code below:
class PoemFiles:
  def __init__(self, poem_file, mode):
    print('Starting up a poem context manager')
    self.file = poem_file
    self.mode = mode

  def __enter__(self):
    print('Opening poem file')
    self.opened_poem_file = open(self.file, self.mode)
    return self.opened_poem_file

  def __exit__(self, *exc):
    print('Closing poem file')
    self.opened_poem_file.close()

with PoemFiles('poem.txt', 'w') as open_poem_file:
  open_poem_file.write('Hope is the thing with feathers')

#Handling Exceptions I
#4/10 in Context Managers
class PoemFiles:

  def __init__(self, poem_file, mode):
    print(' \n -- Starting up a poem context manager -- \n ')
    self.file = poem_file
    self.mode = mode

  def __enter__(self):
    print('Opening poem file')
    self.opened_poem_file = open(self.file, self.mode)
    return self.opened_poem_file

  # Create your __exit__ method here:
  def __exit__(self,exc_type,exc_value,traceback):
    print(exc_type)
    print(exc_value)
    print(traceback)
    self.opened_poem_file.close()
# First
# with PoemFiles('poem.txt', 'r') as file:
  # print("---- Exception data below ----")
  # print(file.uppercasewords())

# Second
with PoemFiles('poem.txt', 'r') as file2:
  print(file2.read()) 
  print("---- Exception data below ----")

#Handling Exceptions II
#5/10 in Context Managers
class PoemFiles:

  def __init__(self, poem_file, mode):
    print(' \n -- Starting up a poem context manager -- \n')
    self.file = poem_file
    self.mode = mode

  def __enter__(self):
    print(' \n --  Opening poem file -- \n')
    self.opened_poem_file = open(self.file, self.mode)
    return self.opened_poem_file

  def __exit__(self, exc_type, exc_value, traceback):
    print(exc_type, exc_value, traceback, '\n')
    # Write your code below: 
    self.opened_poem_file.close()
    if isinstance(exc_value,AttributeError):
      return True

with PoemFiles('poem.txt', 'r') as file:
  print("---- Exception data below ---- \n ")
  print(file.uppercasewords())

with PoemFiles('poem.txt', 'r') as file2:
  print(file2.read())
  print(" \n ---- Exception data below ---- \n ")
#Introduction to Contextlib
#6/10 in Context Managers
# Write your code below:
from contextlib import contextmanager

@contextmanager
def poem_files(file,mode):
  print('Opening File')
  open_poem_file = open(file,mode)
  try:
    yield open_poem_file
  finally:
    print("Closing File")
    open_poem_file.close()
with poem_files('poem.txt', 'a') as opened_file:
  print('Inside yield')
  opened_file.write('Rose is beautiful, Just like you.')



#Contextlib Error Handling
#7/10 in Context Managers
from contextlib import contextmanager
 
@contextmanager
def poem_files(file, mode):
  print('Opening File')
  open_poem_file = open(file, mode)
  try:
    yield open_poem_file
  #Write your code below: 
  except AttributeError as e:
    print(e)
  finally:
    print('Closing File')
    open_poem_file.close()

with poem_files('poem.txt', 'a') as opened_file:
  print('Inside yield')
  opened_file.sign('Buzz is big city. big city is buzz.')



#Nested Context Managers
#9/10 in Context Managers
from contextlib import contextmanager
 
@contextmanager
def poem_files(file, mode):
  print('Opening File',file)
  open_poem_file = open(file, mode)
  try:
    yield open_poem_file
  finally:
    print('Closing File')
    open_poem_file.close()


@contextmanager
def card_files(file, mode):
  print('Opening File',file)
  open_card_file = open(file, mode)
  try:
    yield open_card_file
  finally:
    print('Closing File',file)
    open_card_file.close()

# Write your code below: 
with poem_files('poem.txt','r') as poem:
  with card_files('card.txt','w') as card:
    print(poem,card)
    card.write(poem.read())
