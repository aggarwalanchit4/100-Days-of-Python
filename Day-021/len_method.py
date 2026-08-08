# -----------------------------------------
# Challenge 1 – Implement __len__() Method
# -----------------------------------------

class Team:

def __init__(self, players):
    self.players = players
def __len__(self):
    return len(self.players)
```

players = list(input("enter players in team : ").split())
team = Team(players)
print(len(team))