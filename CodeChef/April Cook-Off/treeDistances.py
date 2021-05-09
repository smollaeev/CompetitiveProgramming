T = int (input ())
for t in range (T):
    firstLine = input ().split ()
    firstLineInt = list (map (int, firstLine))
    x = firstLineInt [0]
    y = firstLineInt [1]
    if not (is_Tree (x, y)):
        print ('NO')
    else:
        print ('YES')
        print (n)
        for i in range (n):
            print (vertice [i])