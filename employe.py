class Employe:

    def __init__(self, numeroPermis, nom, prenom):
        self.numeroPermis = numeroPermis
        self.nom = nom
        self.prenom = prenom
        self.voitureService = None

    def afficherInformations(self):
        print("Nom :", self.nom)
        print("Prenom :", self.prenom)

        if self.voitureService:
            print("Voiture :", self.voitureService.marque)
        else:
            print("Aucune voiture")