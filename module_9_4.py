from random import choice

# Lambda-функция

first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x, y: x == y, first, second)))


# Замыкание переменных

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        new_str = ''
        for i in data_set:
             new_str += f'{i}\n'
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(new_str)
        return file
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# Метод __call__

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())