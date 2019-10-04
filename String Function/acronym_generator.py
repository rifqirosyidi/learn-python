# Example of acronym
# Random Access Memory = RAM


# Ask the input and assign to a variables
s_input = input("Enter some sentences : ")
s_accronym = ''
# Convert to UpeerCase
s_input.upper()

# Convent to List
list_str = s_input.split(sep=' ')

# Cytle through List
for word in list_str:
    s_accronym += word[0]

print(s_accronym)


