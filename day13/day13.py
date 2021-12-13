import statistics

def main():
    test = False
    if test:
        lmax = 18
        with open('test', 'r') as f:
            strlines = f.readlines()
    else:
        lmax = 959
        with open('input', 'r') as f:
            strlines = f.readlines()
    
    lines = [line.strip() for line in strlines]

    points = [(int(line.split(',')[0]), int(line.split(',')[1])) for line in lines[:lmax]]

    print(points[-1])
    foldlines = lines[lmax+1:]
    if not test:
        print(len(foldleft(655, points)))

    for line in foldlines:
        print(line)
        foldnum = int(line.split('=')[-1])
        if line.split('=')[-2][-1] == 'x':
            points = foldleft(foldnum, points)
        elif line.split('=')[-2][-1] == 'y':
            points = foldup(foldnum, points)
        else:
            print("badline")
    render_points(points)
    
def render_points(points):
    xmax = 0
    ymax = 0
    for point in points:
        if point[0] > xmax:
            xmax = point[0]
        if point[1] > ymax:
            ymax = point[1]

    for y in range(ymax+2):
        line = []
        for x in range(xmax+2):
            if (x, y) in points:
                line += [' # ']
            else:
                line += [' . ']
        print(''.join(line))
            

def foldleft(foldline, points):
    newpoints = []
    for x, y in points:
        if x > foldline:
            newpoint = (2*foldline - x, y)
        else:
            newpoint = (x, y)
        if newpoint not in newpoints:
            newpoints += [newpoint]

    return newpoints

def foldup(foldline, points):
    newpoints = []
    for x, y in points:
        if y > foldline:
            newpoint = (x, 2*foldline - y)
        else:
            newpoint = (x, y)
        if newpoint not in newpoints:
            newpoints += [newpoint]

    return newpoints

if __name__ == '__main__':
    main()