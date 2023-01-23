class Board():
    def __init__(self, init, goal):
        self.current = init
        self.goal = goal
        self.blank = self.current.index(' ')
        self.col = len(self.current[0]) - 1
        self.row = len(self.current) - 1
        self.cost = 0
        if self.blank == None:
            print("Invalid Init State")
            return
        # for i in range(len(current)):
        #     for j in range(len(current[0])):
        #         if current
    
    def check(self,r,c):
        if 0<=r and r<=self.row and 0<=c and c<=self.col:
            return True
        return False
    def move(self, action):
        if action == None:
            print("Invalid Action: No action inputted")
            return
        action = action.lower()
        r = self.blank[0]
        c = self.blank[1]
        if action=='l':
            if self.check(r,c-1):
                self.current[r][c-1], self.current[r][c]  = self.current[r][c], self.current[r][c-1]
                self.blank = (r,c-1)
                return
            else:
                print("Invalid Action: Out of index")
                return

        if action=='r':
            if self.check(r,c+1):
                self.current[r][c+1], self.current[r][c]  = self.current[r][c], self.current[r][c+1]
                self.blank = (r,c+1)
                return
            else:
                print("Invalid Action: Out of index")
                return
        if action == 'u':
            if self.check(r-1, c):
                self.current[r-1][c], self.current[r][c]  = self.current[r][c], self.current[r-1][c]
                self.blank = (r-1, c)
                return
            else:
                print("Invalid Action: Out of index")
                return
        if action == 'd':
            if self.check(r+1, c):
                self.current[r+1][c], self.current[r][c]  = self.current[r][c], self.current[r+1][c]
                self.blank = (r+1, c)
                return
            else:
                print("Invalid Action: Out of index")
                return
        print("Invalid Action")
        return

    def actionSpace(self):
        pass
    
    def h(self):
        hn = 0
        for i in range(self.row):
            for j in range(self.col):
                if self.current[i][j] == self.goal[i][j]:
                    hn+=1
        return hn

    def g(self):
        return self.cost
    
    def f(self):
        return self.h() + self.g()
    
    def AStar(self):
        pass
    
    def GBFS(self):
        pass
    
    def printPath(self):
        pass 