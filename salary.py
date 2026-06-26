# net salary
basic = float(input("Enter basic salary: "))
da = float(input("Enter dearness allowance percentage: "))
hra = float(input("Enter house rent allowance percentage: "))
net_salary = basic + (basic * da / 100) + (basic * hra / 100)
print("Net salary is:", net_salary)
