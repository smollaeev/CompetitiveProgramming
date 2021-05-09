class Node:
    def __init__(self, i, j, values):
         self.x = i 
         self.y = j
         self.find_Neigbours (values)
    def find_Neigbours (self, values):
        try:
            if values [self.x][self.y - 1] == '1':
                self.neigbours.append ([self.x, self.y-1])
                self.flags.append (0)
        except:
            pass
        try:
            if values [self.x][self.y + 1] == '1':
                self.neigbours.append ([self.x, self.y + 1])
                self.flags.append (0)
        except:
            pass
        try:
            if values [self.x -1][self.y] == '1':
                self.neigbours.append ([self.x - 1, self.y])
                self.flags.append (0)
        except:
            pass
        try:
            if values [self.x + 1][self.y] == '1':
                self.neigbours.append ([self.x + 1, self.y])
                self.flags.append (0)
        except:
            pass

class Map:
    def __init__(self, values):
        for i in range (len ())
        map.nodes.append ()

T = int (input ())
for t in range (T):
    input_ = input ().split ()
    N = input_ [0]
    M = input_ [1]
    values = []
    for i in range (N):
        values.append (input ())
    nodes = []
    for i in range (N):
        for j in range (M):
            nodes.append (Node (i, j, values))
    neigbours = []
    for node in range (nodes):
        neigbours.append (len (node.neigbours))
        maxIndex = neigbours.index(max(neigbours))
        
    map = Map (values)

