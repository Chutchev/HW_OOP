# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла


class Worker(object):

    def __init__(self, name, second_name, salary, postOffice, hour):
        self.name = name
        self.second_name = second_name
        self.salary = salary
        self.postOffice = postOffice
        self.normal_hour = hour
        self._hour = 0
        self._salary = 0

    def __str__(self):
        return f"Рабочий: {self.name} {self.second_name}. Зарплата по договору: {self.salary}. Должность: " \
               f"{self.postOffice}. Норма часов: {self.normal_hour}. Отработано: {self._hour}. Зарплата в этом" \
               f" месяце: {self._salary}"

    def add_hour_for_worker(self, hour):
        self._hour = hour

    def real_salary(self):
        self._salary = float(self.salary)/float(self.normal_hour) * float(self._hour)



def main():
    workers = fill_list_workers()
    for worker in workers:
        worker.real_salary()
        print(worker)


def fill_list_workers():
    workers = []
    count = 0
    with open('.\\data\\workers', 'r', encoding='utf-8') as file:
        for line in file:
            if count > 0:
                string_line = line.split()
                workers.append(Worker(string_line[0], string_line[1], string_line[2], string_line[3], string_line[4]))
            count += 1
    add_hours(workers)
    return workers


def add_hours(workers):
    with open('.\\data\\hours_of', 'r', encoding='utf-8') as file:
        for line in file:
            string_line = line.split()
            for worker in workers:
                if worker.name == string_line[0] and worker.second_name == string_line[1]:
                    worker.add_hour_for_worker(string_line[2])


if __name__ == '__main__':
    main()
