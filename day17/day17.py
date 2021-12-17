import statistics

def main():
    test = False
    if test:
        with open('test', 'r') as f:
            strlines = f.readlines()
    else:   
        with open('input', 'r') as f:
            strlines = f.readlines()
    
    lines = [line.strip() for line in strlines]

    xtarg = (241, 275)
    ytarg = (-75, -49)

    ymax = ytarg[0]
    numshots = 0

    for xvel in range(22, 276):
        for yvel in range(-75, 1000):
            p = probe(xvel, yvel, xtarg, ytarg)
            ret = p.run_through()
            if ret[0]:
                numshots += 1
                if ret[1] > ymax:
                    ymax = ret[1]

    print("ymax: {}".format(ymax))
    print("numshots: {}".format(numshots))

class probe:
    def __init__(self, xvel, yvel, xtarg, ytarg):
        self.xvel = xvel
        self.yvel = yvel
        self.xpos = 0
        self.ypos = 0

        self.xmin = xtarg[0]
        self.xmax = xtarg[1]
        self.ymin = ytarg[0]
        self.ymax = ytarg[1]

        self.x_history = []
        self.y_history = []
        self.x_history.append(self.xpos)
        self.y_history.append(self.ypos)

    def step(self):
        self.xpos += self.xvel
        self.ypos += self.yvel

        if self.xvel > 0:
            self.xvel -= 1
        elif self.xvel < 0:
            self.xvel += 1
        self.yvel -= 1

        self.x_history.append(self.xpos)
        self.y_history.append(self.ypos)

        if self.intarget():
            return True
        else:
            return False

    def run_through(self):
        found = False
        while not found:
            if self.ypos < self.ymin:
                return (False, self.ypos)
            if self.xvel > 0 and self.xpos > self.xmax:
                return (False, self.ypos)
            if self.xvel < 0 and self.xpos < self.xmin:
                return (False, self.ypos)
            if self.xvel == 0 and (self.xpos < self.xmin or self.xpos > self.xmax):
                return (False, self.ypos)
            
            found = self.step()
        return (True, max(self.y_history))

    def intarget(self):
        if self.xpos >= self.xmin and self.xpos <= self.xmax and self.ypos >= self.ymin and self.ypos <= self.ymax:
            return True
        else:
            return False

if __name__ == '__main__':
    main()