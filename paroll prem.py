# class employee:
#       def _init_(self,name,hourlyrate):
#               self.name=name
#               self.hourlyrate=hourlyrate
#               self.hoursworked=0
#               def addhours (self,hours):
#                       self.hoursworked+=hours
#               def calculatepay(self):
#                       return self.hourlyrate*hoursworked 
#               def resethours (self):
#                       self.hoursworked= 0

#       class Payroll:
#              def __init__(self):
#                 self.employees = {}

#                 def add_employee(self, name, hourly_rate):
#                  if name not in self.employees:
#                   self.employees[name] = Employee(name, hourly_rate)
#                  else:
#                   print(f"Employee {name} already exists.")

#                 def add_hours(self, name, hours):
#                     if name in self.employees:
#                       self.employees[name].add_hourelse:
#                       print(f"Employee {name} not found.")

#                     def generate_payroll(self):
#                       for employee in self.employees.values():
#                        pay = employee.calculate_pay()
#                        print(f"Employee: {employee.name}, Pay: ${pay:.2f}")
#                        employee.reset_hours()  # Reset hours after payroll

# # Example usage
# payroll = Payroll()
# payroll.add_employee("Alice", 20)  # $20 per hour
# payroll.add_employee("Bob", 25)    # $25 per hour
# payroll.add_employee("prem",80)

# payroll.add_hours("Alice", 40)     # Alice worked 40 hours
# payroll.add_hours("Bob", 35)       # Bob worked 35 hours
# payroll.add_hours("prem",30)

# print("Generating Payroll:")
# payroll.generate_payroll()                   
                 


         
    
