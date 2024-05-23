def bank(X, Y):
    # Проходим через каждый год и увеличиваем вклад на 10%
    for _ in range(Y):
        X += X * 0.10
    return X

# Пример использования функции
initial_deposit = 1000  # размер вклада в рублях
years = 5  # срок в годах

final_amount = bank(initial_deposit, years)
print(f"Сумма на счету пользователя спустя {years} лет: {final_amount:.2f} рублей")
