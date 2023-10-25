# Jarrod Humpel

def encode(password):
    res = ''
    for char in password:
        n = int(char) + 3
        n = n % 10  # we need to constrain each n to one digit
        res += str(n)  # add digit to result
    
    return res

def decode(password):
    decode = ''
    for value in password:
        decode_value = int(value) - 3  # unshift the number
        if decode_value < 0:
            decode_value += 10  # contrain n to a positive one digit number
        decode += str(decode_value)  # add digit to result
    return decode


def main():
    while True:
        mode = input("Enter mode ('decode' or 'encode'): ")

        password = input('Enter the password to encode/decode: ')

        # either encode or decode the entered password
        if mode == 'encode':
            print(f'The encoded password is {encode(password)}')
        elif mode == 'decode':
            print(f'The decoded password is {decode(password)}')
        
        # ask the user to continue or not
        if input('exit? (Y/n): ').lower() == 'n':
            break

main()