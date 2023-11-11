class Person:
    """
     Класс описывающий объекты Человек
    """
    def __init__(self, name, age, salary):
        """
        Инициализация класса Person
        :param name: имя человека
        :param age: возраст человека
        :param salary: зарплата человека
        """
        self.name = name
        self.age = age
        self.salary = salary

    def hire(self):
        """
        Функция приёма сотрудника на работу
        """
        print(f"{self.name} нанят.")

    def show(self):
        """
        Функция, для вывода информаци о сотруднике на экран
        """
        print(f"Работник: {self.name}, {self.age}, {self.salary},")


class HR(Person):
    """
    Класс описывающий кадровых служащих
    """
    def __init__(self, name, age, salary, post):
        """
        Инициализация класса HR
        :param name: имя человека
        :param age: возраст человека
        :param salary: зарплата человека
        :param post: должность кадирового служащего
        """
        super().__init__(name, age, salary)
        self.post = post

    def hire(self):
        """
         Функция приёма на работу кадрового служащего
        """
        super().hire()
        print(f"{self.name} работает на должности: {self.post}.")

    def show(self):
        """
        Функция, для вывода информаци о сотруднике на экран
        """
        super().show()
        print(f"{self.name}: {self.post}")


class Engineer(Person):
    """
    Класс описывающий инженеров
    """
    def __init__(self, name, age, salary, specialization):
        """
        Инициализация класса Engineer
        :param name: имя человека
        :param age: возраст человека
        :param salary: зарплата человека
        :param specialization: специализация инженера
        """
        super().__init__(name, age, salary)
        self.specialization = specialization

    def hire(self):
        """
         Функция приёма на работу инженера
        """
        super().hire()
        print(f"{self.name} работает на должности: {self.specialization} инженер.")

    def show(self):
        """
        Функция, для вывода информаци о сотруднике на экран
        """
        super().show()
        print(f"{self.name}: {self.specialization} инженер")


class Admin(Person):
    """
    Класс описывающий административный состав
    """
    def __init__(self, name, age, salary, role):
        """
        Инициализация класса Admin
        :param name: имя человека
        :param age: возраст человека
        :param salary: зарплата человека
        :param role: административная должность служащего
        """
        super().__init__(name, age, salary)
        self.role = role

    def hire(self):
        """
        Функция приёма на работу административного служащего
        """
        super().hire()
        print(f"{self.name} работает на должности: {self.role}.")

    def show(self):
        """
        Функция, для вывода информаци о сотруднике на экран
        """
        super().show()
        print(f"{self.name}: {self.role}")


registry = []


def main():
    """
    Функция выполняющая поставленную задачу, а также инизиализирующая примитивный интерфейс
    """
    while True:
        print("Меню:")
        print("1. Создать нового кадрового служащего")
        print("2. Создать нового инженера")
        print("3. Создать нового административного служащего")
        print("4. Вывести содержимое объектов")
        print("5. Вывести представление конкретного объекта")
        print("6. Завершить работу")

        choice = input("Выберите пункт меню: ")

        if choice == "1":
            name = input("Введите ФИО работника: ")
            while True:
                try:
                    age = int(input("Введите возраст работника: "))
                    break
                except ValueError as a:
                    print("Введён неверный символ, повторите попытку")
            while True:
                try:
                    salary = int(input("Введите зарплату работника: "))
                    break
                except ValueError as a:
                    print("Введён неверный символ, повторите попытку")
            post = input("Введите должность работника: ")
            hr = HR(name, age, salary, post)
            registry.append(hr)
            hr.hire()
        elif choice == "2":
            name = input("Введите ФИО работника: ")
            while True:
                try:
                    age = int(input("Введите возраст работника: "))
                    break
                except ValueError as a:
                    print("Введён неверный символ, повторите попытку")
            while True:
                try:
                    salary = int(input("Введите зарплату работника: "))
                    break
                except ValueError as a:
                    print("Введён неверный символ, повторите попытку")
            specialization = input("Введите специализацию инженера(Прилагательное): ")
            engineer = Engineer(name, age, salary, specialization)
            registry.append(engineer)
            engineer.hire()

        elif choice == "3":
            name = input("Введите ФИО работника: ")
            while True:
                try:
                    age = int(input("Введите возраст работника: "))
                    break
                except ValueError as a:
                    print("Введён неверный символ, повторите попытку")
            while True:
                try:
                    salary = int(input("Введите зарплату работника: "))
                    break
                except ValueError as a:
                    print("Введён неверный символ, повторите попытку")
            role = input("Введите должность работника: ")
            admin = Admin(name, age, salary, role)
            registry.append(admin)
            admin.hire()

        elif choice == "4":
            if len(registry) == 0:
                print("\nРеестр пуст.")
            else:
                for index, obj in enumerate(registry):
                    print(f"\n{index + 1}: {obj.show()}")

        elif choice == "5":
            if len(registry) == 0:
                print("\nРеестр пуст.")
            else:
                index = int(input("\nВведите индекс объекта: ")) - 1
                if 0 <= index < len(registry):
                    print(registry[index].show())
                else:
                    print("\nНеверный индекс объекта.")

        elif choice == "6":
            break

        else:
            print("\nТакой номер отсутствует. Попробуйте снова.")


if __name__ == "__main__":
    main()
