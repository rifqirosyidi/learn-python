some_str = str(input("Enter a Character to Hide (A-Z) : "))
upper_str = some_str.upper()
print("Initial Message : " + upper_str)

secret_str = ""

# Convert To Secret Character
for char in upper_str:
    secret_str += str(ord(char))

unicode_string = secret_str
print("Secret Message : " + unicode_string)

# Convert Back to Original String
original_string = ''

for i in range(0, len(unicode_string)-1, 2):
    temp_char = int(unicode_string[i] + unicode_string[i+1])
    original_string += str(chr(temp_char))


print("Original Mesage : " + original_string)

