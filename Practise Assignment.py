# Software Bug Tracking System

# Get bug details from the user
project_name = input("Enter the project name: ")
bug_id = input("Enter the bug ID: ")
bug_description = input("Enter the bug description: ")

# Get bug severity from the user
severity = int(input("Enter bug severity (1-5): "))

# Get estimated fixing time from the user
estimated_time = float(input("Enter estimated hours required to fix the bug: "))

# Get the developer's hourly rate
hourly_rate = float(input("Enter the developer's hourly rate ($): "))

# Check whether the bug is reproducible
reproducible = input("Is the bug reproducible? (yes/no): ")

# Calculate the estimated fixing cost
estimated_cost = estimated_time * hourly_rate

# Calculate testing time as 25% of fixing hours
testing_time = estimated_time * 0.25

# Calculate total estimated development time and cost
total_time = estimated_time + testing_time
total_cost = total_time * hourly_rate

#Use comparison operators to check wheather bug is critical
is_critical =  severity >= 4

# Check whether fixing requires more than 8 hours
requires_more_than_8_hours = estimated_time > 8

# Check whether total cost exceeds $1,000
cost_exceeds_1000 = total_cost > 1000

# Check whether bug requires urgent attention
urgent_attention = is_critical and reproducible == "yes"

# 10. Display formatted bug report using f-strings
print(f"Bug Report for {project_name}")
print(f"Bug ID: {bug_id}")
print(f"Description: {bug_description}")
print(f"Severity: {severity}")
print(f"Estimated Time: {estimated_time} hours")
print(f"Hourly Rate: ${hourly_rate}")
print(f"Estimated Cost: ${estimated_cost:.2f}")
print(f"Testing Time: {testing_time} hours")
print(f"Total Time: {total_time} hours")
print(f"Total Cost: ${total_cost:.2f}")
print(f"Is Critical: {is_critical}")
print(f"Requires More Than 8 Hours: {requires_more_than_8_hours}")
print(f"Cost Exceeds $1,000: {cost_exceeds_1000}")
print(f"Requires Urgent Attention: {urgent_attention}")