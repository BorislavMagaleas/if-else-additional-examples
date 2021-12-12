figure = input("What figure to draw? ")

if figure == "line":
    print("-" * 5)
elif figure == "square":
    print("-" * 5)
    for i in range(2):
      print("|   |") 
    print("-" * 5)
elif figure == "parallel horizontal lines":
    for i in range(2):
        print("-" * 5)
elif figure == "parallel vertical lines":
    for i in range(2):
        print("|   |")
else:
    print("CAN'T DRAW SUCH FIGURE!")
