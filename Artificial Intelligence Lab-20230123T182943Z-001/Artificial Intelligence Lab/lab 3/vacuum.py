daemon = []
class Env:
    def __init__(self,left=1,right=1,vacuum='l',parent=None, prev_action=None, cost=0):
        self.room = dict()
        self.room['l'] = left
        self.room['r'] = right
        self.v = vacuum
        self.dict = dict()
        self.dict['l'] = 'Left'
        self.dict['r'] = 'Right'
        self.dict[0] = 'Clean'
        self.dict[1] = 'Dirty'
        self.cost = cost
        self.parent = parent
        self.prev_action = prev_action 

    def __repr__(self):
        return f'<Vacuum:<{self.dict[self.v]}>, Room:<{self.dict[self.room["l"]]}, {self.dict[self.room["r"]]}>>'

    def action(self, action=None):
        action = action.upper()
        if action not in ['L','R','S']:
            return None
        newNode = Env(self.room['l'],self.room['r'], self.v)
        if action == 'L':
            newNode.v = 'l'
        if action == 'R':
            newNode.v = 'r'
        if action == 'S':
            newNode.room[newNode.v] = 0
        newNode.parent = self
        newNode.prev_action = action
        newNode.cost = self.cost+1
        return newNode

    def copy(self):
        return Env(self.room['l'], self.room['r'], self.v, self.parent,self.prev_action,self.cost)

    def actionSpace(self):
        temp = self.copy()
        print()
        print(f"Current State = {temp}")
        actions = ['L', 'R', 'S']
        print(f"Actions({temp}) = {actions}")
        print("Transition Model \n ------")
        for i in actions:
            a = self.copy()
            print(f"Result({a}, {i}) = {a.action(i)}")
        print(" ------ ")
    
    def nodeState(self):
        print(' ------ ')
        print('_________')
        print("Node:",self)
        print('_________')
        print("Parent:",self.parent)
        print("Previous Action:",self.prev_action)
        print("Cost:",self.cost)
        print(' ------ ')
if __name__ == "__main__":
    a = Env()
    print("Enter the Initial Position of Vacuum (l for ",
            "left and r for right):")
    vacuum = input().rstrip()
    print("Enter the Cleaniness of the Left and Right Room:")
    print("0 0 = Clean Clean\n0 1 = Clean Dirty\n1 0 = Dirty Clean\n1 1 = Dirty Dirty")
    l, r = map(int, input().split())
    env = Env(l, r, vacuum)
    while(env):
        daemon.append(env)
        env.actionSpace()
        print("Enter the action to take:")
        action = input().rstrip()
        env = env.action(action)
        # if env:
        #     env.nodeState()
    print("Tree:")
    for i in daemon:
        i.nodeState()
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print(" V")
    print("End")