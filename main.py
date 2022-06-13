import turtle
import pandas

screen = turtle.Screen()
screen.title("US game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_name = data.state.to_list()

is_on = True
score = 0

while is_on:

    answer_state = screen.textinput(title=f"Guess the state{score}/50", prompt="What is your answer?: ").title()

    if answer_state in state_name:
        print("True")
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
turtle.mainloop()