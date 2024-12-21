def count_file_contents(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            
            # Calculate number of lines
            lines = content.splitlines()
            num_lines = len(lines)

            # Calculate number of characters
            num_characters = len(content)
            
            # Calculate number of words
            num_words = len(content.split())
            
            print(f"File name: {file_name}")
            print(f"Number of lines: {num_lines}")
            print(f"Number of characters: {num_characters}")
            print(f"Number of words: {num_words}")
    
    except FileNotFoundError:
        print(f"The file '{file_name}' does not exist. Please check the filename and try again.")

file_name = input("Enter the name of the text file: ")
count_file_contents(file_name)