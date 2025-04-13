def solution_part1(input):
    with open(input) as file:
        rows = file.readlines()
        map = []
        for line in rows: 
            map.append(list(line.strip()))
    
    XMAS = 0
    directions = [
        (1, 0), (-1, 0),  # vertical (down, up)
        (0, 1), (0, -1),  # horizontal (right, left)
        (1, 1), (-1, -1), # diagonal (down-right, up-left)
        (1, -1), (-1, 1)  # diagonal (down-left, up-right)
    ]
    
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 'X':
                for direction in directions:
                    try:
                        if (map[i + direction[0]][j + direction[1]] == 'M' and
                            map[i + 2 * direction[0]][j + 2 * direction[1]] == 'A' and
                            map[i + 3 * direction[0]][j + 3 * direction[1]] == 'S'):
                            XMAS += 1
                    except IndexError:
                        pass
    
    return XMAS      

            

print(solution_part1('inputs/2024-4.txt'))lf;sdf;lsd;lfs;d