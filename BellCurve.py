import random
import plotly.express as pe
import plotly.figure_factory as pff
import pandas as pd

"""diceResult = []
count = []
for x in range(0,100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    diceResult.append(dice1 + dice2)
    count.append(x)

graph1 = pe.bar(x = diceResult, y = count)
#graph1.show()

graph2 = pff.create_distplot([diceResult], ["Random Result"], show_hist = False)
graph2.show()"""

data = pd.read_csv("data1.csv")
height = data["Height"]

heightBellCurve = pff.create_distplot([height], ["Heights of different students"], show_hist = False)
heightBellCurve.show()
