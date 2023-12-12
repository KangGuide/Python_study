
with open('data/chicken.txt', 'r') as f:
    for line in f:
        chicken = line.strip()
        chicken1 = chicken.split(": ")
    #   chickenSell = chicken[1] + chickenSell
        print(chicken)
