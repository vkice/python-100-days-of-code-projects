# Password Generator
import string, random
print("Welcome to the Password Generator.")

# Gathering requirements
letters = int(input("How many letters would you like in your password?\n"))
symbols = int(input("How many symbols would you like in your password?\n"))
numbers = int(input("How many numbers would you like in your password?\n"))
total_chars = letters + symbols + numbers
passwd_list = []

# Generating random letters
for i in range(0, letters):
    passwd_list.append(random.choice(string.ascii_letters))

# Generating random symbols, ignoring any password incompatible symbols for demonstration purposes
for i in range(0, symbols):
    passwd_list.append(random.choice(string.punctuation))

# Generating random numbers
for i in range(0, numbers):
    passwd_list.append(random.choice(string.digits))

# Turning list into a random string
final_pw = ''
random.shuffle(passwd_list)
for i in passwd_list:
    final_pw += i

# Printing results
print(f"Here is your randomly generated password: {final_pw}")