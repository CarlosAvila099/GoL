from conway import randomGrid

def make_config(width, height, generations, file_number):
    text = f"{width} {height}\n"
    text += f"{generations}\n"
    grid = randomGrid(width, height)
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x, y] == 255: text += f"{x} {y}\n"
    text = text[:-1]

    output = open(f"Config{file_number}.txt", "w")
    output.write(text)
    output.close()
    
config_files = int(input("Number of config files to create (default 5): ") or 5)
for num in range(config_files):
    print(f"\nParameters for configuration {num+1}:")
    width = int(input("Width of universe (default 100): ") or 100 ) 
    height = int(input("Height of universe (default 100): ") or 100) 
    generations = int(input("Number of generations (default 200): ") or 200)
    make_config(width, height, generations, num+1)