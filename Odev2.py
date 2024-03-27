class Personel:
    def __init__(self, name, department, year, salary):
        self.name = name
        self.department = department
        self.year = year
        self.salary = salary


class Firm:
    def __init__(self):
        self.personel_list = []

    def add_personel(self, personel):
        self.personel_list.append(personel)
        print("Personel added.")

    def list_personel(self):
        for personel in self.personel_list:
            print(
                f"Name:{personel.name}\nDepartmant:{personel.department}\nYear:{personel.year}\nSalary:{personel.salary}$\n------------------------")

    def raise_salary(self, personel, increase_rate):
        increase = increase_rate / 100
        personel.salary += personel.salary * increase

    def remove_personel(self, personel):
        self.personel_list.remove(personel)


if __name__ == "__main__":
    firm = Firm()

    personel1 = Personel("Mert Töke", "IT", "2023", 25000)
    personel2 = Personel("Furkan Akınalp", "Cyber Security", "2023", 22500)
    personel3 = Personel("Charles", "IT", "2020", 43000)

    firm.add_personel(personel1)
    firm.add_personel(personel2)
    firm.add_personel(personel3)

    firm.list_personel()

    firm.raise_salary(personel1, 15)
    firm.raise_salary(personel2, 10)
    firm.raise_salary(personel3, 5)

    firm.remove_personel(personel3)
    firm.list_personel()
