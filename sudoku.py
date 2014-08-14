##
#   Morgan Grant
#   Aug 1,2014
#   Basic Sudoku Puzzle platform of arbitrary size

from math import floor
from math import sqrt


#whenever you get coordinates for a given cell it will be in the form of (which row),(which col).
#The only exceptions to this are if you ask (for example) col number 3 for the 5th cell in it's zone 2 (0,1,2),4 (0,1,2,3,4) but it's showing 4,2
#or if you ask about sectors (or a cell in a sector) those will be using the following as coordinates:
# 0 1 2
# 3 4 5
# 6 7 8
# top row left to right, then next row left to right. so cell 2,1 would be sector 1 cell 5 

class cell:
    def __init__(self,myRow=None,myCol=None,mySect=None,value=0):
        ##
        #   @param  (int)   value   should anywhere from 0 to puzzleSize. 0 is equivilent to a blank square
        #   @param  (zone)  myRow   pointer to the Row it occupies
        #   @param  (zone)  myCol   pointer to the Column it occupies
        #   @param  (zone)  mySect  pointer to the Section it occupies
        
        if type(myRow)==zone and myRow.getZoneType()=="ROW":
            self.__myRow=myRow
        elif type(myRow)==NoneType:
            raise notimplementederror
        else:
            raise typeError("Invalid myRow")
        
        if type(myCol)==zone and myCol.getZoneType()=="COL":
            self.__myCol=myCol
        elif type(myCol)==NoneType:
            raise notimplementederror
        else:
            raise typeError("Invalid myCol")

        if type(mySect)==zone and mySect.getZoneType()=="SECT":
            self.__mySect=mySect
        elif type(mySect)==NoneType:
            raise notimplementederror
        else:
            raise typeError("Invalid mySect")
        
        if value < 0 or value > myRow.getZoneSize():
            self.__value=value
        else:
            raise valueError("value is out of bounds")


        
    def getValue(self):
        return self.__value
    def getMyRow(self):
        return self.__myRow
    def getMyCol(self):
        return self.__myCol
    def getMySect(self):
        return self.__mySect
    def __repr__(self):
        if value>0:
            return self.getValue()
        else:
            return " "
        
    def __int__(self):
        return self.__value
    def __eq__(self,y):
        return self.__value == y.getValue()
    def __ne__(self,y):
        return not self.__eq__(y)

    def setValueHard(self,newValue=0):      #forcibly sets the new value regardless of if it's valid in that cell
        if newValue == " " or newValue == "" or newValue == None:
            newValue=0
            #notimplementederror    check to see if the new value is in VALIDVALUES up in puzzle
        self.__value=newValue
    def setValueSoft(self,newValue=0):      #uses canIFit(newValue) to check if it's valid, then calls setValueHard()
        raise notImplementedError
    def canIFit(self,newValue): #checks each sector it's in to see if a given value will fit in there
        raise notImplementedError
        
        return True
    def getPos(self):       #returns Row,Col as a tuple
        return ( getMyRow().getZonePos() , getMyCol().getZonePos() )

class zone:
    def __init__(self,ZoneType,ZonePos,ZoneSize, cells=None):
        ##
        #   @param  (str)   ZoneType    Should be "row", "Col" or "SECT" in any type of casing.
        #   @param  (int)   ZonePos     0-X where X is ZoneSize-1
        #   @param  (int)   ZoneSize    should be equal to puzzleSize in the puzzle in which it is contained (barring weird shit). should be a square)
        #   @param  (list)  cells       UNIMPLEMENTED a list of cell objects
        if (type(ZoneType) != str) or (ZoneType.upper() != "ROW" and ZoneType.upper() != "COL" and ZoneType.upper() != "SECT"):
            raise typeError("Invalid Zone Type")
        else:
            self.__zoneType=ZoneType.upper()
            
        if 0 > ZonePos or ZonePos >= ZoneSize:
            raise inputError("ZonePos out of bounds")
        else:
            self.__zonePos=int(ZonePos)

        if floor(sqrt(ZoneSize)) < sqrt(ZoneSize):
            raise inputError("invalid ZoneSize (should be a square)")
        else:
            self.__zoneSize=ZoneSize

        self.__cells=cells

    
    

    def getZoneType(self):
        return self.__zoneType
    def getZonePos(self):
        return self.__zonePos
    def getZoneSize(self):
        return self.__zoneSize
    def getCells(self):
        return self.__cells
    def getContents(self):
        #returns a set of the contents of filled cells in the zone
        contents=set()
        for cellObj in getCells():
            contents.add(cellobj.value())
        contents.discard(0)
        contents.discard(" ")
        return contents
        
    


class puzzle:
    def __init__(self,puzzleSize,startvalues=None):         #put some stuff in the doctest
        '''
        initializes the puzzle class

        >>> test1=puzzle(9)
        >>> pass
        >>> del test1
        '''
        ##
        #   @param  (int)   puzzlesize  the length of one side of the puzzle. should be a square number (4,9,16,etc)
        #   @param  (list)  startvalues list[rownumber] of lists[colnumber] of the start values for the differnet cells
        self.__puzzleSize=puzzleSize
        self.__rows=[]  #notimplemented
        self.__cols=[]  #notimplemented
        self.__sectors=[]   #notimplemented
        self.__VALIDVALUES=set([i for i in range(self.__puzzleSize)])
        self.__cells=[]          #a table of pointers to the cell objects themselves
        '''for row in range(self.__puzzleSize):         #notimplementederror
            self.__cells.append([])
            for col in range(self.__puzzleSize):
                self.__cells[row].insert(col,cell(ROW,COL,SECT))      #still need to implement proper assignment of sections'''

        
        
        
    #"get" methods
    def getRows(self):
        return self.__rows
    def getCols(self):
        return self.__cols
    def getSectors(self):
        return self.__sectors
    def getPuzzleSize(self):
        return self.__puzzleSize
    def getValidValues(self):
        return self.__VALIDVALUES

    def __repr__(self):  #notimplementederror
        raise notimplementederror
        return self
    
    def sectToCoord(self,sect,cellnum):
        pass
        raise notimplmentederror
        #hmmmm.... need some kind of math to convert sectorFOOcellBar into rowBAZcolQUUX and vice versa. should return a tuple 
    def coordToSect(self,row,col):
        '''
        Converts RowX ColY into SectorA Cell#B
        >>> test1=puzzle(9)
        >>> test1.coordToSect(4,6)
        (5, 3)
        >>> del test1
        '''
        sectorSize=int(sqrt(self.__puzzleSize))
        sectRow=row//sectorSize
        sectCol=col//sectorSize
        sector=int(sectCol+(sectRow*sectorSize))     #Sector determined
        cellSectRow=row-(sectRow*sectorSize)
        cellSectCol=col-(sectCol*sectorSize)
        cellNum=int(cellSectCol+(cellSectRow*(sqrt(self.__puzzleSize))))    #cell determined
        return (sector,cellNum)

    #"set" methods
    def setPuzzleConents(self, dataSet):
        #   @param  (list)  dataSet list[rownumber] of lists[colnumber] of the start values for the differnet cells 
        raise notimplementederror
    #not yet implemented
    def solvableTest():
        raise notImplementedError
        return False
    def autoSolve(self):        #this and antiSolve() will modify the puzzle it is run on.
        #this and the other anti/autosolves should have an option to only run it X number of steps into the future (default of 1,000,000) to prevent recursion.
        raise notImplementedError
    def antiSolve(self):
        raise notImplementedError
    def forkAutoSolve(self):    #this and forkAntiSolve() will spawn a new puzzle and attempt to run auto/antisolve() on it, then return the result
        raise notImplementedError
    def forkAntiSolve(self):
        raise notImplementedError
    



def importValues(puzz,filename):
    raise notImplementedError
def exportValues(puzz,filename):
    raise notImplementedError



if __name__ == "__main__":
	import doctest
	doctest.testmod(report=True)
