'''Возьмите задачу о банкомате из семинара 2.
Разбейте её на отдельные операции — функции. Дополнительно сохраняйте
все операции поступления и снятия средств в список.'''

import decimal

decimal.getcontext().prec = 2

MULTIPLICITY = 50
PERCENT_WITHDRAWAL = decimal.Decimal(15)/decimal.Decimal(1000)
PERCENT_BONUS = decimal.Decimal(30)/decimal.Decimal(1000)
COUNTER_OPERATIONS = 3
MIN_LIMIT_WITHDRAWAL = decimal.Decimal(30)
MAX_LIMIT_WITHDRAWAL = decimal.Decimal(600)
PERCENT_WEALTH = decimal.Decimal(100)/decimal.Decimal(1000)
WEALTH_LIMIT = 5_000_000
CMD_DEPOSIT = '1'
CMD_WITHDRAW = '2'
CMD_EXIT = '3'

balance = 0
operations = 0
transaction_log = []

def log_transaction(operation, amount):
    transaction_log.append((operation, amount))

def apply_wealth_tax(balance):
    if balance > WEALTH_LIMIT:
        wealth_tax = balance * PERCENT_WEALTH
        balance -= wealth_tax
        log_transaction("Wealth Tax", -wealth_tax)
        print(f'Вычтен налог на богатство в размере {wealth_tax}')
    return balance

def deposit_funds(balance, amount):
    balance += amount
    log_transaction("Deposit", amount)
    return balance

def calculate_withdrawal_commission(amount):
    commission = amount * PERCENT_WITHDRAWAL
    if commission < MIN_LIMIT_WITHDRAWAL:
        commission = MIN_LIMIT_WITHDRAWAL
    elif commission > MAX_LIMIT_WITHDRAWAL:
        commission = MAX_LIMIT_WITHDRAWAL
    return commission

def withdraw_funds(balance, amount):
    commission = calculate_withdrawal_commission(amount)
    if commission + amount > balance:
        print('На балансе недостаточно средств')
    else:
        balance -= (amount + commission)
        log_transaction("Withdrawal", -amount - commission)
        print(f'Сумма снятия: {amount}, комиссия: {commission}, общая сумма: {amount + commission}')
    return balance

def apply_bonus(balance):
    bonus_sum = balance * PERCENT_BONUS
    balance += bonus_sum
    log_transaction("Bonus", bonus_sum)
    print(f'Сумма бонуса: {bonus_sum}')
    return balance


while True:
    action = input(
        f'Пополнить - {CMD_DEPOSIT}\n'
        f'Снять - {CMD_WITHDRAW}\n'
        f'Выход - {CMD_EXIT}\n'
        f'Введите действие: ')

    balance = apply_wealth_tax(balance)

    if action == CMD_DEPOSIT or action == CMD_WITHDRAW:
        amount = 1
        while amount % MULTIPLICITY != 0:
            amount = int(input(f'Введите сумму, кратную {MULTIPLICITY}: '))

        if action == CMD_DEPOSIT:
            balance = deposit_funds(balance, amount)
            operations += 1
            print(f'Сумма пополнения: {amount}')

        elif action == CMD_WITHDRAW:
            balance = withdraw_funds(balance, amount)
            operations += 1

        if operations % COUNTER_OPERATIONS == 0:
            balance = apply_bonus(balance)

        print(f'Текущий баланс: {balance}')

    elif action == CMD_EXIT:
        break
    else:
        print(f'Введена неверная команда')

print("Транзакции:")
for log in transaction_log:
     print(log)

