class Character:
    def __init__(self, name: str, max_hp: int):
        if type(max_hp) is not int or max_hp <= 0:
            raise ValueError("max_hp має бути додатним цілим числом")
        self.name = name
        self.__max_hp = max_hp
        self.__hp = max_hp

    @property
    def hp(self) -> int:
        return self.__hp

    @property
    def max_hp(self) -> int:
        return self.__max_hp

    def take_damage(self, amount: int) -> None:
        if type(amount) is not int or amount < 0:
            raise ValueError("Шкода має бути невід'ємним цілим числом")
        self.__hp = max(0, self.__hp - amount)

    def heal(self, amount: int) -> None:
        if type(amount) is not int or amount < 0:
            raise ValueError("Лікування має бути невід'ємним цілим числом")
        self.__hp = min(self.__max_hp, self.__hp + amount)

    def is_alive(self) -> bool:
        return self.__hp > 0


if __name__ == "__main__":
    hero = Character("Dragon", 100)
    hero.take_damage(30)
    print(hero.hp)
    hero.heal(100)
    print(hero.hp)
    hero.take_damage(200)
    print(hero.hp, hero.is_alive())
