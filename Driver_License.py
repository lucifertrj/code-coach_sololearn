class Driver:

    def __init__(self,name,agents,queue):
        self.name = name
        self.agents = agents
        self.members = queue
    
    def total_time(self):
        result = self.members.index(self.name)+1
        if self.agents == 0:
            return 0
        elif result == self.agents:
            return 20
        else:
            return abs((result*20)-((self.agents-1)*20))

name = input("").upper()
agents = int(input(""))
queue = input("").upper().split()
queue.append(name)
queue.sort()

dl = Driver(name,agents,queue)
print(dl.total_time())