class Orange:
    def __init__(self, weight, storage):
        self.weight = weight
        self.storage = storage

    def isAvailable(self):
        return self.storage > 0


orange = Orange(200, 20)

print(f"Weight: {orange.weight}")
print(f"Storage: {orange.storage}")
print(f"Is Available: {orange.isAvailable()}")
