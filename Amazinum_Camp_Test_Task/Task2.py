import random
import matplotlib.pyplot as plt

def count_neighbors(grid, i, j):
    # Count the number of alive neighbors for a given cell at (i, j) in the grid.
    count = 0
    # Check the relative positions adjacent to the current element
    neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    for dx, dy in neighbors:
        x, y = i + dx, j + dy
        # Check if the neighbor's coordinates are within the grid
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
            count += grid[x][y]
    return count

def apply_rules(grid):
    # Apply the transformation rules to a given grid and return a new grid
    new_grid = [row.copy() for row in grid]  # Copy the existing grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            neighbors_count = count_neighbors(grid, i, j)
            if grid[i][j] == 1:  # The cell is alive
                if neighbors_count < 2 or neighbors_count > 3:
                    new_grid[i][j] = 0  # The cell dies
            else:  # The cell is dead
                if neighbors_count == 3:
                    new_grid[i][j] = 1  # The cell becomes alive
    return new_grid

def print_grid(grid):
    # Print the given grid
    for row in grid:
        print(row)

def random_grid(rows, columns):
    # Create a random grid
    new_grid = []
    for i in range(rows):
        new_grid.append([])  # Add new rows
        for j in range(columns):
            new_grid[i].append(random.randint(0,1))  # Add 1 or 0 to the grid
    return new_grid

def custom_grid(rows, columns):
    # Create a custom grid
    new_grid = []
    for i in range(rows):
        new_grid.append([])  # Add new rows
        for j in range(columns):
            while True:
                # Check user input
                element = int(input(f'Enter the [{i}][{j}] element (must be 1 or 0): '))
                if element == 1 or element == 0:
                    new_grid[i].append(element)  # Add new element
                    break
                else:
                    print("Incorrect input!")
    return new_grid

def initial_simulation(grid):
    # Complete the initial transformation
    print("Initial grid: ")
    print_grid(grid)
    for i in range(8):  # Iterate 7 times
        new_grid = apply_rules(grid)
        if i == 7:
            print("7th iteration of the initial grid is: ")
            print_grid(new_grid)  # Print the 7th iteration

def plot_grid(grid):
    # Visualize the grid transformation
    plt.imshow(grid, cmap="gray")
    plt.axis('off')
    plt.show(block=False)
    plt.pause(0.5)
    plt.clf()

def endless_simulation(grid):
    # Simulate grid transformations
    while True:  # Infinite loop
        print("Current grid:")
        print_grid(grid)  # Print and visualize grid
        plot_grid(grid)
        grid = apply_rules(grid)
        print("Next grid:")
        print_grid(grid)
        plot_grid(grid)
        # Ask for user input
        ans = input("Continue simulations? Press 1 to continue, press 0 to stop \n")
        if ans == '0':
            print("Simulation stopped.")
            break  # Stop the simulation
        elif ans != '1':
            print("Invalid input, press 1 or 0")
# Ask user for task choice
choice = input("""What would you like to do?
- Press 1 for the initial task
- Press 2 for a random grid
- Press 3 for a custom grid
Your choice: """)
if choice == '1':
    # Initial task
    initial_grid = [
        [1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 1],
        [1, 0, 0, 1, 0, 0, 1],
        [0, 1, 1, 0, 1, 1, 0],
        [1, 1, 1, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 0, 1]
    ]
    initial_simulation(initial_grid)
elif choice == '2':
    # Random grid
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    test_grid = random_grid(rows, columns)
    endless_simulation(test_grid)
elif choice == '3':
    # Custom grid
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    user_grid = custom_grid(rows, columns)
    endless_simulation(user_grid)
else:
    print("Invalid choice")