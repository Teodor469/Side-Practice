def main():
    the_string = input()
    while True:
        command = input().split()
        if command[0] == 'End':
            break

        if command[0] == "Translate":
            the_string = the_string.replace(command[1], command[2])
            print(the_string)
        elif command[0] == "Includes":
            substring_to_check = command[1]
            if substring_to_check in the_string:
                print("True")
            else:
                print("False")
        elif command[0] == "Start":
            start_substring = command[1]
            if the_string.startswith(start_substring):
                print("True")
            else:
                print("False")
        elif command[0] == "Lowercase":
            the_string = the_string.lower()
            print(the_string)
        elif command[0] == "FindIndex":
            char_to_find = command[1]
            last_occurrence_index = the_string.rfind(char_to_find)
            print(last_occurrence_index)
        elif command[0] == "Remove":
            start_index = int(command[1])
            count = int(command[2])
            the_string = the_string[:start_index] + the_string[start_index + count:]
            print(the_string)
            
main()