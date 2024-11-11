VALID_CHOICES = ['rock', 'paper', 'scissors']

def prompt(message):
    print(f"==> {message}")

prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
choice = input()

while choice not in VALID_CHOICES:
    prompt("That's not a valid choice")
    choice = input()

