class Validator:

    def validuj_heslo(self, heslo):
        if len(heslo) < 5:
            return False

        for char in heslo:
            if char.isnumeric():
                return True
        return False