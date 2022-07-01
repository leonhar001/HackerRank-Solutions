import itertools

listElements = []
squaredElements = []
allModulos = []

KandM= input().split() #KandM[0] = K , KandM[1] = M
K = int(KandM[0])
M = int(KandM[1])

i = 0
while i < K: #get all inputs
    line = input().split()
    line.pop(0)
    listElements.insert(i, line)
    i+=1

for element in listElements: 
    element = [int(i) for i in element] #convert to int
    squaredElements.append(list(map(lambda x:x**2, element))) # square of every element

allCombinations = list(itertools.product(*squaredElements)) #do all possible combinations

for combination in allCombinations:
    allModulos.append(sum(combination) % M) #get all possible modulos
    
print(max(allModulos)) #get the biggest modulo
