c = input('Enter A Character to check whether it\'s vowel or consonant: ')
if c == 'a' or c == 'A' or c == 'e' or c == 'E' or c == 'i' or c == 'I' or c == 'o' or c == 'O' or c == 'u' or c == 'U':
    print(f'{c} is a vowel')
else:
    print(f'{c} is a consonant')

a=('aeiouAEIOU')
c=input("enter a charater: ")
if c in a:
    print(f'{c} is vowel')
else:
    print(f'{c} is consonant')