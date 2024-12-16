class Employee:
    def __init__(self, name, position, hourly_rate):
        self.name = name
        self.position = position
        self.hourly_rate = hourly_rate
        self.hours_worked = 0
        self.bonus =0

    def add_hours(self, hours):
        self.hours_worked += hours

    def add_bonus(self, bonus_amount):
        self.bonus += bonus_amount

    def calculate_regular_pay(self):
        regular_hours = min(self.hours_worked, 40)
        return regular_hours * self.hourly_rate

    def calculate_overtime_pay(self):
        overtime_hours = max(self.hours_worked - 40, 0)
        return overtime_hours * self.hourly_rate * 1.5

    def calculate_gross_pay(self):
        return self.calculate_regular_pay() + self.calculate_overtime_pay() + self.bonus

    def calculate_monthly_salary(self):
        return 4 * self.calculate_gross_pay()

    def calculate_tax(self):
        monthly_salary = self.calculate_monthly_salary()
        return monthly_salary * 0.08

    def calculate_net_pay(self):
        monthly_salary = self.calculate_monthly_salary()
        tax = self.calculate_tax()
        return monthly_salary - tax


# Function to display payroll
def display_payroll(employees):
    print("\nPayroll Summary:")
    print("=" * 50)
    for employee in employees:
        regular_pay = employee.calculate_regular_pay()
        overtime_pay = employee.calculate_overtime_pay()
        gross_pay = employee.calculate_gross_pay()
        monthly_salary = employee.calculate_monthly_salary()
        pf = employee.calculate_tax()
        net_pay = employee.calculate_net_pay()

        print(f"Name: {employee.name}")
        print(f"Position: {employee.position}")
        print(f"  Regular Pay: ${regular_pay:.2f}")
        print(f"  Overtime Pay: ${overtime_pay:.2f}")
        print(f"  Bonus: ${employee.bonus:.2f}")
        print(f"  Weekly Gross Pay: ${gross_pay:.2f}")
        print(f"  Monthly Salary: ${monthly_salary:.2f}")
        print(f"  tax Deduction: ${pf:.2f}")
        print(f"  Net Pay: ${net_pay:.2f}")
        print("-" * 50)


# Employee list
employees = [
    Employee("Premkumar", "Manager", 20.0),
    Employee("Bhuvaneswaran", "Assistant Manager", 15.0),
    Employee("Chandran", "Team Lead", 25.0),
    Employee("Duraimanickam", "Manager", 30.0),
    Employee("Elakiya", "Junior Manager", 45.0),
]

# Add hours and bonuses
employees[0].add_hours(45)
employees[0].add_bonus(100)

employees[1].add_hours(38)
employees[1].add_bonus(50)

employees[2].add_hours(50)
employees[2].add_bonus(200)

employees[3].add_hours(55)
employees[3].add_bonus(150)

employees[4].add_hours(60)
employees[4].add_bonus(100)

# Display the payroll
display_payroll(employees)