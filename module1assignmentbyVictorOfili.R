library(stringr)

# Create a list of 400 workers dynamically
employees <- paste("employee", 1:400)

# Generate payment slips and assign levels based on salary
# (Removed set.seed(123))
for (employee in employees) {
    salary <- sample(7500:30000, 1) # Random salary for each employee
    salary_in_dollars <- paste0("$", format(salary, big.mark = ",")) # Format salary with dollar sign and commas
    cat(sprintf("Payment slip generated for %s who earns %s: YES\n", employee, salary_in_dollars))
    
    if (salary > 10000 && salary < 20000) {
        employee_grade <- "A1" # Salary range for employee who earns between 10,000 and 20,000
    } else if (salary > 7500 && salary < 30000) {
        employee_grade <- "A5-F" # Salary range for female employee who earns between 7,500 and 30,000
    } else {
        employee_grade <- "Not assigned"
    }
    
    cat(sprintf("Level assigned for %s who earns %s: %s\n", employee, salary_in_dollars, employee_grade))
}
