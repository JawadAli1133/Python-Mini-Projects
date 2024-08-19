try:
    file = open('file.txt')
    values = {
        'key': 'value',
        'key1': 'value1'
    }
    print(values['key1'])
except FileNotFoundError:
    file = open('file.txt', 'w')
    file.write('Something')
except KeyError as message:
    print(f'The key {message} does not exist')
else:
    content = file.read()
    print(content)
finally:
    file.close()