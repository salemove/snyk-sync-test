password = 'Password123'

def main():
    user_pass = input('Password: ')
    if user_pass == password:
        print('Passwords matches. Access granted.')
    else:
        print(f'Passwords do not match. Hint: {password}')

    with open(input('path:'), 'rw') as f:
        print(f.readlines())

if __name__ == '__main__':
    main()
