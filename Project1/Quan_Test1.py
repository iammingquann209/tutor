#READ
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None

#WRITE
def write_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"File '{filename}' written successfully.")
    except:
        print(f"Error writing to file '{filename}'.")

#FORMAT
def format_string(string):  
    
#Delete '        ' and '------------'   
    originalLines = string.split('\n')
    lines = []
    for line in originalLines:
        if '-' not in line:
            lines.append(line)
    numOfColumn = len(lines[0].split())
    
#Create nestList that each element is a list of each row
    nestList = []
    for line in lines:
        words = line.split()
        nestList.append(words)   
    
#Max_of_each_Column
    padding = []
    for index in range(numOfColumn):
        max_width = max(len(element[index]) for element in nestList)
        padding.append(max_width)
    
#Formatted
    formatted_lines = []
    for row in nestList:
            formatted_row = ' | '.join(f'{col:^{width}}' if col else ' ' * width for col, width in zip(row, padding))
            formatted_lines.append(formatted_row)
    
#Max length of string formatted    
    max_len = 0   
    sum = 0
    for item in padding:
        sum += item
    max_len = sum + (numOfColumn - 1)*3
    
#Add 2 row '   ' and '----' to results   
    separator_row = '-' * max_len
    formatted_lines.insert(1, separator_row)
    formatted_lines.insert(3, separator_row)
     
#Final results
    test1 = '\n'.join(formatted_lines)
    return test1

#MAIN
def main():
   file_content = read_file('test.txt')
   test1 = format_string(file_content)
   write_file('test1.txt', test1)

if __name__ == "__main__":
    main()