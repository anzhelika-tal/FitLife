# Проект FitLife - MVP версия 1.0
# Константы
WATER_PER_KG = 30
LITER = 1000

# 1. Знакомство
print('Вас приветствует цифровой фитнес-трекер FitLife. Давайте знакомиться!')
user_name = input('Как вас зовут? ')
print(f'Приятно познакомиться, {user_name}!')
user_age = int(input('Сколько вам лет? '))

# 2. Сбор данных
user_weight = float(input('Введите ваш вес (в кг, например, 75.5): '))
user_height = float(input('Введите ваш рост (в метрах, например, 1.75): '))
print('Отлично, мы собрали всю нужную информацию!')

# 3. Расчет bmi (Индекс массы тела)
bmi = user_weight / (user_height ** 2)
bmi = round(bmi, 1)

# Подсчет воды: вес * 30 мл
water_ml = user_weight * WATER_PER_KG
water_l_rounded = round(water_ml / LITER, 2)

# 4. Вывод результата.
print(f'{user_name}, ваш отчет готов!')
print(f'Отчет для пользователя: {user_name}, {user_age} г.')
print(f'Ваш Индекс Массы Тела: {bmi}')
print(f'Рекомендованная норма воды: {water_l_rounded} л. в день')
print('Расчет окончен. Будьте здоровы!')
