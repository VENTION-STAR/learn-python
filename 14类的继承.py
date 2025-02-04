class Employee :
    def __init__(self,name,staff_id):
        self.name = name
        self.id = staff_id
    def print_info(self):
        print(f'姓名：{self.name}\n工号：{self.id}\n')
class FullTimeEmployee(Employee) :
    def __init__(self,name,staff_id,monthly_salary):
        super().__init__(name,staff_id)
        self.monthly_salary = monthly_salary
    def calculate_monthly_pay(self):
        return self.monthly_salary

class PartTimeEmployee(Employee) :
    def __init__(self,name,staff_id,daily_salary,work_days):
        super().__init__(name,staff_id)
        self.daily_salary = daily_salary
        self.work_days = work_days
    def calculate_monthly_pay(self):
        return self.work_days*self.daily_salary
staff_1 = FullTimeEmployee('冯文星','001',6500)
staff_1.print_info()
print(f'{staff_1.name}的月薪为：{staff_1.calculate_monthly_pay()}元\n')
staff_2 = PartTimeEmployee('贺誉','002',200,15)
staff_2.print_info()
print(f'{staff_2.name}的月薪为：{staff_2.calculate_monthly_pay()}元')