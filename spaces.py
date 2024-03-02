def replace_colons_with_spaces(file_path):
    # Read the content of the file
    with open(file_path, 'r') as file:
        content = file.read()

    # Replace colons with two spaces
    modified_content = content.replace(':', '\n\n')

    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.write(modified_content)

# Example: Replace colons with two spaces in 'example.txt' file
file_path = '/home/horto/Downloads/order.txt'
replace_colons_with_spaces(file_path)
print(f"Colons replaced with two spaces in '{file_path}'.")
