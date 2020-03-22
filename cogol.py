import numpy as np
import json 
import time


class Gol ():
    """  """
    def __init__(self):
        """ Initializarion of the Game
            All Variables are set in the Config File of JSON"""
        
        ############# Params From File ###########
        with open("config/config.json") as c:
            config = json.load(c)
        
        self.rows = config ["rows"]
        self.cols = config ["cols"]
        self.hold_time = config ["timeHold"]
        self.stills = config ["stills"]
        self.max_iter = config ["maxIter"]
        self.display_char = config["displayChar"]
        ##########################################

        self.board = np.zeros( ( self.rows , self.cols ) )
        
    def printWelcome ( self ):
        """ Welcome Screen 
            Args : None
            Return : None
        """
        msg = """Welcome to Conway's Game of Life!!
        Please Select your Initial Setup:"""
        print(msg)

    def printSelectionList ( self ):
        """ Selection Message 
            Args: None
            Return: None
        """
        for i,j in enumerate(self.stills.keys()):
                    print(str(i) + ". " + j)
        print("9. RANDOM")

    def selection(self):
        """ Select What your initial cell patterns required
            Args: None
            Return None
        """
        while 1 :
                self.printSelectionList()
                ind = int(input())
                
                if 0 <= ind <= 8:
                    self.game =  np.array(list(self.stills.values())[ind])
                    self.setBoard()
                    break

                elif ind==9:
                    self.game = None
                    self.board = np.random.choice([0,1] , (self.rows , self.cols))
                    break

                else:
                    print ("Please Type Valid Index")

    def setBoard ( self ):
        """ Sets the Middle Of the Board to the Game
            Args: None
            Return: None
        """
        self.board[int(self.rows/2) : int(self.rows/2) + self.game.shape[0] ,\
                        int(self.cols/2) : int(self.cols/2) + self.game.shape[1]] = self.game

    def getNeighborSum(self , i , j):
        """ Gets the Sum of Neighbors to check future status of the cell 
            Args :
                i: x index of current Checking Cell 
                j: y index of current Checking Cell
            Return :
                (int) sum of Neighbouring Cells  
        """
        sum = 0
        for r in range(-1,2):
            for c in range(-1,2):
                if (0 <= i+r < self.rows) and (0 <= j+c < self.cols): # Check For Index in range
                    sum+=self.board[i+r,j+c]
        return sum - self.board[i,j]
    
    def isAlive(self , i , j):
        """ Check if cell is Alive or Dead
            Args :
                i: x index of current Checking Cell 
                j: y index of current Checking Cell
            Return :
                (bool) True if Alive , False if Dead  
        """
        return self.board [i,j]

    def playMove ( self ):
        """ Plans The Next Generation and Stores """
        temp = np.zeros((self.rows , self.cols))
        while (self.max_iter != 0):
            for r in range(self.rows):
                for c in range(self.cols):
                    neighbor_sum = self.getNeighborSum(r,c)
                    
                    if not self.isAlive(r,c) and neighbor_sum==3:
                        temp[r,c] = 1 
                    elif self.isAlive(r,c) and 2<=neighbor_sum<=3:
                        temp[r,c] = 1
                    else:
                        temp[r,c] = 0 
            self.max_iter -=1
            self.board = temp
            temp = np.zeros((self.rows , self.cols))
            self.drawPattern()

    def drawPattern(self):
        """ Print the Pattern Generated by PlayMove """
        for row in self.board:
            print(" ".join(map(self.valToChar, row)))
        time.sleep(self.hold_time/1000) 
        print("\033[%dA"%(self.rows+1)) #This is used for dynamical printing, It moves the cursor up by self.rows+1 lines

    def valToChar(self, val):
        """ Converts value in board numpy array to char for displaying the game """
        return self.display_char if val == 1 else " "

    def playOneMove(self):
        temp = np.zeros((self.rows,self.cols))
        for r in range(self.rows):
            for c in range(self.cols):
                neighbor_sum = self.getNeighborSum(r,c)
                
                if not self.isAlive(r,c) and neighbor_sum==3:
                    temp[r,c] = 1 
                elif self.isAlive(r,c) and 2<=neighbor_sum<=3:
                    temp[r,c] = 1
                else:
                    temp[r,c] = 0 
        self.board = temp

    
if __name__ == "__main__":
    o = Gol()
    o.printWelcome()
    o.selection()
    o.playMove()
    print ("Thank you For Playing!")