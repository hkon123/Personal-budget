


class Expence(object):
    total_expence = 0
    biggest_expence = ["source",0]

    def __init__(self, source, amount):
        self.source = source
        self.amount = amount
        self.update_class()

    def update_class(self):
        Expence.total_expence +=self.amount
        if Expence.biggest_expence[1] > self.amount:
            Expence.biggest_expence[0] = self.source
            Expence.biggest_expence[1] = self.amount
