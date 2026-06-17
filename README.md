# Employee Advance Eligibility and Policy Assistant

## Project Overview
This project is a simple prototype system that evaluates employee eligibility for advance salary requests.  
It applies business rules to check eligibility, calculate fees, VAT, and total payable amount based on company policy.

## Features
- Load employee data from CSV files
- Check employee eligibility:
  - Company status (active/ Not active)
  - Maximum advance limit (50% of net salary)
  - Monthly request restriction
  - Contract validity (minimum 30 days)
- Calculate:
  - Service fee
  - Transaction fee
  - VAT (15%)
  - Total payable amount

## Project Structure
project/
│── app.py  
│── data/  
    │── customers.csv  
    │── requests.csv  

## How to Run
1. Install dependencies:
pip install pandas

2. Run the program:
python app.py

3. Enter:
- Customer ID
- Advance amount

## Business Rules
- Only active company employees are eligible
- Maximum advance = 50% of net salary
- Only one approved/confirmed request per month
- Contract must be valid for at least 30 days
- VAT = 15% of service fee

## Technologies Used
- Python
- Pandas
- DateTime

## Author
Razan Albishri
