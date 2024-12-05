basic = float(input("Enter the basic salary: "))
da = 0.97 * basic
hra = 0.57 * basic
gross_salary = basic + da + hra + 150
epf = 0.12 * basic
net_salary = gross_salary - epf - 200
print("Net salary:", net_salary)
