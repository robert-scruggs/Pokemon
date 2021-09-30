class Pokemon:
    def __init__(self,attack,defense,name):
        self.attack = attack
        self.defense = defense
        self.name = name

    def __repr__(self):
        return str(self.defense)

    def walking(self):
        print('Walking...')

    def running(self):
        print('Running...')
