import turtle as t
import pandas


# Getting the states data
state_data = pandas.read_csv('50_states.csv')


# Setting the screen
screen = t.Screen()
screen.bgpic('blank_states_img.gif')
game_run = True
guessed_states = []


def print_state_name(state, x, y):
    name = t.Turtle()
    name.penup()
    name.hideturtle()
    name.goto(int(x), int(y))
    name.write(f'{state}')


# Game loop
while game_run:
    state_name = str(screen.textinput("Input Name", "Enter name of a US state")).title()
    state_list = state_data.state.to_list()
    if state_name == 'Exit':
        break
    if state_name in state_list:
        guessed_states.append(state_name)
        state_x = state_data[state_data.state == state_name].x
        state_y = state_data[state_data.state == state_name].y
        print_state_name(state_name, state_x, state_y)

not_guessed_names = [name for name in state_list if name not in guessed_states]
# not_guessed_data = state_data[~state_data.state.isin(guessed_states)]
not_guessed_data = pandas.DataFrame(not_guessed_names)
not_guessed_data.to_csv('not_guessed.csv')
screen.exitonclick()
