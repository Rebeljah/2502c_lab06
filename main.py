# Jarrod Humpel

def encode(password):
    res = ''
    for char in password:
        n = int(char) + 3
        n = n % 10
        res += str(n)
    
    return res

def decode(password):
    decode = ''
    for value in password:
        decode_value = int(value) - 3
        if decode_value < 0:
            decode_value += 10
        decode += str(decode_value)
    return decode


def main():
    while True:
        mode = input("Enter mode ('decode' or 'encode'): ")

        password = input('Enter the password to encode/decode: ')

        if mode == 'encode':
            print(f'The encoded password is {encode(password)}')
        elif mode == 'decode':
            print(f'The decoded password is {decode(password)}')
        
        if input('exit? (Y/n): ').lower() == 'n':
            break

main()