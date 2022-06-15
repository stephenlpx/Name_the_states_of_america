import turtle
import pandas

screen = turtle.Screen()
screen.title("US game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_name = data.state.to_list()

guessed_states = []

score = 0

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"Guess the state{score}/50", prompt="What is your answer?: ").title()
    # creates a list of all the states that the user failed to enter
    if answer_state == "Exit":
        #use list comprehension to shorten the code
        states_to_learn = [state for state in state_name if state not in guessed_states]
        df = pandas.DataFrame(states_to_learn)
        df.to_csv("states_to_learn.csv")
        break

    if answer_state in state_name and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        #getting the row of data from the state name
        state_data = data[data.state == answer_state]
        t.goto(int(state_data["x"]), int(state_data["y"]))
        t.write(answer_state)
        score += 1

        if score == 50:
            is_on = False

screen.exitonclick()
