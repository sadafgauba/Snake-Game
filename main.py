from snake import Snake
from food import Food
from scoreboard import Scoreboard

snake = Snake()
food = Food()
scoreboard = Scoreboard()
scoreboard.display_score()
first_time_food = True

while True:
    snake.direction_update()
    snake_head, space_after_tail = snake.move()
    if snake.detect_collision():
        break
    if first_time_food:
        food_pos = food.show_food()
        first_time_food = False

    if snake.head.distance(food) < 15:
        scoreboard.update_score()
        scoreboard.display_score()
        food_pos = food.show_food()
        snake.add_part(space_after_tail)

scoreboard.display_gameover()
snake.click_exit()
