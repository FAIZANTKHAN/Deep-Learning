import numpy as np
#This contains program on the basic of matrix
#Calculate profit/loss from revenue and expenses

revenue = np.array([[180,200,220],[24,36,40],[12,18,20]])
expenses = np.array([[80,90,100],[10,16,20],[8,10,10]])
profit=revenue-expenses
print(profit)

#Calculate total sales from units and price per unit using matrix multiplication
price_per_unit=np.array([1000,400,1200])
units = np.array([[30,40,50],[5,10,15],[2,5,7]])

print(price_per_unit*units)

#Using dot product
print(np.dot(price_per_unit,units))


#Q1)Convert USD to INR
#Q2)Calculate total flowers sale every month for divine flowers shop

#Q1)
revenues_usd = np.array([[200,220,250],[68,79,105],[110,140,180],[80,85,90]])
print(83*revenues_usd)
revenues_inr=np.dot(83,revenues_usd)#Using dot product
print(revenues_inr)

#Q2)

units_sold = np.array([[50,60,25],[10,13,5],[40,70,52]])
price_per_unit = np.array([20,30,15])

total_sales_amount=np.dot(price_per_unit,units_sold)
print(total_sales_amount)
