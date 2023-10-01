import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
Fur_colour = data["Primary Fur Color"].tolist()
grey = 0
cinnamon = 0
black = 0
n = len(Fur_colour)

for i in range(n):
    if Fur_colour[i] == "Gray":
        grey += 1
    elif Fur_colour[i] == "Cinnamon":
        cinnamon += 1
    elif Fur_colour[i] == "Black":
        black += 1

# Create a new DataFrame for the color counts
color_counts = pd.DataFrame({
    "Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey, cinnamon, black]
})

# Write the color counts to a new CSV file
color_counts.to_csv("newdata.csv", index=False)

print(color_counts)
