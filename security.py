class Security:

    def __init__(self,data):
        self.text=data

    def alert(self):
        if '$' in self.text:
            G= self.text.rfind("G")
            T=self.text.rfind("T")
            if G>T:
                if self.text.index('$') in range(T,G):
                    print("ALARM")
                else:
                    print("quiet")
            else:
                if self.text.index('$') in range(G,T):
                    print("ALARM")
                else:
                    print("quiet")

data = input()
secure=Security(data)
secure.alert()
