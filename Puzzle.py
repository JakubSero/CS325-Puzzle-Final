import heapq


# description: Find a minimum length path between the Source and the Destination

# input: Board - 2D array with '-' for traversable space and '#' for obstructions
#        Source - starting location on the Board (tuple of x,y coordinates)
#        Destination - ending location on the Board (tuple of x,y, coordinates)

# output: List of tuples that show the path taken from the Source to the Destination

def solve_puzzle(Board, Source, Destination):
    distance = 0
    result = []
    m = len(Board)
    n = len(Board[0])
    visited = [[False for i in range(n)] for j in range(m)]
    q = []
    heapq.heappush(q, (Source[0], Source[1], distance))
    while len(q) > 0:
        distance += 1
        current = heapq.heappop(q)

        if visited[current[0]][current[1]]:
            continue
        else:
            result.append(current)

        if current[0] == Destination[0] and current[1] == Destination[1]:
            return path(result)

        visited[current[0]][current[1]] = True

        for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x, y = current[0] + i, current[1] + j
            if 0 <= x < m and 0 <= y < n and not visited[x][y] and Board[x][y] != '#':
                heapq.heappush(q, (x, y, min(current[2] + 1, distance)))

    return None


def path(result):
    answer = [(result[-1][0], result[-1][1])]
    last = result[-1]
    for i in result[::-1]:
        # check if distance is 1 between two nodes in the result array and then check
        # all directions to make sure only one coordinate changed value.
        # otherwise, we know they are not connected
        if i[2] == last[2] - 1 and \
                ((last[0] - i[0] == 1 and last[1] - i[1] == 0) or
                 (last[1] - i[1] == 1 and last[0] - i[0] == 0) or

                 (i[0] - last[0] == 1 and i[1] - last[1] == 0) or
                 (i[1] - last[1] == 1 and i[0] - last[0] == 0)):
            answer.append((i[0], i[1]))
            last = i

    return answer[::-1]

print(solve_puzzle([['-', '-', '-', '-', '-'],
                    ['#', '-', '-', '-', '-'],
                    ['-', '#', '#', '-', '-'],
                    ['-', '-', '-', '-', '-'],
                    ['-', '-', '-', '-', '-']], (0,0), (3,2)))
