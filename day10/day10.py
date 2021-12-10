from statistics import median

def main():
    test = False
    if test:
        with open('test.txt', 'r') as f:
            strlines = f.readlines()
    else:   
        with open('input.txt', 'r') as f:
            strlines = f.readlines()

    lines = [line.strip() for line in strlines]
    score = 0
    newlines = []

    for line in lines:
        lscore = scoreline(line)
        score += lscore
        if not lscore:
            newlines.append(line)
    print(score)

    scores= []
    for line in newlines:
        scores.append(finishline(line))
    print(median(scores))

def scoreline(line):
    stack = []
    for c in line:
        if c == '{':
            stack.append('}')
        elif c == '[':
            stack.append(']')
        elif c == '(':
            stack.append(')')
        elif c == '<':
            stack.append('>')
        elif stack:
            correct = stack.pop()
            if c != correct:
                return scorechar(c)
        else:
            return scorechar(c)
    return 0

def finishline(line):
    stack = []
    for c in line:
        if c == '{':
            stack.append('}')
        elif c == '[':
            stack.append(']')
        elif c == '(':
            stack.append(')')
        elif c == '<':
            stack.append('>')
        else:
            correct = stack.pop()

    score = 0
    for c in reversed(stack):
        score *= 5
        if c == ')':
            score += 1
        elif c == ']':
            score += 2
        elif c == '}':
            score += 3
        elif c == '>':
            score += 4
    return score

def scorechar(char):
    if char == ')':
        return 3
    if char == ']':
        return 57
    if char == '}':
        return 1197
    if char == '>':
        return 25137
    return 0

if __name__ == '__main__':
    main()