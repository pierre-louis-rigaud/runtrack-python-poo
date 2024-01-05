import random
class Personnage:
    def __init__(self, nom, maxVie) -> None:
        self._nom = nom
        self._maxVie = maxVie
        self._vie = self._maxVie
        self._estVivant = True
        
    def predreDegats(self,degats):
        if self._vie > degats:
            self._vie -= degats
            print(f"{self._nom} possède maintenant {self._vie} points de vie\n")
        else:
            self._estVivant = False
            print(f"{self._nom} possède maintenant 0 points de vie\n")
        
    def attaquer(self, ennemi):
        degats = random.randint(0,20)
        print(f"{self._nom} a attaqué et à fait {degats} points de degats")
        ennemi.predreDegats(degats)