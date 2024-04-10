class Maze:
  '''
  Singleton - The maze\n
  _instance: The one maze\n
  _initialized: A bool for if the maze has been constructed or not\n
  _maze[][]: A 2D list containing the state of each maze tile
  __new__(cls): Checks if the maze has been constructed before\n
  __init__(self): Creates and stores a 2d list from the file\n
  __getitem__(row): overrides the [] operator for 1d and 2d. Returns the specified row or row and column\n
  __len__() returns the number of rows in the maze\n
  __str__() returns the maze as a grid in a string
  search_maze(ch): Returns the location of character ch as a list [row, column]
  '''
  _instance = None
  _initialized = False

  def __new__(cls, *args):
    '''override the __new__ method'''
    #return super().__new__(cls) used for testing
    if(cls._instance == None):
      #Create instance
      cls._instance = super().__new__(cls)

    #Got an instance
    return cls._instance

  def __init__(self):
    '''Fill in the maze grid'''
    #precon
    if(Maze._initialized == False):
      #Fill self.maze[][]
      self._maze = []
      file = open("minomaze.txt","r")
      lines = file.readlines()
      
      #grab each character
      for i in range(0,len(lines)):
        column = []
        read_this = lines[i].strip()
        for j in range(0,len(read_this)):
          column.append(read_this[j]) #char j of line i
        self._maze.append(column)

      Maze._initialized = True
        
          

  def __getitem__(self, row):
    '''Access the maze like a 2D list'''
    return self._maze[row] #A second [] will access the row list too

  def __len__(self):
    '''The length of a column'''
    return len(self._maze) #A second [] will return the length of a row

  def __str__(self):
    '''The string representation of a maze'''
    the_string = ""
    #For each row
    for i in range(0,len(self._maze)):
      #For each column
      for j in range(0,len(self._maze[i])):
        the_string += self._maze[i][j] + " " #Added a space
      #Column done  
      the_string += "\n"

    #done with everything
    return the_string

  def search_maze(self,ch):
    '''
    Return the location of character ch\n
    Use "H" or "M" for hero or minotaur, "f" for finish, "s" for start
    '''
    #For every row
    for i in range(0, len(self._maze)):
      #For every column
      for j in range(0, len(self._maze[i])):
        if(self._maze[i][j] == ch):
          return [i,j]
    #not found
    return [-1,-1] #should never happen
  