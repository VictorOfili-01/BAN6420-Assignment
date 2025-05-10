import random

# Create a list of 400 workers dynamically
employees = [f"employee {i+1}" for i in range(400)]

# Generate payment slips and assign levels based on salary
for employee in employees:
    try:
        salary = random.randint(7500, 30000)  # Random salary for each employee
        salary_in_dollars = f"${salary:,}"  # Format salary with dollar sign and commas
        print(f"Has payment slip for {employee} who earns {salary_in_dollars} been generated?: YES")


        if 10000 < salary < 20000:  # Salary range for employee who earns between 10,000 and 20,000
            employee_grade = "A1"
            print(f"Level assigned for {employee} who earns {salary_in_dollars}: {employee_grade}")
        elif 7500 < salary < 30000: # Salary range for female employee who earns between 7,500 and 30,000
            employee_level = "A5-F"
            print(f"Level assigned for female {employee} who earns {salary_in_dollars}: {employee_level}")
        else:
            print(f"Level not assigned for {employee} who earns {salary_in_dollars}")
    except Exception as e:
        print(f"Error processing {employee}: {e}")
