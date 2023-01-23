from collections import defaultdict
class PriorityQueue:
    def __init__(self, func):
        self.arr = []
        self.func = func

    def isEmpty(self):
        if len(self.arr) == 0:
            return True
        return False

    def siftUp(self, i):
        j = i//2
        if j > 0 and self.func(self.arr[i]) < self.func(self.arr[j]):
            self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
            self.siftUp(j)
        return
    
    def left(self, i):
        return 2*i
    
    def right(self, i):
        return 2*i + 1

    def siftDown(self, i=0):
        j = min(self.left(i), self.right(i))
        if j <= len(self.arr)-1 and self.func(self.arr[i]) > self.func(self.arr[j]):
            self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
            self.siftDown(j)
        return
    
    def insert(self, ele):
        self.arr.append(ele)
        self.siftUp(len(self.arr)-1)
    
    def pop(self):
        mini = self.arr[0]
        self.arr[0] = self.arr[-1]
        self.arr.pop(-1)
        self.siftDown()
        return mini

class eightP:
    def __init__(self, b, blank, score = 0, noActions = 0):
        self.b = b
        self.blank = blank
        self.actionTrans = {
            "up":[-1,0],
            "down":[1,0],
            "right":[0,1],
            "left":[0,-1]
        }

        self.goal = [[1,2,3],[8,0,4],[7,6,5]]
        self.score = 0
        self.reward = 100
        self.actionCost = -1
        self.lastAction = None
        self.noActions = 0
    
    def copy(self):
        return eightP(self.b, self.blank, self.score, self.noActions)
    
    def _updateBlank(self, action):
        return [self.blank[0] + action[0], self.blank[1] + action[1]]
    
    def _move(self, action):
        self.b[self.blank[0]][self.blank[1]], self.b[self.blank[0]+action[0]][self.blank[1]+action[1]] = self.b[self.blank[0]+action[0]][self.blank[1]+action[1]], self.b[self.blank[0]][self.blank[1]]
        self.blank = self._updateBlank(action)
        self.noActions += 1
        # temp = self.blank.copy()
        # self.blank[0]+=action[0]
        # self.blank[1]+=action[1]
        # tempValue = self.b[self.blank[0]][self.blank[1]]
        # self.b[self.blank[0]][self.blank[1]] = 0
        # self.b[temp[0]][temp[1]] = 
    
    def _isValid(self, action):
        a, b = self._updateBlank(action)
        if 0 <= a < 3 and 0 <= b < 3:
            return True
        return False
    
    def move(self, action):
        action = self.actionTrans[action]
        if self._isValid(action):
            self._move(action)
            return True
        else:
            # self.score = -1000 
            print("Invalid Move: Out of Index")
            return False
    
    def _printRow(self, a):
        f = '|'
        for i in range(len(a)):
            f += '{'+str(i)+':^4}|'
        print(f.format(*a))
    
    def _printEmptyRow(self, n):
        for i in range(n):
            print(' ----', end="")
        print()
    
    def printGame(self):
        if self.b == None:
            return
        n = len(self.b[0])
        self._printEmptyRow(n)
        for i in self.b:
            self._printRow(i)
            self._printEmptyRow(n)
    
    def run(self, printG = True):
        if printG == True: self.printGame()
        while(True):
            print("Enter you move: ['up', 'down', 'left', 'right']")
            action = input().rstrip()
            if not action in self.actionTrans.keys():
                print("Exit")
                break
            else:
                self.score+=self.actionCost
                self.move(action)
                if printG == True: self.printGame()
                print(self.f())
                if self.goal == self.b:
                    # self.score += self.reward
                    print("Reach Goal!!!")
                    print("Total score = ", self.score+self.reward)
                    break
    def h(self):
        hn = 0
        for i in range(len(self.b[0])):
            for j in range(len(self.b[0])):
                if self.b[i][j] != self.goal[i][j]:
                    hn+=1
        return hn
                
    def g(self):
        return self.noActions

    def f(self):
        return self.g()+self.h()
    
    def AStar(self):
        def AStarComp(a):
            return a.f()
        pp = PriorityQueue(AStarComp)
        pp.insert(self.copy())
        while(not pp.isEmpty()):
            orig = pp.pop()
            orig.printGame()
            print(orig.f())
            if orig.b == orig.goal:
                print("Total Score = ", orig.score)
                return
            for i in self.actionTrans.keys():
                temp = orig.copy()
                check = temp.move(i)
                if check:
                    temp.lastAction = i
                    pp.insert(temp)

        # bestAction = None
        # currentScore = self.b.f()
        # for i in self.actionTrans.keys():
        #     temp = self.copy()
        #     temp2 = temp.move(i)
        #     if temp2:
        #         pp.insert()

            
    def GBFS(self):
        pass

inputBoard = [[0,2,3],[1,8,4],[7,6,5]]
hardInput = [[7,8,1],[5,0,3],[2,6,4]]
a = eightP(b = inputBoard, blank = [0,0])
a.AStar()
# a.run()