import random

# Задання значень та відповідних ймовірностей
values = [1, 2, 3, 4]
probabilities = [0.4, 0.3, 0.1, 0.2]

# Кількість реалізацій
M = 100

# Зберігаємо результати реалізацій
realizations = []

# Генеруємо M реалізацій
for _ in range(M):
    realization = random.choices(values, probabilities)[0]
    realizations.append(realization)

# Рахуємо кількість кожного зі значень
count_x1 = realizations.count(1)
count_x2 = realizations.count(2)
count_x3 = realizations.count(3)
count_x4 = realizations.count(4)

# Розрахунок оцінки імовірності кожного значення
estimated_prob_x1 = count_x1 / M
estimated_prob_x2 = count_x2 / M
estimated_prob_x3 = count_x3 / M
estimated_prob_x4 = count_x4 / M

# Виводимо результати
print("Реалізації:", realizations)
print("Оцінка імовірності X1:", estimated_prob_x1)
print("Оцінка імовірності X2:", estimated_prob_x2)
print("Оцінка імовірності X3:", estimated_prob_x3)
print("Оцінка імовірності X4:", estimated_prob_x4)
