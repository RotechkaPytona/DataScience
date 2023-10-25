
import matplotlib.pyplot as plt

# Исходные данные
N = 1000  # Всего население
I0 = 1  # Начальное количество заболевших (первый человек)
S0 = N - I0  # Начальное количество здоровых
R0 = 0  # Начальное количество выздоровевших

# Списки для хранения данных
S = [S0]
I = [I0]
R = [R0]

# Дни
days = [0]

recovery_period = 7  # Период выздоровления в днях

# Рассчитываем значения для каждого дня
while I[-1] > 0:
    new_I = I[-1] * (3 * S[-1] / N - 1)
    I.append(new_I)

    if len(I) >= recovery_period:
        new_R = R[-1] + I[-recovery_period]
        R.append(new_R)
    else:
        R.append(0)

    S.append(N - new_I - R[-1])
    days.append(days[-1] + 1)

# Построение графика
plt.plot(days, S, label="Здоровые")
plt.plot(days, I, label="Заболевшие")
plt.plot(days, R, label="Выздоровевшие")
plt.xlabel("Дни")
plt.ylabel("Число людей")
plt.legend()
plt.title("Модель эпидемии коронавируса с учетом выздоровления через 7 дней")
plt.show()

# Нахождение дня окончания эпидемии
end_day = days[-1]
print(f"Эпидемия закончится на {end_day} день")

# Нахождение пика эпидемии
peak_infections = max(I)
peak_day = days[I.index(peak_infections)]
print(f"Пик эпидемии: {peak_infections} заболевших на {peak_day} день")




