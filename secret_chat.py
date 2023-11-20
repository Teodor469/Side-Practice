import re

def main():
    input_text = input()
    task = input().split(":|:")

    while task[0] != "Reveal":
        if task[0] == "ChangeAll":
            input_text = input_text.replace(task[1], task[2])
            print(input_text)
        elif task[0] == "InsertSpace":
            space_num = int(task[1])
            input_text = input_text[:space_num] + " " + input_text[space_num:]
            print(input_text)
        elif task[0] == "Reverse":
            for_check = task[1]
            if for_check in input_text:
                for_replays = for_check[::-1]
                input_text = re.sub(re.escape(for_check), "", input_text, 1) + for_replays
                print(input_text)
            else:
                print("error")

        task = input().split(":|:")

    print(f"You have a new text message: {input_text}")

if __name__ == "__main__":
    main()
