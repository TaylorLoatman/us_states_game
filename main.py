import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
game_data = []
game_on = True
correct_guess = 0

while len(game_data) < 50:

    answer_pop = turtle.Turtle()
    answer_pop.hideturtle()
    answer_state = screen.textinput(title=f"{correct_guess}/50 Guess The States",
                                    prompt="What's another state's name?").title()
    state = data[data.state == answer_state]

    if answer_state == "Exit":
        data_dict = {
            "states": states_list
        }
        df = pandas.DataFrame(data_dict)
        df.to_csv("states_to_learn.csv")
        break
    elif answer_state not in states_list:
        answer_pop.penup()
        answer_pop.home()
    else:
        correct_guess += 1
        game_data.append(answer_state)
        answer_pop.penup()
        answer_pop.goto(int(state.x), int(state.y))
        answer_pop.pendown()
        answer_pop.write(answer_state)
        states_list.remove(answer_state)

# states_to_learn.csv








