class MessageProcessor:
    def __init__(self, message) -> None:
        self.message = message

    def insert_space(self, index):
        self.message = self.message[:index] + " " + self.message[index:]
        print(self.message)

    def reverse(self, substring):
        if substring in self.message:
            reversed_substring = substring[::-1]
            self.message = self.message.replace(substring, reversed_substring, 1)
            print(self.message)
        else:
            print("error")

    def change_all(self, substring, replacement):
        self.message = self.message.replace(substring, replacement)
        print(self.message)

    def reveal_message(self):
        print(f"You have a new text message: {self.message}")

concealed_message = input()
message_processor = MessageProcessor(concealed_message)

while True:
    command = input().split(":|:")
    action = command[0]

    if action == 'InsertSpace':
        index = int(command[1])
        message_processor.insert_space(index)
    elif action == 'Reverse':
        substring = command[1]
        message_processor.reverse(substring)
    elif action == 'ChangeAll':
        substring = command[1]
        replacement = command[2]
        message_processor.change_all(substring, replacement)
    elif action == 'Reveal':
        message_processor.reveal_message()
        break