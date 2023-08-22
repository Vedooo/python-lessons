import turtle
import pandas as pd
import numpy as np

s = turtle.Screen()

IMAGE = "blank_states_img.gif"
s.title("U.S. State Game")
s.addshape(IMAGE)
turtle.shape(IMAGE)

df = pd.read_csv("50_states.csv")
all_cities = df.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = s.textinput(title='Guess the state', 
                               prompt='What is other states name?').title()

    if answer_state in all_cities:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = df[df.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
    
    if answer_state == "exit":
        missed_states = [state for state in all_cities if state not in guessed_states]
        df2 = pd.DataFrame(missed_states)
        df2.to_csv("missing_cities.csv")
        break
    
    if len(guessed_states) == 50:
        break