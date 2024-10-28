# def calculate_finance(monthly_income: float, tax_rate: float, currency: str) -> None:
#     yearly_salary: float = monthly_income * 12
#     monthly_tax: float = monthly_income * (tax_rate / 100)
#     yearly_tax: float = monthly_tax * 12
#     monthly_net_income: float = monthly_income - monthly_tax
#     yearly_net_income: float = yearly_salary - yearly_tax
#     print('---------------------------')
#     print(f'Ежемесячный доход: {currency}{monthly_income}$')
#     print(f'Ставка налога: {currency}{monthly_tax}$')
#     print(f'Ежемесячный налог: {currency}{monthly_net_income}$')
#     print(f'Ежемесячный чистый доход: {currency}{yearly_salary}$')
#     print(f'Годовой уплаченный налог: {currency}{yearly_tax}$')
#     print(f'Годовой чистый доход: {currency}{yearly_net_income}$')
#     print('---------------------------')
# calculate_finance(100.1234, 20, '$')
#
# def main() -> None:
#     monthly_income: float = float(input('Введите свой ежемесячный доход $: '))
#     tax_rate: float = float(input('Введите свой ставка налога (%): '))
#
#     calculate_finance(monthly_income, tax_rate, currency='KR')
#
# if __name__ == '__main__':
#     main()
# x = open('homework.py', "w")
# x.close()


y = open('.gitignore', 'w')
y.close()