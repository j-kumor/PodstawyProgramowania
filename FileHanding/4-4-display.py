# Program to display the contents of it_company.csv in chunks of five lines

file_name = 'it_company.csv'

# Function to display lines in chunks
def display_lines_in_chunks(file_name, chunk_size=5):
    with open(file_name, 'r') as file:
        while True:
            # Read the next chunk of lines
            lines = [file.readline() for _ in range(chunk_size)]
            
            # If no more lines are read, break the loop
            if not lines or all(line == '' for line in lines):
                break
            
            for line in lines:
                print(line, end='')
            
            input("\nPress Enter key to continue...")

# Call the function to display lines
display_lines_in_chunks(file_name)