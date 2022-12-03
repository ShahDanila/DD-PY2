import doctest


class Castle:
    """
           Создание и подготовка к работе объекта "Замок"

           :param walls: Колличество стен замка
           :param towers: Колличество башен замка
           :param gates: Колличество ворот замка

           Пример:
           >>> Izengard = Castle(9, 9, 8)  # инициализация экземпляра класса
    """
    def __init__(self, walls: int, towers: int, gates: int) -> None:
        if not isinstance(walls, int):
            raise TypeError("Таких стен не бывает!")
        if walls <= 0:
            raise ValueError("Нет стен - нет замка!")
        if walls <= 2:
            raise ValueError("Мало! Надо минимум 3 стены!")
        self.walls = walls

        if not isinstance(towers, int):
            raise TypeError("Таких башен не бывает!")
        if towers <= 0:
            raise ValueError("Это замок, а не форт, без башен не обойтись!")
        if towers > walls:
            raise ValueError("У нас недостаточно стен!")
        self.towers = towers

        if not isinstance(gates, int):
            raise TypeError("Таких ворот не бывает!")
        if gates <= 0:
            raise ValueError("Ни зайти, ни выйти - это самая неприступная крепость!")
        if gates > walls:
            raise ValueError("Вы хотите из замка проходной двор сделать?!")
        self.gates = gates

    def gates_open(self) -> bool:
        """
                Функция которая проверяет открыты ли ворота

                :return: Являются ли ворота открытыми

                Пример:

                >>> Izengard = Castle(9, 9, 8)
                >>> Izengard.gates_open()
        """

        ...

    def sell_castle(self) -> int:
        """
                Функция которая продаёт замок
                :return: Стоимость замка в серебряных талерах

                Пример:

                >>> Izengard = Castle(9, 9, 8)
                >>> Izengard.sell_castle()
        """
        ...


class Village:
    """
        Создание и подготовка к работе объекта "Деревня"

        :param souls: Колличество крестьян
        :param square: Площадь деревни в гектарах

        Пример:
        >>> Malinovka = Village(325, 40, 15)  # инициализация экземпляра класса
    """
    def __init__(self, souls: int, houses: int, square: [int, float]):
        if not isinstance(souls, int):
            raise TypeError("Это же люди!")
        if souls <= 0:
            raise ValueError("Деревня не может быть пустой!")
        if souls > 1000:
            raise ValueError("Многовато будет!")
        self.souls = souls

        if not isinstance(houses, int):
            raise TypeError("Это же дома!")
        if houses <= 0:
            raise ValueError("А люди где жить будут?")
        if houses > self.souls//7:
            raise ValueError("Многовато будет!")
        self.houses = houses

        if not isinstance(square, (int, float)):
            raise TypeError("Эта деревня не на бумаге!")
        if square <= 0:
            raise ValueError("Деревня не может быть без земли")
        if square > 1000:
            raise ValueError("Многовато будет!")
        self.square = square
        ...

    def collect_taxes(self) -> int:
        """
                Функция которая собирает налоги

                :return: Налог в мешках зерна

                Пример:

                >>> Malinovka = Village(325, 40, 15)
                >>> Malinovka.collect_taxes()
        """
        ...

    def sell_village(self) -> int:
        """
                Функция которая продаёт деревню

                :return: Стоимость деревни в серебряных талерах

                Пример:

                >>> Malinovka = Village(325, 40, 15)
                >>> Malinovka.sell_village()
        """
        ...

    def fire_village(self, ruins: (int, float)) -> None:
        """
                Функция которая оставляет оккупанта без продовольствия

                :param ruins: Количество сожжённых домов
                :raise ValueError: Если количество руин больше количества домов или меньше одного


                Пример:

                >>> Malinovka = Village(325, 40, 15)
                >>> Malinovka.fire_village(20)
        """
        if not isinstance(ruins, (int, float)):
            raise TypeError("Сжечь можно только int или float количество домов")
        if ruins < 1:
            raise ValueError("Нельзя оставлять деревню врагу")
        if ruins > self.houses:
            raise ValueError("Вы перестарались")
        ...


class Peasant:
    """
            Создание и подготовка к работе объекта "Крестьянин"

            :param age: Возраст крестьянина
            :param money: Накопления крестьянина в франках
            :param bags: Запасы зерна в мешках

            Пример:
            >>> Jack = Peasant(32, 5, 20)  # инициализация экземпляра класса
    """
    def __init__(self, age: int, money: [int, float], bags: [int, float]):
        if not isinstance(age, int):
            raise TypeError("Нужен примерный возраст в int")
        if age < 0:
            raise ValueError("Так он же ещё не родился!")
        if age > 50:
            raise ValueError("Крестьяне столько не живут!")
        self.age = age

        if not isinstance(money, (int, float)):
            raise TypeError("Копить можно только в int и float")
        if money > 50:
            raise ValueError("Крестьяне столько не зарабатывают!")
        self.money = money

        if not isinstance(bags, (int, float)):
            raise TypeError("Мешки с зерном могут быть только в int и float")
        if bags < 5:
            raise ValueError("Так он помрёт с голоду и не заплатит оброк!")
        if bags > 100:
            raise ValueError("Слишком зажиточный!")
        self.bags = bags

    def pay_taxes(self, tax: (int, float)) -> [int, float]:
        """
                Функция которая платит налоги

                :return: Налог в мешках зерна

                Пример:

                >>> Jack = Peasant(32, 5, 20)
                >>> Jack.pay_taxes(10)
        """
        if not isinstance(tax, (int, float)):
            raise TypeError("Мешки с зерном могут быть только в int и float")
        if tax < 3:
            raise ValueError("Феодалу не на что будет жить!")
        if self.bags - tax < 6:
            raise ValueError("Крестьянину не на что будет жить!")
        ...

    def repair_house(self, cost: [int, float]) -> None:
        """
                Функция которая ремонтирует дом, сожжённый феодалом

                :return: Налог в мешках зерна
                :raise ValueError:

                Пример:

                >>> Jack = Peasant(32, 5, 20)
                >>> Jack.repair_house(3)
        """
        if not isinstance(cost, (int, float)):
            raise TypeError("Деньги могут быть только в int и float")
        if cost <= 0:
            raise ValueError("Ваш дом не пострадал!")
        if cost > 50:
            raise ValueError("Крстьянская халупа не может быть такой дорогой!")
        ...


if __name__ == "__main__":
    doctest.testmod()
