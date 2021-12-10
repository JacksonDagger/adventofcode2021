def main():
    test = False
    if test:
        with open('test.txt', 'r') as f:
            strlines = f.readlines()
    else:   
        with open('input.txt', 'r') as f:
            strlines = f.readlines()
    
    lines = [line.strip() for line in strlines]
    

if __name__ == '__main__':
    main()