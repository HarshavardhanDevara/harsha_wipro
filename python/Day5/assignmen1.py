# Write a script that opens a text file, reads its contents line by line,
#  and prints each line to the console.
#  Ensure that the file is properly closed after the operation, 
# even if an error occurs during the file operation
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                print(line, end='')
    except Exception as e:
        print(f"An error occurred: {e}")


file_path = r'C:\Users\harsh\Desktop\harsha_wipro\python\Day5\demo.txt'
read_file(file_path)
