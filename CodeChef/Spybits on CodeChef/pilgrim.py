def find_RequiredEnergies (specialCities, graph):
    requiredEnergies = []
    for city in specialCities:
        
def find_SpecialCities (graph):
    specialCities = []
    vertices = graph [:, 0]+graph [:, 1]
    for v in vertices:
        if v.count () == 1 and v not in specialCities:
            specialCities.append (v)
    return specialCities

def calculate_MaximumNoneEmptySpecials (graph):
    specialCities = find_SpecialCities (graph)
    requiredEnergies = find_RequiredEnergies (specialCities, graph)

T = int (input ())
if T<1 or T> 50:
    exit ()
answers = []
for t in range (T):
    firstLineList = input ().split ()
    if len (firstLineList) != 2:
        exit ()
    N = int (firstLineList [0])
    M = int (firstLineList [1])
    if N<2 or N>10**5 or M<1 or M>10**5:
        exit ()
    secondLineList = input ().split ()
    energies = list (map (int, secondLineList))
    for energy in energies:
        if energy < 1 or energy > 10**18:
            exit ()
    U = []
    V = []
    K = []
    graph = []
    for line in range (N - 1):
        inputList = input ().split ()
        graph.append (list (map (int, inputList)))
        if graph [line][0]<1 or graph [line][0] > N or graph [line][1] < 1 or graph [line][1] > N:
            exit ()
        if graph [line][2] < 1 or graph [line][2] > 10**6:
            exit ()
    
    answers.append (calculate_MaximumNoneEmptySpecials (graph))

for t in range (T):
    print (answers [t])