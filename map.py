colors = ['Orange','Yellow','Green']

states = ['Western_Australia', 'Northern_Territory', 'Southern_Australia', 'Queensland', 'New_South_Wales', 'Victoria','Tasmania']
#the states of Australia are stored in a list called states. We can also store it as an adjacency matrix for bigger maps
neighbors = {} #dict to store the neighbours
neighbors['Western_Australia'] = ['Northern_Territory', 'Southern_Australia']
neighbors['Northern_Territory'] = ['Western_Australia', 'Southern_Australia', 'Queensland']
neighbors['Southern_Australia'] = ['Western_Australia', 'Northern_Territory', 'Queensland', 'New_South_Wales', 'Victoria']
neighbors['Queensland'] = ['Northern_Territory', 'Southern_Australia', 'New_South_Wales']
neighbors['New_South_Wales'] = ['Queensland', 'Southern_Australia', 'Victoria']
neighbors['Victoria'] = ['Southern_Australia', 'New_South_Wales']
neighbors['Tasmania'] = []      #Tasmania doesn't have any neighbour and is not attached to any other node in the graph

colors_of_states = {}    #dict 
def find(state, color):
    for neighbor in neighbors.get(state):                     #iterates over the neighbours and checks that no adjacent area has same color
        color_of_neighbor = colors_of_states.get(neighbor)
        if color_of_neighbor == color:
            return False
    return True

def find_color_for_state(state): #after find returns True then we return that color to the main function meaning that the adjacent area doen't have that color. For Southern_Australia it will check with all its adjacent area and then only assign the color to it
    for color in colors:
        if find(state, color):
            return color
    return None

def main():
    for state in states:
        color = find_color_for_state(state)
        if color is None:
            print("No solution exists.")       #for times when the constraints don't get satisfied and the map coloring for that graph is not possible
            return
        colors_of_states[state] = color
    for state, color in colors_of_states.items():
        print(f"{state}: {color}")
    
if __name__ == '__main__':
    main()
