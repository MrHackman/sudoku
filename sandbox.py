from math import sqrt
testlist=[]
value=0
cell=0
sector=0
sectX=0
sectY=0

size=9

for y in range(size):
    sectY=y//(int(sqrt(size)))
    testlist.append([])
    for x in range(size):
        sectX=x//(int(sqrt(size)))
        print("sectX:",sectX,"sectY:",sectY)
        testlist[y].insert(x,int(sectX+(sectY*(sqrt(size)))))
    
