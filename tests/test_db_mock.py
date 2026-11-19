
import pytest
from unittest.mock import Mock
from bank import InsufficientFunds, save_account, load_balance


def test_saved_balance_can_be_loaded(db, account):
    save_account(db, account)
    assert load_balance(db, "Ayesha") == 1000


def test_each_test_gets_an_empty_database(db):
    count = db.execute(
        "SELECT COUNT(*) FROM accounts"
    ).fetchone()[0]
    assert count == 0


def test_withdraw_sends_sms(account):
    sms = Mock()
    account.withdraw_and_notify(200, sms)
    sms.send.assert_called_once_with(
        "Ayesha",
        "Withdrawn: 200. New balance: 800"
    )


def test_no_sms_when_withdraw_fails(account):
    sms = Mock()
    with pytest.raises(InsufficientFunds):
        account.withdraw_and_notify(5000, sms)
    sms.send.assert_not_called()


def test_sms_failure_is_reported(account):
    sms = Mock()
    sms.send.side_effect = ConnectionError("gateway down")
    with pytest.raises(ConnectionError):
        account.withdraw_and_notify(200, sms)
