# Napiš třídu hráč, který bude mít dvě metody - set_score, get_score.
# První metoda nastaví hráči skóre, druhá metoda vypíše do konzole hodnotu skóre.
# Při vytváření instance třídy hráč bude zapotřebí pouze nickname hráče.


class Player:
    def __init__(self, nickname):
        self.nickname = nickname
        self.score = None

    def set_score(self, score):
        self.score = score

    def get_score(self):
        return self.score


player = Player("Kharianne")
player.set_score(35)
print(player.get_score())
