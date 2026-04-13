# ABSTRACTION

class CommandPrompt:
    def __init__(self, buy_commands, sell_commands, wait_commands):
        self.buy_commands = buy_commands
        self.sell_commands = sell_commands
        self.wait_commands = wait_commands

    def ask(self):
        while True:
            choice = input("Your decision: ")

            if choice in self.buy_commands:
                return "buy"
            elif choice in self.sell_commands:
                return "sell"
            elif choice in self.wait_commands:
                return "wait"
            else:
                print(f"Invalid choice: {choice}")


# create instance ABOVE main(), as required
prompt = CommandPrompt(
    buy_commands=("buy", "b"),
    sell_commands=("sell", "s"),
    wait_commands=("wait", "", "w"),
)


# ----- Wallet class -----

class Wallet:
    def __init__(self, pln, usd):
        self.pln = float(pln)
        self.usd = float(usd)

    def convert_pln_to_usd(self, usdpln_rate):
        if self.pln > 0:
            self.usd += self.pln / usdpln_rate
            self.pln = 0.0

    def convert_usd_to_pln(self, usdpln_rate):
        if self.usd > 0:
            self.pln += self.usd * usdpln_rate
            self.usd = 0.0


# ----- main function -----

def main(usdpln_rates):
    wallet = Wallet(1000, 0)

    for rate in usdpln_rates:
        print(f"Wallet: PLN {wallet.pln:.2f}, USD {wallet.usd:.2f}")
        print(f"USD/PLN rate: {rate:.2f}")

        decision = prompt.ask()

        if decision == "buy":
            wallet.convert_pln_to_usd(rate)
        elif decision == "sell":
            wallet.convert_usd_to_pln(rate)
        # "wait" does nothing

    print(f"Wallet: PLN {wallet.pln:.2f}, USD {wallet.usd:.2f}")

rates = [4.1]
main(rates)


# EXERCISE 2

import math


def middle_elements(sequences):
    result = []

    for seq in sequences:
        length = len(seq)

        # skip empty sequences
        if length == 0:
            continue

        # middle index (right one if even)
        middle_index = length // 2
        result.append(seq[middle_index])

    return result


class SequenceOfNumbers:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step

    def __len__(self):
        if self.step <= 0:
            return 0
        return math.ceil((self.stop - self.start) / self.step)

    def __getitem__(self, index):
        if index < 0:
            raise IndexError("Negative indexes are not supported, sorry!")

        length = len(self)
        if index >= length:
            raise IndexError(
                "Always look beyond the horizon, but never beyond the end of sequence!"
            )

        return self.start + index * self.step


print(middle_elements([
    [6, 7, 8, 9, 10],
    ["Who", "is", "that?"],
    [],
    ["six", "seven", "eight", "nine"],
]))

nums = SequenceOfNumbers(14, 46, 4)

print(len(nums))   # 8
print(nums[0])     # 14
print(nums[7])     # 42
print(nums[2])     # 22

# EXERCISE 4
import string


class SingleChoiceQuestion:
    def __init__(self, question_text, answers):
        self.question_text = question_text
        self.answers = answers

    def ask(self):
        # Display question
        print(self.question_text)

        # Assign letters to options
        letters = string.ascii_lowercase
        option_map = {}
        for i, answer in enumerate(self.answers):
            letter = letters[i]
            option_map[letter] = answer
            print(f"{letter}) {answer}")

        # Prompt user for input
        while True:
            choice = input("Answer: ").strip().lower()
            if choice in option_map:
                print()  # empty line after question
                return choice
            else:
                print(f"Invalid answer, try again:", end=" ")


class Questionnaire:
    def __init__(self, title):
        self.title = title
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def run(self):
        print(self.title)
        print()  # empty line

        results = {}
        for i, question in enumerate(self.questions):
            answer = question.ask()
            results[i] = answer

        print("Thank you!")
        return results

questionnaire = Questionnaire('Laptop satisfaction questionnaire')

q1 = SingleChoiceQuestion(
    'Size of screen',
    ['less than 15 inches', 'from 15 to 17 inches', 'more than 17 inches']
)
q2 = SingleChoiceQuestion(
    'Type of screen',
    ['matte', 'glossy']
)
q3 = SingleChoiceQuestion(
    'Would you recommend it?',
    ['definitely yes', 'rather yes', 'not sure', 'rather not', 'definitely not']
)

questionnaire.add_question(q1)
questionnaire.add_question(q2)
questionnaire.add_question(q3)

answers = questionnaire.run()
print(answers)