


class Income(object):
    total_income = 0

    def __init__(self, source, amount):
        self.source = source
        self.amount = amount
        self.update_class()

    def update_class(self):
        Income.total_income += self.amount
