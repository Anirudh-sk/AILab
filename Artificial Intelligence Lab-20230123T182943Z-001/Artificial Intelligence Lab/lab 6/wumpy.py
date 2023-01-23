# import os
class WWorld:
    def __init__(self, b = None, visited = None):
        self.b = b
        self.visited = visited
        self.actions = ['up', 'down', 'left', 'right', 'grab']
        self.agent = [len(b[0])-1, 0]
        self.actionTrans = {'up' : (-1,0), 'down' : (1,0), 'left':(0,-1), 'right':(0,1), 'grab': 1}
        self.score = 0
        self.scoringScheme = {'Gold':1000, 'action':-1, 'death':-1000}

    def _mask(self):
        k = [['-' for _ in range(len(self.b[0]))] for _ in range(len(self.b[0]))]
        for i in range(len(self.b)):
            for j in range(len(self.b[0])):
                if self.visited[i][j]:
                    k[i][j] = self.b[i][j]
        return k
    def _printRow(self, a):
        f = '|'
        for i in range(len(a)):
            f += '{'+str(i)+':^4}|'
        print(f.format(*a))
    
    def _printEmptyRow(self, n):
        for i in range(n):
            print(' ----', end="")
        print()
    
    def printGameFullyObs(self, b):
        if b == None:
            return
        n = len(b[0])
        self._printEmptyRow(n)
        for i in b:
            self._printRow(i)
            self._printEmptyRow(n)
    
    def printGame(self):
        self.printGameFullyObs(b=self._mask())
    
    def printActions(self):
        print(*self.actions)
    
    def _isGold(self, cord):
        if 'G' in self.b[cord[0]][cord[1]]:
            return True
        return False
    
    def _isValidCords(self, cord):
        if cord[0] < len(self.b[0]) and cord[0] >= 0 and cord[1] < len(self.b[0]) and cord[1] >= 0:
            return True
        return False
    
    def _isSafe(self, cord):
        if 'W' in self.b[cord[0]][cord[1]] or 'P' in self.b[cord[0]][cord[1]]:
            return False
        return True

    def move(self, action):
        # os.system('cls')
        self.score+=self.scoringScheme['action']
        na = self.actionTrans[action]
        if na == 1:
            if self._isGold(self.agent):
                self.b[self.agent[0]][self.agent[1]] = self.b[self.agent[0]][self.agent[1]].replace('G','')
                self.score+=self.scoringScheme['Gold']
                return True
        else:
            if self._isValidCords(self.agent) and self._isValidCords([self.agent[0]+na[0], self.agent[1]+na[1]]):
                # print(self.agent)
                self.b[self.agent[0]][self.agent[1]] = self.b[self.agent[0]][self.agent[1]].replace('A','')
                # print(self.b[self.agent[0]][self.agent[1]])
                # print(self.b)
                self.agent[0]+= na[0]
                self.agent[1]+= na[1]
                # print(self.agent)
                self.visited[self.agent[0]][self.agent[1]] = True
                self.b[self.agent[0]][self.agent[1]] += 'A'
            else:
                print("Invalid Move: Out of Bounds")
                return False
        if not self._isSafe(self.agent):
            self.score+=self.scoringScheme['death']
            return True
        
    def run(self):
        over = False
        while(not over):
            self.printGame()
            # print(self.f())
            print(self.actions)
            print("Enter the move to make")
            action = input().rstrip()
            action.lower()
            over = self.move(action)

board = [['S', ' ', 'B','P'], ['W', 'BSG', 'P','B'],['S',' ','B',' '],['A','B','P','B']]
visited = [[False for _ in range(len(board[0]))] for _ in range(len(board[0]))]
visited[len(board[0])-1][0] = True
a = WWorld(b = board, visited = visited)
# a.printGame()
a.run()
a.printGame()
print(a.score)