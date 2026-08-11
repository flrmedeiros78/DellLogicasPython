from datetime import date

class Gato:
    """Um bicho"""
    def __init__(self, nome, sexo, peso, nasc):
        self.nome = nome
        self.sexo = sexo
        self.peso = peso
        self.nasc = nasc

    def __str__(self):
        return '{}, sexo{}, {}kg, nasceu em {}'.format(self.nome, self.sexo, self.peso, self.nasc)

    def idade(self):
        """Idade do bicho, em anos (ponto-flutuante)."""
        return (date.today() - self.nasc).days / 365


def repartir_por_idade(gatos, anos_de_idade):
    """Reparte uma lista de gatos em um par de listas: a dos gatos mais jovens que a idade informada e a dos mais velhos."""
   
    gatos_jovens = []
    gatos_velhos = []
    for g in gatos:
        if g.idade() < anos_de_idade:
            gatos_jovens.append(g)
        else:
            gatos_velhos.append(g)
    return gatos_jovens, gatos_velhos

um_gato = Gato('Zarabi', ' f', 4.5, date(2010, 9, 4))
print(um_gato)