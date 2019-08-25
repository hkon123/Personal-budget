

class Asset(object):
    total_assets = 0

    def __init__(self, origin, value):
        self.origin = origin
        self.value = value
        self.update_class()

    def update_class(self):
        Asset.total_assets += self.value
