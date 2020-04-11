import os
import csv 

csvpath=os.path.join('..','Resources','budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    month = []
    revenue = []
    revenue_change = []
    monthly_change = []
    
    print(f"Header: {csv_header}")               
       
    for row in csvreader:
        month.append(row[0])
        revenue.append(row[1])
    print(len(month))
 
    revenue_int = map(int,revenue)
    total_revenue = (sum(revenue_int))
    print(total_revenue)

    i = 0
    for i in range(len(revenue) - 1):
        profit_loss = int(revenue[i+1]) - int(revenue[i])
 
        revenue_change.append(profit_loss)
    Total = sum(revenue_change)
    
    monthly_change = Total / len(revenue_change)
    print(monthly_change)
    
    

    profit_increase = max(revenue_change)
    print(profit_increase)
    k = revenue_change.index(profit_increase)
    month_increase = month[k+1]
    

    profit_decrease = min(revenue_change)
    print(profit_decrease)
    j = revenue_change.index(profit_decrease)
    month_decrease = month[j+1]





output = (
f'Financial Analysis \n'
f'---------------------------- \n'

f"Total number of months: " + str(len(month)

f"Total Revenue in period: $ " + str(total_revenue)
      
f"Average monthly change in Revenue : $" + str(monthly_change)

f"Greatest Increase in Profits: {month_increase} (${profit_increase})"

f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})")

print(output)

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
