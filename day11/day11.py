import statistics

def main():
    test = False
    if test:
        with open('test.txt', 'r') as f:
            strlines = f.readlines()
    else:   
        with open('input.txt', 'r') as f:
            strlines = f.readlines()
    
    lines = [line.strip() for line in strlines]
    
    octopi = [[int(c) for c in line] for line in lines]
    flashes = 0
    for i in range(100):
        flashes += update_energy(octopi)

    print(flashes)

    i = 101
    while(update_energy(octopi)<100):
        i += 1
    print(i)

def update_energy(octopi):
    for i in range(len(octopi)):
        for j in range(len(octopi[i])):
            octopi[i][j] += 1
    for i in range(len(octopi)):
        for j in range(len(octopi[i])):
            if octopi[i][j] > 9:
                octopi = flash(octopi, i, j)
    flashes = 0
    for i in range(len(octopi)):
        for j in range(len(octopi[i])):
            if octopi[i][j] < 0:
                octopi[i][j] = 0
                flashes += 1
    return(flashes)

def flash(octopi, i, j):
    octopi[i][j] = -1
    toinc = []
    if i > 0:
        toinc += [(i-1, j)]
        if j > 0:
            toinc += [(i-1, j-1)]
        if j < len(octopi[i])-1:
            toinc += [(i-1, j+1)]
    if i < len(octopi)-1:
        toinc += [(i+1, j)]
        if j > 0:
            toinc += [(i+1, j-1)]
        if j < len(octopi[i])-1:
            toinc += [(i+1, j+1)]
    if j > 0:
            toinc += [(i, j-1)]
    if j < len(octopi[i])-1:
        toinc += [(i, j+1)]

    for x, y in toinc:
        if octopi[x][y] >= 0:
            octopi[x][y] += 1
        if octopi[x][y] > 9:
            octopi = flash(octopi, x, y)
    return octopi

if __name__ == '__main__':
    main()