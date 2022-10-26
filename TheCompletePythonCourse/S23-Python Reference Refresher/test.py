# class Address:
#     def __init__(self, street, city, state, zipcode, street2=''):
#         self.street = street
#         self.street2 = street2
#         self.city = city
#         self.state = state
#         self.zipcode = zipcode
#
#     def __str__(self):
#         lines = [self.street]
#         if self.street2:
#             lines.append(self.street2)
#         lines.append(f'{self.city}, {self.state}, {self.zipcode}')
#         return '\n'.join(lines)
#
#
# class PayrollSystem:
#     def calculate_payroll(self, employees):
#         print('Calculating Payroll')
#         print('===================')
#         for employee in employees:
#             print(f'Payroll for: {employee.id} - {employee.name}')
#             print(f'- Check amount: {employee.calculate_payroll()}')
#             if employee.address:
#                 print(' - Sent to:')
#                 print(employee.address)
#             print('')
#
#
# class Employee:
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
#         self.address = None
#
#
# class SalaryEmployee(Employee):
#     def __init__(self, id, name, weekly_salary):
#         super().__init__(id, name)
#         self.weekly_salary = weekly_salary
#
#     def calculate_payroll(self):
#         return self.weekly_salary
#
#
# class HourlyEmployee(Employee):
#     def __init__(self, id, name, hours_worked, hour_rate):
#         super().__init__(id, name)
#         self.hours_worked = hours_worked
#         self.hour_rate = hour_rate
#
#     def calculate_payroll(self):
#         return self.hours_worked * self.hour_rate
#
#
# class ComissionEmployee(SalaryEmployee):
#     def __init__(self, id, name, weekly_salary, commission):
#         super().__init__(id, name, weekly_salary)
#         self.commission = commission
#
#     def calculate_payroll(self):
#         fixed = super().calculate_payroll()
#         return fixed + self.commission
#
#
# class Manager(SalaryEmployee):
#     def work(self, hours):
#         print(f'{self.name} screams and yells for {hours} hours.')
#
#
# class Secretary(SalaryEmployee):
#     def work(self, hours):
#         print(f'{self.name} expends {hours} hours doing office paperwork.')
#
#
# class SalesPerson(ComissionEmployee):
#     def work(self, hours):
#         print(f'{self.name} expends {hours} hours on the phone.')
#
#
# class FactoryWorker(HourlyEmployee):
#     def work(self, hours):
#         print(f'{self.name} manufactures gadgets for {hours} hours.')
#
#
# class ProductivitySystem:
#     @staticmethod
#     def track(employees, hours):
#         print('Tracking Employee Productivity')
#         print('==============================')
#         for employee in employees:
#             employee.work(hours)
#         print('')
#
#
# class TemporarySecretary(Secretary, HourlyEmployee):
#     def __init__(self, id, name, hours_worked, hour_rate):
#         HourlyEmployee.__init__(self, id, name, hours_worked, hour_rate)
#
#     def calculate_payroll(self):
#         return HourlyEmployee.calculate_payroll(self)
#
# manager = Manager(1, 'Mariy Poppins', 3000)
# manager.address = Address(
#     '121 Admin Rd',
#     'Concord',
#     'NH',
#     '03301'
# )
# secretary = Secretary(2, 'John Smith', 1500)
# secretary.address = Address(
#     '67 Paperwrok Ave.',
#     'Manchester',
#     'NH',
#     '03101'
# )
# sales_guy = SalesPerson(3, 'Kevin Bacon', 1000, 250)
# factory_worker = FactoryWorker(2, 'Jane Doe', 40, 15)
# temporary_secretary = TemporarySecretary(5, 'Robin Williams', 40, 9)
#
# employees = [
#     manager,
#     secretary,
#     sales_guy,
#     factory_worker,
#     temporary_secretary,
# ]
#
# productivity_system = ProductivitySystem()
# productivity_system.track(employees, 40)
# payroll_system = PayrollSystem()
# payroll_system.calculate_payroll(employees)






def mon_decorateur(fonction):
    """Premier exemple de décorateur"""
    print("Notre décorateur est appelé avec en paramètre la fonction {0}".format(fonction))
    return fonction

@mon_decorateur
def salut():
    """Fonction modifiée par notre décorateur"""
    print("Salut !")

