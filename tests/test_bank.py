
import pytest
from datetime import date
import bank
from bank import InsufficientFunds


def test_new_account_starts_with_given_balance(account):
    assert account.balance == 1000


def test_deposit_increases_balance(account):
    account.deposit(500)
    assert account.balance == 1500


def test_withdraw_more_than_balance_raises(account):
    with pytest.raises(InsufficientFunds):
        account.withdraw(5000)
    assert account.balance == 1000


def test_save_statement(account, tmp_path):
    file = tmp_path / "statement.txt"
    account.save_statement(file)
    assert file.read_text() == (
        "Owner: Ayesha\nBalance: 1000"
    )


@pytest.mark.xfail(
    reason="known bug: negative withdrawals are not rejected"
)
def test_withdraw_negative_amount_raises(account):
    with pytest.raises(ValueError):
        account.withdraw(-100)


@pytest.mark.slow
def test_many_deposits(account):
    for _ in range(10_000):
        account.deposit(1)
    assert account.balance == 11_000


@pytest.mark.parametrize("amount, expected_balance", [
    (1, 999),
    (999, 1),
    (1000, 0),
])
def test_withdraw_valid_boundaries(
    account, amount, expected_balance
):
    account.withdraw(amount)
    assert account.balance == expected_balance


def test_withdraw_just_above_balance_raises(account):
    with pytest.raises(InsufficientFunds):
        account.withdraw(1001)


def test_print_statement(account, capsys):
    account.print_statement()
    captured = capsys.readouterr()
    assert captured.out == (
        "Owner: Ayesha\nBalance: 1000\n"
    )


def test_interest_added_on_first_of_month(
    account, monkeypatch
):
    monkeypatch.setattr(
        bank, "today", lambda: date(2026, 12, 1)
    )
    account.add_monthly_interest(rate=0.01)
    assert account.balance == pytest.approx(1010)


def test_interest_refused_mid_month(
    account, monkeypatch
):
    monkeypatch.setattr(
        bank, "today", lambda: date(2026, 12, 15)
    )
    with pytest.raises(ValueError, match="1st of the month"):
        account.add_monthly_interest(rate=0.01)
