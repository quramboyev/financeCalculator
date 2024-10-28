# first hometask
# def calculate_finance(monthly_income: float, tax_rate: float, rent: float, food: float, gym: float) -> None:
#     yearly_salary: float = monthly_income * 12
#     monthly_tax: float = monthly_income * (tax_rate / 100)
#     monthly_expenses: float = rent + food + gym + monthly_tax
#     monthly_net_income: float = monthly_income - monthly_expenses
# 
#     print('---------------------------')
#     print(f'Ежемесячный доход: {monthly_income}$')
#     print(f'Налог за месяц: {monthly_tax}$')
#     print(f'Ежемесячные расходы: {monthly_expenses}$')
#     print(f'Чистый доход (месяц): {monthly_net_income}$')
#     print('---------------------------')
# 
# 
# def main() -> None:
#     monthly_income: float = float(input("Введите свой ежемесячный доход $: "))
#     tax_rate: float = float(input('Введите ставку налога (%): '))
#     rent: float = float(input('Введите сумму аренды: '))
#     food: float = float(input('Введите ежемесячные расходы на еду: '))
#     gym: float = float(input('Введите стоимость абонемента в спортзал: '))
# 
#     calculate_finance(monthly_income, tax_rate, rent, food, gym)
# 
# 
# if __name__ == '__main__':
#     main()

def calculate_finance(monthly_income: float, tax_rate: float, currency: str) -> None:
    yearly_salary: float = monthly_income * 12
    monthly_tax: float = monthly_income * (tax_rate / 100)
    yearly_tax: float = monthly_tax * 12
    monthly_net_income: float = monthly_income - monthly_tax
    yearly_net_income: float = yearly_salary - yearly_tax
    print('---------------------------')
    print(f'Ежемесячный доход: {currency}{monthly_income}$')
    print(f'Налог за месяц: {currency}{monthly_tax}$')
    print(f'Чистый доход за месяц: {currency}{monthly_net_income}$')
    print(f'Годовой доход: {currency}{yearly_salary}$')
    print(f'Уплаченный налог за год: {currency}{yearly_tax}$')
    print(f'Чистый доход за год: {currency}{yearly_net_income}$')
    print('---------------------------')


def get_float_input(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка! Введите число.")


def main() -> None:
    monthly_income: float = get_float_input('Введите свой ежемесячный доход $: ')
    tax_rate: float = get_float_input('Введите свою ставку налога (%): ')

    calculate_finance(monthly_income, tax_rate, currency='KR')


if __name__ == '__main__':
    main()

a = 1
b = 3
c = a + b
