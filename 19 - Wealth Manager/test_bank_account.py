from bank_account import BankAccount
import unittest


class TestBankAccount(unittest.TestCase):
    def test_initial_balance(self):
        account = BankAccount(initial_balance=100)  # create inside the test
        self.assertEqual(account.balance, 100)
    
    def setUp(self):
        self.account = BankAccount(initial_balance=100)

    def tearDown(self):
        self.account = None
    
    
    def test_deposit_positive_amount(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)
        
    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-20)

    def test_withdraw_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-30)

    def test_deposit_zero(self):
        with self.assertRaises(ValueError):
            self.account.deposit(0)
    
if __name__ == '__main__':
    unittest.main()