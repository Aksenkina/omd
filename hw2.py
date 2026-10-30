import csv

INPUT_FILE = 'Corp_Summary.csv'
OUTPUT_FILE = 'report.csv'

def read_csv(filename):
    employee_data = []
    with open (filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)

        for row in reader:
            employee = {
                'name': row[0],
                'department': row[1],
                'team': row[2],
                'position': row[3],
                'score': float(row[4]),
                'salary': int(row[5])
            }
            employee_data.append(employee)
    
    # Проверка сырых данных
    # for emp in employee_data:
        # print(emp)
    return employee_data

# read_csv(INPUT_FILE)

def hierarchy(data):  # Функция для отчета 1: Иерархия (показывает для каждого департамента, какие команды в него входят)
    department_teams = {}

    for employee in data:
        department = employee['department']
        team = employee['team']

        if department not in department_teams:
            department_teams[department] = []

        if team not in department_teams[department]:
            department_teams[department].append(team)
    
    print('Иерархия департаментов:')
    for department, teams in department_teams.items():
        print(f'{department}: {', '.join(teams)}')

def summary(data):  # Функция для отчета 2: Сводка по департаментам (показывает название, сколько человек, мин. и макс. зарплату, среднюю зп по каждому департаменту)
    department_summary = {}

    for employee in data:
        department = employee['department']
        salary = employee['salary']

        if department not in department_summary:
            department_summary[department] = {
                'count': 0,
                'min_salary': salary,
                'max_salary': salary,
                'total_salary': 0
            }

        department_summary[department]['count'] += 1
        department_summary[department]['total_salary'] += salary

        if salary < department_summary[department]['min_salary']:
            department_summary[department]['min_salary'] = salary
        if salary > department_summary[department]['max_salary']:
            department_summary[department]['max_salary'] = salary
    
    print('Сводка по департаментам:')
    for department, summary in department_summary.items():
        avg_salary = summary['total_salary'] / summary['count']
        print(f"{department}: {summary['count']} чел., мин. ЗП: {summary['min_salary']}, макс. ЗП: {summary['max_salary']}, средняя ЗП: {avg_salary:.2f}")

def summary_csv(data):  # Функция для отчета 3: Сводка по департаментам (как в отчете 2), записанная в csv-файл
    department_summary = {}
    
    for employee in data:
        department = employee['department']
        salary = employee['salary']
    
        if department not in department_summary:
            department_summary[department] = {
                'count': 0,
                'min_salary': salary,
                'max_salary': salary,
                'total_salary': 0
            }
    
        department_summary[department]['count'] += 1
        department_summary[department]['total_salary'] += salary
    
        if salary < department_summary[department]['min_salary']:
            department_summary[department]['min_salary'] = salary
        if salary > department_summary[department]['max_salary']:
            department_summary[department]['max_salary'] = salary
    with open(OUTPUT_FILE, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Департамент', 'Количество', 'Мин. ЗП', 'Макс. ЗП', 'Средняя ЗП'])

        for department, summary in department_summary.items():
            avg_salary = summary['total_salary'] / summary['count']
            writer.writerow([department, summary['count'], summary['min_salary'], summary['max_salary'], f'{avg_salary:.2f}'])

    print(f'Отчет сохранен в {OUTPUT_FILE}')

def main(report_number):
    data = read_csv(INPUT_FILE)

    if report_number == 1:
        hierarchy(data)
    elif report_number == 2:
        summary(data)
    elif report_number == 3:
        summary_csv(data)
    else:
        print('Такого отчета нет. Введите 1, 2 или 3.')
if __name__ == "__main__":
    main(3)

