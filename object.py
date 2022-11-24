player = player(20,11,50)
teki = teki(hp=1000000)
player.attack(teki)

class Teki():
    
    def __init__(self,hp,speed,kasikosa) -> None:
        self.hp = 10
        self.speed = 0.1
        
    def attack(self):
        if self.hp<=0:
            print("YOU WIN!")
        
    def get_damage(self):
        self.hp-=23  

class Player():
    
    def __init__(self,hp,speed,kasikosa) -> None:
        self.hp = hp
        self.speed = speed
        self.kasikosa = kasikosa
        
    def attakck(self,enemy_object: Teki):
        player
        
    def die(self)
    sel.hp = 0
    print("!!Game Over!!")   





