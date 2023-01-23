class Env:
    def __init__(self,left=1,right=1,vacuum='l'):
        self.room = dict()
        self.room['l'] = left
        self.room['r'] = right
        self.v = vacuum
        self.dict = dict()
        self.dict['l'] = 'Left'
        self.dict['r'] = 'Right'
        self.dict[0] = 'Clean'
        self.dict[1] = 'Dirty'

    def __repr__(self):
        return f'<Vacuum:<{self.dict[self.v]}>, Room:<{self.dict[self.room["l"]]}, {self.dict[self.room["r"]]}>>'

    def action(self, action=None):
        action = action.upper()
        if action == 'L':
            self.v = 'l'
        if action == 'R':
            self.v = 'r'
        if action == 'S':
            self.room[self.v] = 0
        return self

    def copy(self):
        return Env(self.room['l'], self.room['r'], self.v)

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

if __name__ == "__main__":
    a = Env()
    print("Enter the Initial Position of Vacuum (l for ",
            "left and r for right):")
    vacuum = input().rstrip()
    print("Enter the Cleaniness of the Left and Right Room:")
    print("0 0 = Clean Clean\n0 1 = Clean Dirty\n1 0 = Dirty Clean\n1 1 = Dirty Dirty")
    l, r = map(int, input().split())
    env = Env(l, r, vacuum)
    while(True):
        env.actionSpace()
        print("Enter the action to take:")
        action = input().rstrip()
        env.action(action)
