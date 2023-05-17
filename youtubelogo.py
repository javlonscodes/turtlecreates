# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from turtle import *
hideturtle()



fillcolor("red")

begin_fill()
for i in [300, 200]*2:
    forward(i)
    circle(30, 90)



end_fill()
penup()
goto(120, 65)
pendown()

fillcolor("white")

begin_fill()
for i in [30, 120, 120]:
      left(i)
      forward(100)

end_fill()
done()



