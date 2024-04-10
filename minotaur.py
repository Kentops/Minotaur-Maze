import random

from maze import Maze


class Minotaur:
  '''The minotaur opponent'''
  
  def __init__(self):
    '''Initialize maze object and randomly place minotaur'''
    maze = Maze()
    

    placed = False #I changed this because it was n^2 runtime before
    while not placed: #Feel free to change it back
      r = random.randint(1, len(maze)-2) #-2 to avoid border
      c = random.randint(1,len(maze[0])-2)
      if(maze[r][c] == " "):
        placed = True
        maze[r][c] = "M"
    
    
  def move_minotaur(self) :
    '''Moves the minotaur toward the player. Returns what the minotaur landed on. 
    Must be able to touch player. Cannot touch * or f
    If it can't move toward the player, it will move toward f'''
    maze = Maze()
    loc = maze.search_maze("M")
    result = self._move(loc, "H")
    if(result == -1):
      result = self._move(loc, "f")
    return result
    
  #I asked about making these private methods
  def _move(self, loc, target):
    '''Moves the minotaur'''
    maze = Maze()
    target_loc = maze.search_maze(target)


    #Move minotaur and check if there is a wall
    if(target_loc[0] > loc[0] and self._check_tile(loc[0]+ 1, loc[1])):
      #Moves down
      old = maze[loc[0]+1][loc[1]]
      maze[loc[0]][loc[1]] = " "
      maze[loc[0]+1][loc[1]] = "M"
      return old

    elif(target_loc[0] < loc[0] and self._check_tile(loc[0]-1,loc[1])):
      #Moves up
      old = maze[loc[0] -1][loc[1]]
      maze[loc[0]][loc[1]] = " "
      maze[loc[0]-1][loc[1]] = "M"
      return old

    elif(target_loc[1] > loc[1] and self._check_tile(loc[0],loc[1]+1)):
      #Moves right
      old = maze[loc[0]][loc[1]+1]
      maze[loc[0]][loc[1]] = " "
      maze[loc[0]][loc[1]+1] = "M"
      return old

    elif(target_loc[1] < loc[1] and self._check_tile(loc[0],loc[1]-1)):
      #Moves left
      old = maze[loc[0]][loc[1]-1]
      maze[loc[0]][loc[1]] = " "
      maze[loc[0]][loc[1] - 1] = "M"
      return old
    else:
      #Cannot get closer to the target
      #This should not happen if the target is f
      return -1

  def _check_tile(self,x,y)->bool:
    '''Checks if the minotaur can move to maze[x][y]'''
    maze = Maze()
    return maze[x][y] != "*" and maze[x][y] != "f"
    

    '''if hero_loc[0] > minotaur_loc[0]:
      if self.maze[minotaur_loc[0] + 1][minotaur_loc[1]] == ' ':
        self.maze[minotaur_loc[0]][minotaur_loc[1]] = ' '
        self.maze[minotaur_loc[0] + 1][minotaur_loc[1]] = 'M'
    elif hero_loc[0] < minotaur_loc[0]:
      if self.maze[minotaur_loc[0] - 1][minotaur_loc[1]] == ' ':
          self.maze[minotaur_loc[0]][minotaur_loc[1]] = ' '
          self.maze[minotaur_loc[0] - 1][minotaur_loc[1]] = 'M'
    elif hero_loc[1] > minotaur_loc[1]:
      if self.maze[minotaur_loc[0]][minotaur_loc[1] + 1] == ' ':
          self.maze[minotaur_loc[0]][minotaur_loc[1]] = ' '
          self.maze[minotaur_loc[0]][minotaur_loc[1] + 1] = 'M'
    elif hero_loc[1] < minotaur_loc[1]:
      if self.maze[minotaur_loc[0]][minotaur_loc[1] - 1] == ' ':
          self.maze[minotaur_loc[0]][minotaur_loc[1]] = ' '
          self.maze[minotaur_loc[0]][minotaur_loc[1] - 1] = 'M'
    else:
      return Maze()
      '''
    '''if(hero_loc[0] > minotaur_loc[0]):
      if self.maze[minotaur_loc[0] + 1][minotaur_loc[1]] == ' ':
        self.maze[minotaur_loc[0]][minotaur_loc[1]] = " "
        self.maze[minotaur_loc[0]+1][minotaur_loc[1]] = "M"
      elif self.maze[minotaur_loc[0] + 1][minotaur_loc[1]] == '*':
        self.maze[minotaur_loc[0]][minotaur_loc[1]] = " "
        self.maze[minotaur_loc[0]][minotaur_loc[1] -1] = "M"
    elif(hero_loc[0] < minotaur_loc[0]):
      self.maze[minotaur_loc[0]][minotaur_loc[1]] = " "
      self.maze[minotaur_loc[0]-1][minotaur_loc[1]] = "M"
    elif(hero_loc[1] > minotaur_loc[1]):
      self.maze[minotaur_loc[0]][minotaur_loc[1]] = " "
      self.maze[minotaur_loc[0]][minotaur_loc[1]+1] = "M"
    elif(hero_loc[1] < minotaur_loc[1]):
      self.maze[minotaur_loc[0]][minotaur_loc[1]] = " "
      self.maze[minotaur_loc[0]][minotaur_loc[1] - 1] = "M"'''
