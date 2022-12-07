# Adjacent Matrix
G = [[ 0, 1, 1, 0, 1, 0],
     [ 1, 0, 1, 1, 0, 1],
     [ 1, 1, 0, 1, 1, 0],
     [ 0, 1, 1, 0, 0, 1],
     [ 1, 0, 1, 0, 0, 1],
     [ 0, 1, 0, 1, 1, 0]]




Vertex = "abcdef"
t_={}
for i in range(len(G)):
  t_[Vertex[i]] = i

degree =[]
for i in range(len(G)):
  degree.append(sum(G[i]))


colorDict = {}
for i in range(len(G)):
    colorDict[Vertex[i]] = ["C2", "C3", "C1", "C4"]



empty_list = []

#counter variable to count unique values
count = 0


for ele in colorDict[Vertex[i]] :
    if(ele not in empty_list):
        count += 1
        empty_list.append(ele)


sortedNode=[]
index = []


for i in range(len(degree)):
  _max = 0
  j = 0
  for j in range(len(degree)):
    if j not in index:
      if degree[j] > _max:
        _max = degree[j]
        idx = j
  index.append(idx)
  sortedNode.append(Vertex[idx])


theSolution={}
for n in sortedNode:
  setTheColor = colorDict[n]
  theSolution[n] = setTheColor[0]
  adjacentNode = G[t_[n]]
  for j in range(len(adjacentNode)):
    if adjacentNode[j]==1 and (setTheColor[0] in colorDict[Vertex[j]]):
      colorDict[Vertex[j]].remove(setTheColor[0])


# Print the solution
for t,w in sorted(theSolution.items()):
  print("Vertex",t," = Color",w)
print("Find The chromatic number :", count)
