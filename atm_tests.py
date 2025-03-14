import unittest
from atm import ATM
from atm import InvalidPinException
from atm import InsufficientFundsException


class ATMTestCase(unittest.TestCase):
    def test_check_balance_should_return_funds(self):
        # Act
        pin, funds = 1124, 50
        # Arrange
        atm = ATM(pin, funds)
        result = atm.check_balance(pin)
        # Assert
        self.assertEqual(result, 50)

    def test_deposit_should_increase_funds(self):
        # Act
        pin, funds, deposit_funds = 1234, 40, 20
        # Arrange
        atm = ATM(pin, funds)
        result = atm.deposit(pin, deposit_funds)
        # Assert
        self.assertEqual(result, 60)

    def test_withdraw_should_decrease_funds(self):
        # Act
        pin, funds, withdraw_funds = 1243, 40, 30
        # Arrange
        atm = ATM(pin, funds)
        result = atm.withdraw(pin, withdraw_funds)
        # Assert
        self.assertEqual(result, 10)

    def test_wrong_pin_on_check_balance_should_raise_exception(self):
        # Act
        pin, wrong_pin = 1111, 2222
        # Arrange
        atm = ATM(pin)
        # Assert
        self.assertRaises(InvalidPinException, atm.check_balance, wrong_pin)

    def test_wrong_pin_on_deposit_should_raise_exception(self):
        # Act
        pin, wrong_pin, deposit_funds = 1111, 2222, 30
        # Arrange
        atm = ATM(pin)
        # Assert
        self.assertRaises(InvalidPinException, atm.deposit, wrong_pin, deposit_funds)

    def test_wrong_pin_on_withdraw_should_raise_exception(self):
        # Act
        pin, wrong_pin, withdraw_funds = 1111, 2222, 20
        # Arrange
        atm = ATM(pin)
        # Assert
        self.assertRaises(InvalidPinException, atm.withdraw, wrong_pin, withdraw_funds)

    def test_insufficient_funds_on_withdraw_should_raise_exception(self):
        # Act
        pin, withdraw_funds = 1111, 20
        # Arrange
        atm = ATM(pin)
        # Assert
        self.assertRaises(InsufficientFundsException, atm.withdraw, pin, withdraw_funds)



if __name__ == "__main__":
    unittest.main()
