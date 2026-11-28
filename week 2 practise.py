
# Ask the user to enter their first and last names
full_name = input("Enter your first and last name: ")

# Find the space between the names
space_position = full_name.find(" ")

# Extract first and last names using slicing
first_name = full_name[:space_position]
last_name = full_name[space_position + 1:]

# Capitalize each name
first_name = first_name.capitalize()
last_name = last_name.capitalize()

# Print the greeting
print(f"Hi, {first_name} {last_name}")