import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
game = True
data = pandas.read_csv("50_states.csv")

trtl = turtle.Turtle()
trtl.penup()
trtl.hideturtle()
trtl.speed("fastest")
guesses = 0
guessed_states = []
while game:

    answer = screen.textinput(title=f"{guesses}/50 States Correct", prompt="Enter the name of a state: ").title()
    for state in data["state"]:
        if answer == state and answer not in guessed_states:
            guessed_states.append(answer)
            guesses += 1
            current_state = data[data["state"] == state]
            trtl.goto(int(current_state.x), int(current_state.y))
            trtl.write(answer)
    if guesses == 50:
        trtl.home()
        trtl.write("Congratulations! You won!")

screen.exitonclick()
