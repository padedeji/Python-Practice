# Calculate the total cost of tile it would take to cover a floor plan of width and height, using a cost entered by the user.

def tile_cost():
    cost_of_tile = float(input("What is the cost of one tile? "))
    width = float(input("What is the width of the floor plan? "))
    height = float(input("What is the height of the floor plan? "))
    full_cost = cost_of_tile * width * height
    return "The cost to tile a %.2f x %.2f floor is: $%.2f " % (width, height, width * height * cost_of_tile)


print(tile_cost())
