
from datetime import date


def today():
    return date.today()


class InsufficientFunds(Exception):
    pass


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFunds(
                f"Balance is only {self.balance}"
            )
        self.balance -= amount

    def save_statement(self, path):
        path.write_text(
            f"Owner: {self.owner}\nBalance: {self.balance}"
        )

    def print_statement(self):
        print(f"Owner: {self.owner}")
        print(f"Balance: {self.balance}")

    def add_monthly_interest(self, rate):
        if today().day != 1:
            raise ValueError(
                "Interest is only added on the 1st of the month"
            )
        self.balance += self.balance * rate

    def withdraw_and_notify(self, amount, sms_service):
        self.withdraw(amount)
        sms_service.send(
            self.owner,
            f"Withdrawn: {amount}. New balance: {self.balance}"
        )


def save_account(conn, account):
    conn.execute(
        "INSERT INTO accounts (owner, balance) VALUES (?, ?)",
        (account.owner, account.balance),
    )
    conn.commit()


def load_balance(conn, owner):
    row = conn.execute(
        "SELECT balance FROM accounts WHERE owner = ?",
        (owner,),
    ).fetchone()
    return row[0]


class SMSService:
    def send(self, to, message):
        raise RuntimeError("Real SMS gateway not available")
