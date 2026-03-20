with open('new_file.txt', 'w', encoding='utf-8') as file:
    file.write('Hello!\n')
with open('new_file.txt', 'a', encoding='utf-8') as file:
    file.write('Hello, again!\n')
with open('new_file.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)