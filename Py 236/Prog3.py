# suppose u put 1 rs in bank on 1st day(monday) and every day from next day(tue to sun) u put in 1rs more than before and on every subsicuent monday you put 1 rs more tha last monday if we have number n find total amount of money you will have in the bank on nth day

def cal_amount(n):
    amount = n
    daily_deposit = 1
    monday_deposit = 1
    
    for day in range(1, n):
        amount += daily_deposit
        
        if day % 7 == 0:
            amount += monday_deposit
            monday_deposit += 1
        
        daily_deposit += 1
    
    print(amount)

cal_amount(17)