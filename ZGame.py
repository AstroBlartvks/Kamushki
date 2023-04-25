class ZGame:
    def __init__(self):
        self.stacks = []
        self.finish = 0
        self.rules = []
        self.history = []
        self.timer = -1
        self.players = []
        self.now_turn = 0
    

    def create_rule(self, operator: str, number: int):
        if operator == "+":
            return lambda x: x + number
        else:
            return lambda x: x * number


    def create_game(self, stacks: list, finish: int, rules: list, timer: int = -1):
        self.stacks = stacks
        self.finish = finish
        self.rules = rules
        self.history = []
        self.timer = timer
        self.players = []
        self.now_turn = 0
    
    
    def add_player(self, PlayerNickName: str):
        self.players.append(PlayerNickName)
    

    def player_turn(self, rule: int, to_stack: int):
        self.stacks[to_stack] = self.rules[rule](self.stacks[to_stack])
        self.history.append((self.players[self.now_turn % len(self.players)], self.stacks[to_stack]))
        self.now_turn += 1


    def who_won(self):
        if sum(self.stacks) >= self.finish: return True, self.history[-1][0]
        else: return False, None

        
