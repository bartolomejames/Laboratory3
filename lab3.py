def loan_eligibility():
    try:
       
        salary = float(input("Enter your monthly salary: "))
        loan_amount = float(input("Enter the loan amount requested: "))

        
        if salary >= 30000:
            
            if loan_amount <= 10 * salary:
                print("You are eligible for the loan.")

               
                months = int(input("Enter the number of months to pay back the loan: "))

                
                total_amount_with_interest = loan_amount * 1.10
                monthly_payment = total_amount_with_interest / months

                
                print(f"Loan approved with a 10% interest increase.")
                print(f"Total loan amount with interest: {total_amount_with_interest:.2f}")
                print(f"Your monthly payment for {months} months will be: {monthly_payment:.2f}")
            else:
                
                print(f"Loan request too high. The loan amount exceeds 10 times your monthly salary.")
        else:
            
            print(f"Your salary is too low to qualify for the loan. Minimum salary required is 30,000.")
    
    except ValueError:
        
        print("Invalid input. Please enter a valid number for salary and loan amount.")
loan_eligibility()