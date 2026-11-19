
import pytest
import sqlite3
from bank import BankAccount


@pytest.fixture
def account():
    return BankAccount("Ayesha", balance=1000)


@pytest.fixture
def db():
    conn = sqlite3.connect(":memory:")
    conn.execute(
        "CREATE TABLE accounts (owner TEXT, balance REAL)"
    )

    print("\n[setup] database opened")
    yield conn

    conn.close()
    print("\n[teardown] database closed")
