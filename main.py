import csv
from pathlib import Path

#list of loan costs
loan_costs = [500, 600, 200, 1000, 450]

#number of loans calculated and printed
number_of_loans = len(loan_costs)
print(f"Number of loans: {number_of_loans}")

#sum of loans calculated and printed
loan_totals = sum(loan_costs)
print(f"Total amount of all loans: ${loan_totals: .2f}")

#average loan amount calculated and printed
average_loan_amount = loan_totals / number_of_loans
print(f"Average loan amount: ${average_loan_amount: .2f}")

#given loan data
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# future value and remaining months on the loan obtained from given loan data, results printed
future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")
print(future_value)
print(remaining_months)

# calculation of present value using given loan data
annual_discount_rate = .20
present_value = future_value / (1 + annual_discount_rate/12) ** remaining_months

# buyer recommendation based on loan's present value with respect to loan's current cost, results printed
if present_value >= loan["loan_price"]:
    print("The loan is worth buying at current cost")
else:
    print("The loan is too expensive and not worth the price")

# new loan data
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# function to calculate present value
def calculate_present_value(future_value, remaining_months, annual_discount_rate):
    return present_value


# calcuation of present value for new loan data using calculate present value function
annual_discount_rate = 0.20
present_value = calculate_present_value(
    new_loan["future_value"],
    new_loan["remaining_months"],
    annual_discount_rate)
print(f"The present value of the loan is: ${present_value: .2f}")


"""Part 4: Conditionally filter lists of loans.

In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than 500
    b. If the loan_price is less than 500 then append that loan to the `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# @TODO: Create an empty list called `inexpensive_loans`
# YOUR CODE HERE!

# @TODO: Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
# YOUR CODE HERE!

# @TODO: Print the `inexpensive_loans` list
# YOUR CODE HERE!


"""Part 5: Save the results.

Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

    Hint: Refer to the official documentation for the csv library.
    https://docs.python.org/3/library/csv.html#writer-objects

"""

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# @TODO: Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
# YOUR CODE HERE!

