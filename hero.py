from maze import Maze

class Hero:
  '''The player'''
  def __init__(self):
    maze = Maze()
    start_position = maze.search_maze("s")
    maze[start_position[0]][start_position[1]]='H'

  def go_up(self):
    '''Moves the player and returns what the player ran into'''
    maze = Maze() #define this each time
    loc = maze.search_maze("H")
    new_location = maze[loc[0] - 1][loc[1]]
    #* border, so no need to check if index is out of bounds
    if new_location == ' ':
      #Update player position and remove old H
      maze[loc[0] - 1][loc[1]] = 'H'
      maze[loc[0]][loc[1]] = " "
    return(new_location)
      

  def go_down(self):
    '''Moves the player and returns what the player ran into'''
    maze = Maze()
    loc = maze.search_maze("H")
    new_location = maze[loc[0] + 1][loc[1]]
    if new_location == " ":
      maze[loc[0] +1][loc[1]] = "H"
      maze[loc[0]][loc[1]] = " "
    return new_location

  def go_left(self):
    '''Moves the player and returns what the player ran into'''
    maze = Maze()
    loc = maze.search_maze("H")
    new_location = maze[loc[0]][loc[1] -1]
    if new_location == " ":
      maze[loc[0]][loc[1] -1] = "H"
      maze[loc[0]][loc[1]] = " "
    return new_location

  def go_right(self):
    '''Moves the player and returns what the player ran into'''
    maze = Maze()
    loc = maze.search_maze("H")
    new_location = maze[loc[0]][loc[1] + 1]
    if(new_location == " "):
      maze[loc[0]][loc[1] + 1] = "H"
      maze[loc[0]][loc[1]] = " "
    return new_location


''' def go_down(self):
    new_pos = self.row + 1
    if new_pos < len(self.maze) and self.maze[new_pos][self.col] != '*':
      self.maze[self.row][self.col]=''
      self.row = new_pos
      self.maze[self.row][self.col] = 'H'''