directions = input("You are on an island next to the beach, which way are you going? left or right?").lower()
if directions == "left":
  actions = input("After adventuring on the island you arrive infront of a lake. Do you wait for the boat or you swim?").lower()
  if actions == "wait":
    doors = input("A guide takes you to a labyrinth and leaves you in front of 3 doors. Red, Yellow and blue. Which one do you choose?").lower()
    if doors == "red":
      print("Burned by fire. Game Over")
    elif doors == "yellow":
      print("You win!")
    elif doors == "blue":
      print("Eaten by beast. Game Over.")
    else:
      print("Game Over.")
  else:
    print("Attacked by trout. Game Over")
else:
  print("Fall into a hole. Game Over.")
