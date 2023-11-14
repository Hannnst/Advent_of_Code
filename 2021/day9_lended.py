from functools import reduce

UP = 'UP'
DOWN = 'DOWN'
LEFT = 'LEFT'
RIGHT = 'RIGHT'

def part_one(input):
    def find_neighbor_values(point, grid):
        directions = [
            (point[0], point[1]-1) if point[1]-1 >= 0 else None, # up
            (point[0], point[1]+1) if point[1]+1 < len(grid) else None, # down
            (point[0]-1, point[1]) if point[0]-1 >= 0 else None, # left
            (point[0]+1, point[1]) if point[0]+1 < len(grid[point[1]]) else None, # right
        ]

        for direction in directions:
            if direction: yield grid[direction[1]][direction[0]]

    grid = [[char.rstrip() for char in line.strip()] for line in input]
    low_points = []
    for y, y_line in enumerate(grid):
        for x, value in enumerate(y_line):
            is_lowpoint = True
            for n_val in find_neighbor_values((x,y), grid):
                if n_val <= value: is_lowpoint = False
            if is_lowpoint: low_points.append(value)
    return sum([int(v)+1 for v in low_points])

def part_two(input):
    def find_neighbor_values(point, grid, ignore_directions=[]):
        directions = find_neighbor_points(point, grid, ignore_directions)
        for direction in directions:
            if direction: yield grid[direction[1]][direction[0]]

    def find_neighbor_points(point, grid, ignore_directions=[]):
        directions = [
            (point[0], point[1]-1) if ((point[1]-1 >= 0) and UP not in ignore_directions) else None, # up
            (point[0], point[1]+1) if ((point[1]+1 < len(grid)) and DOWN not in ignore_directions) else None, # down
            (point[0]-1, point[1]) if ((point[0]-1 >= 0) and LEFT not in ignore_directions) else None, # left
            (point[0]+1, point[1]) if ((point[0]+1 < len(grid[point[1]])) and RIGHT not in ignore_directions) else None, # right
        ]
        return directions

    def is_basin(point, grid, ignore_directions=[]):
        is_lowpoint = True
        for n_val in find_neighbor_values(point, grid, ignore_directions):
            if n_val < grid[point[1]][point[0]]: return False
        return is_lowpoint

    def get_basin_size(point, grid):
        basin_points = set() # These are parts of basins (but not necessarily basins themselves)
        ignorable_directions = {}
        def scan(point, grid, ignore_directions=[]):
            if point not in ignorable_directions: ignorable_directions[point] = ignore_directions
            else: ignorable_directions[point] = ignorable_directions[point] + ignore_directions
            ignore_directions = ignorable_directions[point]
            if not point: return False
            if is_basin(point, grid, ignore_directions):
                up_point, down_point, left_point, right_point = find_neighbor_points(point, grid, ignore_directions)
                basin_points.update([point, up_point, down_point, left_point, right_point])
                scan(up_point, grid, [DOWN])
                scan(down_point, grid, [UP])
                scan(left_point, grid, [RIGHT])
                scan(right_point, grid, [LEFT])
        scan(point, grid)

        basin_size = 0
        for point in basin_points:
            if point and grid[point[1]][point[0]] != 9:
                basin_size += 1
        return basin_size

    grid = [[int(char.rstrip()) for char in line.strip()] for line in input]

    sizes = []
    for y, y_line in enumerate(grid):   
        for x, _ in enumerate(y_line):
            sizes.append(get_basin_size((x, y), grid))
    sizes.sort(reverse=True)
    return reduce((lambda x, y: x * y), sizes[:3])
    
if __name__ == '__main__':
    with open('Files/day9.txt', 'r') as input:
        print(f'Part 1: {part_one(input)} is the solution')

    with open('Files/day9.txt', 'r') as input:
        print(f'Part 2: {part_two(input)} is the solution')