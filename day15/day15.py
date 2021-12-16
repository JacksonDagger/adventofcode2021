import statistics
from bisect import insort
from queue import PriorityQueue

def main():
    test = False
    if test:
        with open('test', 'r') as f:
            strlines = f.readlines()
    else:   
        with open('input', 'r') as f:
            strlines = f.readlines()
    
    lines = [line.strip() for line in strlines]
    risks = [[int(c) for c in line] for line in lines]

    distances = [['inf']*len(risks[0]) for _ in range(len(risks))]
    distances[0][0] = 0

    pq = PriorityQueue()
    pq.put((0, (0, 0)))

    visited = set()

    while not pq.empty():
        (dist, (x, y)) = pq.get()
        visited.add((x, y))

        neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        neighbors = list(filter(lambda v: isvalid(v, len(risks[0]), len(risks)), neighbors))
        for neighbor in neighbors:
            if neighbor not in visited:
                old_risk = distances[neighbor[0]][neighbor[1]]
                new_risk = dist + risks[neighbor[0]][neighbor[1]]

                if old_risk == 'inf' or new_risk < old_risk:
                    distances[neighbor[0]][neighbor[1]] = new_risk
                    pq.put((new_risk, neighbor))
    print(distances[-1][-1])

    # Part 2
    distances = [['inf']*len(risks[0])*5 for _ in range(len(risks)*5)]
    distances[0][0] = 0

    pq = PriorityQueue()
    pq.put((0, (0, 0)))

    visited = set()

    while not pq.empty():
        (dist, (x, y)) = pq.get()
        visited.add((x, y))

        neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        neighbors = list(filter(lambda v: isvalid(v, 5*len(risks[0]), 5*len(risks)), neighbors))
        for neighbor in neighbors:
            old_risk = distances[neighbor[0]][neighbor[1]]
            new_risk = dist + tiled_risk(neighbor[0], neighbor[1], risks)

            if old_risk == 'inf' or new_risk < old_risk:
                distances[neighbor[0]][neighbor[1]] = new_risk
                pq.put((new_risk, neighbor))
    print(distances[-1][-1])


def tiled_risk(x, y, risk):
    xinc = x // len(risk)
    yinc = y // len(risk[0])
    
    return ((risk[x % len(risk)][y% len(risk[0])] + xinc + yinc - 1) % 9) + 1

def isvalid(vertex, xmax, ymax):
    x = vertex[0]
    y = vertex[1]
    return x >= 0 and y >= 0 and x < xmax and y < ymax


if __name__ == '__main__':
    main()