import pulp


def resolve_problem():
    # Ініціалізація моделі
    model = pulp.LpProblem("Maximize_Profit", pulp.LpMaximize)

    # Визначення змінних
    lemonade = pulp.LpVariable(
        "Lemonade", lowBound=0, cat="Integer"
    )  # Кількість продукту А
    fruit_juice = pulp.LpVariable(
        "Fruit_Juice", lowBound=0, cat="Integer"
    )  # Кількість продукту Б

    # Функція цілі (Максимізація прибутку)
    model += lemonade + fruit_juice, "Profit"

    # Додавання обмежень
    model += 2 * lemonade + fruit_juice <= 100  # Вода
    model += lemonade <= 50  # Цукор
    model += lemonade <= 30  # Лимонний сік
    model += 2 * fruit_juice <= 40  # Фруктове пюре

    # Розв'язання моделі
    model.solve()

    return model, lemonade, fruit_juice


def main():
    model, lemonade, fruit_juice = resolve_problem()

    print("Максимальна кількість продуктів -", pulp.value(model.objective))
    print("Лимонад -", lemonade.varValue)
    print("Фруктовий сік -", fruit_juice.varValue)


if __name__ == "__main__":
    main()
