with open('input.txt', 'r') as f:
    strlines = f.readlines()

hor = 0
depth = 0
aim = 0
for line in strlines:
    num = line.strip()[-1]
    if "forward" in line:
        hor += int(num)
        depth += int(num)*aim
    if "down" in line:
        aim += int(num)
    if "up" in line:
        aim -= int(num)
print(str(hor*depth))