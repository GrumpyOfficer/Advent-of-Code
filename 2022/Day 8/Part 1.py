rows = open("2022\\Day 8\\testdata.txt", "r").read().split("\n")
colums = [list(column) for column in zip(*rows)]

def visibleLeft(currRow, height, currentTreePos):
    count = 0
    for letter in [*rows[currRow]][:currentTreePos]:
        if int(letter) < height:
            count += 1
    if count == len([*rows[currRow]][:currentTreePos]):
        return True
    else:
        return False

def visibleRight(currRow, height, currentTreePos):
    count = 0
    for letter in [*rows[currRow]][currentTreePos+1:]:
        if int(letter) < height:
            count += 1
    if count == len([*rows[currRow]][currentTreePos+1:]):
        return True
    else:
        return False

print(colums)

def checkTree(currentTreeRow, currentTree):
    prevRowTrees = [*rows[currentTreeRow-1]]
    currRowTrees = [*rows[currentTreeRow]]
    nextRowTrees = [*rows[currentTreeRow+1]]
    tree = currRowTrees[currentTree]
    if prevRowTrees[currentTree] >= tree and currRowTrees[currentTree-1] >= tree and currRowTrees[currentTree+1] >= tree and nextRowTrees[currentTree] >= tree:
        return 0    # Tree is not visible
    else:
        return 1    # Tree is visible

# !!! Die GANZE reihe testen nicht nur die angrenzenden !!!

visibleTrees = 0

currentRow = 1
currentTree = 1

while currentRow < len(rows)-1:
    row = [*rows[currentRow]][:-1]
    currentTree = 0
    while currentTree < len(row)-1:
        currentTree += 1
        visibleTrees += checkTree(currentRow, currentTree)
    currentRow += 1

outerRing = (len(rows)-2)*2+len(rows[0])*2
print(visibleTrees, outerRing)