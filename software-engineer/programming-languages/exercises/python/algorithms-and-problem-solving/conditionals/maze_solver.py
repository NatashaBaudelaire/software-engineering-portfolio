def solve_maze():
    import sys
    from collections import deque

    input = sys.stdin.read
    data = input().splitlines()
    
    n = int(data[0])
    start_y = int(data[1])
    start_x = int(data[2])
    
    maze = [list(line) for line in data[3:3+n]]
    
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir_names = [
        "RIGHTOOOO THIS SAKE IS SUUUUUUUUPEEEEEEER", 
        "YUMMM THE MEAT IS REALLY GOOD",
        "NAAAAMIII SWAAAAAAAAAAN ROBIIIIIN CHAAAAAAN the dessert is ready!",
        "YOHOHOHOHOHOHOHOHOHO"
    ]
    
    x, y = start_x, start_y
    
    if maze[y][x] == 'S':
        for row in maze:
            print(''.join(row))
        print("It was way too easy to get here, hand over the sake already, you lousy cook!")
        return
    
    maze[y][x] = 'Z'
    
    queue = deque([(x, y)])
    found_sake = False
    
    while queue and not found_sake:
        current_x, current_y = queue.popleft()
        
        for i, (dx, dy) in enumerate(directions):
            new_x, new_y = current_x + dx, current_y + dy
            
            if 0 <= new_x < n and 0 <= new_y < n:
                
                if maze[new_y][new_x] == 'S':
                    found_sake = True
                    
                    temp_x, temp_y = current_x, current_y
                    path = []
                    
                    while maze[temp_y][temp_x] == 'Z':
                        path.append((temp_x, temp_y))
                        for dx2, dy2 in directions:
                            prev_x, prev_y = temp_x - dx2, temp_y - dy2
                            if 0 <= prev_x < n and 0 <= prev_y < n and maze[prev_y][prev_x] == 'Z':
                                temp_x, temp_y = prev_x, prev_y
                                break
                    
                    for px, py in reversed(path):
                        maze[py][px] = 'Z'
                        for row in maze:
                            print(''.join(row))
                        print(dir_names[i])
                        print()
                    
                    maze[new_y][new_x] = 'Z'
                    for row in maze:
                        print(''.join(row))
                    print("It was way too easy to get here, hand over the sake already, you lousy cook!")
                    return
                
                elif maze[new_y][new_x] == '.':
                    maze[new_y][new_x] = 'Z'
                    queue.append((new_x, new_y))
                    
                    for row in maze:
                        print(''.join(row))
                    print(dir_names[i])
                    print()
    
    for row in maze:
        print(''.join(row))
    print("This is the best day of my life! I will never find that sake!")

if __name__ == "__main__":
    solve_maze()
