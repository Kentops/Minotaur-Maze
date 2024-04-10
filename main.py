from maze import Maze
from hero import Hero
from minotaur import Minotaur


def main():
  print("Welcome hero, can you survive the Minotaur's Maze?")
  labyrinth = Maze()
  the_hero = Hero()
  dinosaur = Minotaur() #The proctor kept calling it a dinosaur

  #game loop
  game_done = False
  while not game_done:
    print(labyrinth)
    dir = input("Chose a direction (WASD): ")
    dir = dir.upper()
    result = ""
    if dir == "W":
      result = the_hero.go_up()
    elif dir == "A":
      result = the_hero.go_left()
    elif dir == "S":
      result = the_hero.go_down()
    elif dir == "D":
      result = the_hero.go_right()
    else:
      print("Invalid input")
      continue
    #inputs done
    #Check movement results
    if(result == "*"):
      print("You ran into a wall!")
    elif(result == "M"):
      print("You ran into the minotaur!")
      print("Game Over!")
      game_done = True
      continue #Make sure the minotaur doesn't move again
    elif(result == "f"):
      print("You escaped the maze!")
      print("You win!")
      game_done = True
      continue
    #minotaur
    if dinosaur.move_minotaur() == "H":
      print("The minotaur got to you!")
      print("Game Over!")
      game_done = True
    
    
    
    
    

main()