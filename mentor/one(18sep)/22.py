# Question -  Accept an english alphabet from user and check if it is a consonent or a vowel
alp = input("Enter an single English alphabet: ")

if alp == 'a' or alp == 'A' or alp == 'e' or alp == 'E' or alp == 'i' or alp == 'I' or alp == 'o' or alp == 'O' or alp == 'u' or alp == 'U':
    print(f"{alp} is a vowel.")
else:
    print(f"{alp} is a consonant.")
