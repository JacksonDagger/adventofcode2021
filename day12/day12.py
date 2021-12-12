import statistics

def main():
    test = False
    if test:
        with open('test.txt', 'r') as f:
            strlines = f.readlines()
    else:   
        with open('input', 'r') as f:
            strlines = f.readlines()
    
    lines = [line.strip() for line in strlines]

    # Part 1
    vertices = {}
    for line in lines:
        v1 = line.split('-')[0]
        v2 = line.split('-')[1]
        if v1 in vertices:
            vertices[v1].append(v2)
        else:
            vertices[v1] = [v2]
        if v2 in vertices:
            vertices[v2].append(v1)
        else:
            vertices[v2] = [v1]

    paths = chart_paths(['start'], vertices, set())
    print(len(paths))

    paths = chart_paths_p2(['start'], vertices, set(), False)
    print(len(paths))
    

def chart_paths(prev, vertices, visited):
    viscopy = visited.copy()
    if prev[-1] == 'end':
        return [prev]
    if prev[-1].islower():
        viscopy.add(prev[-1])

    paths = []
    tovisit = vertices[prev[-1]]
    for v in tovisit:
        if v not in viscopy:
            newprev = prev + [v]
            paths += chart_paths(newprev, vertices, viscopy)

    return paths

def chart_paths_p2(prev, vertices, visited, dblvisit):
    viscopy = visited.copy()
    if prev[-1] == 'end':
        return [prev]
    if prev[-1].islower():
        if prev[-1] in viscopy:
            if dblvisit:
                return []
            else:
                dblvisit = True
        viscopy.add(prev[-1])

    paths = []
    tovisit = vertices[prev[-1]]
    for v in tovisit:
        if v == 'start':
            continue
        if (v in viscopy) and dblvisit:
            continue
        
        newprev = prev + [v]
        paths += chart_paths_p2(newprev, vertices, viscopy, dblvisit)

    return paths
    
if __name__ == '__main__':
    main()