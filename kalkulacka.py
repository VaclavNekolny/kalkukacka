class Kalkulacka:
    """
    Tohle je kalkulačka. Umí sečíst dvě čísla a dokonce umí i odečíst dvě čísla. Je prostě fakt hustá!
    :param a: první číslo (float nebo int)
    :param b: druhé číslo (float nebo int)
    :return: sečte čísla z proměnných 'a' a 'b' a vrátí výsledek
    """
    def secti(self, a,b):
        return a+b

    def odecti(self, a,b):
        return a-b

    def vynasob(self, a,b):
        return a*b