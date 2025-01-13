import queue

# Creates a queue of files to print
files_to_print = queue.Queue()

while True:
    print('1. Add file to print')
    print('2. Print file')
    print('0. Quit')
    menu = input('Select an option: ')

    if menu == '1':
        # add new file to the end of the queue
        file_name = input('Enter file name to print: ')
        files_to_print.put(file_name)  # Put the file name in the queue

    elif menu == '2':
        # Check if the queue is not empty
        if not files_to_print.empty():
            # Print the file at the front of the queue
            file_to_print = files_to_print.get()  # Get the first file from the queue
            print(f'File {file_to_print} is currently being printed. Please wait!')
        else:
            print('No files to print.')

    elif menu == '0':
        print('Exiting the program.')
        break
