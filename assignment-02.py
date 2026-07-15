class Orange:
    def __init__(self, weight: float, storage: int) -> None:
        self.weight: float = weight
        self.storage: int = storage

    def isAvailable(self) -> bool:
        return self.storage > 0


orange: Orange = Orange(200, 20)

print(f"Weight: {orange.weight}")
print(f"Storage: {orange.storage}")
print(f"Is Available: {orange.isAvailable()}")
