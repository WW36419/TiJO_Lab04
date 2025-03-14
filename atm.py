class ATM:
    """
    Klasa reprezentująca bankomat (ATM) z podstawowymi operacjami bankowymi.
    """

    def __init__(self, pin: int, funds: float = 0):
        self.pin = hash(str(pin))
        self.funds = funds

    def check_balance(self, pin: int) -> float:
        """
        Sprawdza saldo konta użytkownika.

        :param pin: PIN użytkownika.
        :return: Saldo konta użytkownika.
        :raises InvalidPinException: Jeśli podany PIN jest nieprawidłowy.
        """
        if (self.pin != hash(str(pin))):
            raise InvalidPinException

        return self.funds


    def deposit(self, pin: int, amount: float) -> float:
        """
        Wpłaca środki na konto użytkownika.

        :param pin: PIN użytkownika.
        :param amount: Kwota do wpłacenia.
        :return: Aktualne saldo po wpłacie.
        :raises InvalidPinException: Jeśli podany PIN jest nieprawidłowy.
        """
        if (self.pin != hash(str(pin))):
            raise InvalidPinException

        self.funds += amount
        return self.funds

    def withdraw(self, pin: int, amount: float) -> float:
        """
        Wypłaca środki z konta użytkownika.

        :param pin: PIN użytkownika.
        :param amount: Kwota do wypłacenia.
        :return: Aktualne saldo po wypłacie.
        :raises InsufficientFundsException: Jeśli saldo jest niewystarczające.
        :raises InvalidPinException: Jeśli podany PIN jest nieprawidłowy.
        """
        if (self.pin != hash(str(pin))):
            raise InvalidPinException
        if (self.funds < amount):
            raise InsufficientFundsException

        self.funds -= amount
        return self.funds


class InvalidPinException(Exception):
    def __init__(self):
        super().__init__("ODMOWA! Nieprawidłowy numer PIN.")

class InsufficientFundsException(Exception):
    def __init__(self):
        super().__init__("ODMOWA! Za mało środków na koncie.")