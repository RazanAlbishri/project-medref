#import liblaries
import pandas as pd
from datetime import datetime

#read customers data
customers = pd.read_csv("data/customers.csv")
#read requests data
requests = pd.read_csv("data/requests.csv")


## P1 - Company Status
'''
Only employees under active partner 
companies are allowed to request an advance.
'''
customer_id = input("Enter your ID:")
amount = float(input("Enter advance amount: "))

customer = customers[customers["customer_id"] == customer_id]

if len(customer) == 0:
    print("Customer not found")

else:
    customer = customer.iloc[0]

    if customer["company_status"] != "active":
        print("Company not active")
    else:
        print("Company is active")

    ## P2 - Advance Limit
    '''
    The maximum advance amount is 50% of the 
    employee net salary.
    '''
    max_limit = customer["net_salary"] * 0.50
    print("The maximum advance Limit:", max_limit)

    ## P3 - Monthly Request Rule
    #An employee cannot have more than one approved or confirmed request in the same calendar month.
    request_date = datetime.today()
    requests["request_date"] = pd.to_datetime(requests["request_date"])

    employee_requests = requests[
        (requests["customer_id"] == customer_id) &
        (requests["state"].isin(["approved", "confirmed"])) &
        (requests["request_date"].dt.month == request_date.month) &
        (requests["request_date"].dt.year == request_date.year)
    ]

    if len(employee_requests) > 0:
        print("Already has request this month")

    ## P4 - Contract Expiry Rule
    # The employee contract must be valid for at least 30 days from the request date.
    contract_expiry = pd.to_datetime(customer["contract_expiry_date"])
    days_left = (contract_expiry - request_date).days

    if days_left < 30:
        print("Not Allowed : Contract expires in less than 30 days")
    else:
        print("Allowed : Contract expires in greater than 30 days")

    ## P5 - Fee Rules
    salary = customer["net_salary"]
    # If net salary is between 1 and 3000 SAR:- service_fee = 21 SAR- transaction_fee = 2 SAR
    if salary >= 1 and salary <= 3000:
        service_fee = 21
        transaction_fee = 2
    
    # If net salary is between 3000.01 and 7000 SAR:- service_fee = 39 SAR- transaction_fee = 3 SAR
    elif salary >= 3000.01 and salary <= 7000:
        service_fee = 39
        transaction_fee = 3
    
    # If net salary is above 7000 SAR:- service_fee = 59 SAR- transaction_fee = 5 SAR
    elif salary > 7000:
        service_fee = 59
        transaction_fee = 5
    
    # VAT is 15% of the service fee only.
    vat = service_fee * 0.15
    # Total payable = requested amount + service fee + transaction fee + VAT.
    total_payable = amount + service_fee + transaction_fee + vat

    print("Service Fee = ", service_fee)
    print("Transaction Fee = ", transaction_fee)
    print("VAT = ", round(vat, 2))
    print("Total Payable = ", round(total_payable, 2))