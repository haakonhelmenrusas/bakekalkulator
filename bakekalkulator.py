class Bakekalkulator:
    """ En klasse som tar inn antall porsjoner oppskriften gir, ingredienser og ønsket antall porsjoner, og returnerer en ingrediensliste med ønsket antall porsjoner """
    def __init__(self, porsjonerInn, ingredienser, onsketAntallPorsjoner):
        self.porsjonerInn = porsjonerInn
        self.ingredienser = ingredienser
        self.onsketAntallPorsjoner = onsketAntallPorsjoner

    def omdanningsfaktor(self):
        return self.onsketAntallPorsjoner / self.porsjonerInn