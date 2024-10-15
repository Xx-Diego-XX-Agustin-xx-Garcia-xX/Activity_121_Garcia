#import statements
import leaderboard as lead
import turtle as turt
import random as rand

#game configuration
counter_interval = 1000
dart_color = "red"
dart_size = 2
dart_shape = "classic"
font_setup = ("Arial", 20, "normal")
timer = 5
timer_up = False
score = 0

#initialize turtles
leaderboard_file_name = "a122_leaderboard.txt"
player_name = input ("Please enter your name:")
dart = turt.Turtle()
dart.shape(dart_shape)
dart.shapesize(dart_size)
dart.fillcolor(dart_color)
writer = turt.Turtle()
counter = turt.Turtle()

#game functions
def change_position():
  new_xpos = rand.randint(-200, 200)
  new_ypos = rand.randint(-150, 150)
  dart.goto(new_xpos, new_ypos)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font = font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font = font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

def dart_clicked(x, y):
  change_position()
  writer.clear()
  global timer_up
  if timer_up == False:
    update_score()
  else:
    dart.hide()

def update_score():
  global score
  score += 1
  writer.write(score, font = font_setup)

def manage_leaderboard():
  global score
  global dart
  leader_names_list = lead.get_names(leaderboard_file_name)
  leader_scores_list = lead.get_scores(leaderboard_file_name)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lead.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lead.draw_leaderboard(True, leader_names_list, leader_scores_list, spot, score)

  else:
    lead.draw_leaderboard(False, leader_names_list, leader_scores_list, spot, score)

#events
dart.onclick(dart_clicked)
wn = turt.Screen()
counter.getscreen().ontimer(countdown, counter_interval)
wn.mainloop()
