# Create a program that asks the user for their favorite quote and author, 
# then writes this information to a file in a formatted way. 
# Afterwards, read the file and print its contents to the console.

def write_quote_to_file(file_path):
    quote = input("Enter your favorite quote: ")
    author = input("Enter the author of the quote: ")
    
    with open(file_path, 'w') as file:
        file.write(f'"{quote}"\n- {author}\n')

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                print(line, end='')
    except Exception as e:
        print(f"An error occurred: {e}")


file_path = r'C:\Users\harsh\Desktop\harsha_wipro\python\Day5\fav_quote.txt'

write_quote_to_file(file_path)
read_file(file_path)
