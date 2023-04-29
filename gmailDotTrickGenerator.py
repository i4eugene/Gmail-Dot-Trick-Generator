import os

def generate_dot_variants(email):
    """
    Generates all possible email variants using dots.
    :param email: a string with an email address
    :return: a generator with email variants
    """
    parts = email.split('@')
    username = parts[0]
    domain = parts[1]
    n = len(username)
    # create a list of indices where dots can be inserted
    indices = [i for i in range(n - 1)]
    # iterate over all possible combinations
    for i in range(2 ** (n - 1)):
        binary = bin(i)[2:].zfill(n - 1)
        variant = ''
        for j in range(n):
            variant += username[j]
            if j in indices and binary[j-1] == '1':
                variant += '.'
        variant += '@' + domain
        yield variant


# get email from the user
email = input('Enter email: ')

# generate all variants
variants = list(generate_dot_variants(email))

# save variants to a file in the current directory
filename = os.path.join(os.getcwd(), 'variants.txt')
with open(filename, 'w') as file:
    file.write('\n'.join(variants))

print(f'Saved {len(variants)} variants to file {filename}')

# wait for user input before closing the program
input('Press Enter to close the program...')
