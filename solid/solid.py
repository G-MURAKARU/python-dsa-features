# Uncle Bob's SOLID PRINCIPLES
# S - single responsibility
# - removed pay method from Order class, reusability
# O - open (for extension)/closed (for modification)
# L - Liskov substitution
# I - interface segregation
# D - dependency inversion
from abc import ABC, abstractmethod


class Order:
    items = []
    quantities = []
    prices = []
    status: str = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        multiply = __import__("operator").mul
        return sum(multiply(*i) for i in zip(self.prices, self.quantities))

    def set_status(self, order_status: str) -> None:
        self.status = order_status


# OLD PAYMENT PROCESSOR - does not adhere to O in SOLID as it requires modification to add more payment methods
# class PaymentProcessor:
#     def pay_debit(self, order: Order, security_code: str) -> None:
#         print("Processing debit payment type")
#         print(f"Verifying security code: {security_code}")
#         # so that status is only handled by the Order class
#         order.set_status("paid")

#     def pay_credit(self, order: Order, security_code: str) -> None:
#         print("Processing credit payment type")
#         print(f"Verifying security code: {security_code}")
#         # so that status is only handled by the Order class
#         order.set_status("paid")


# NEW PAYMENT PROCESSOR - adheres to O in SOLID, no mods, extended in subclasses below (peep paypal subclass)
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order: Order) -> None:
        pass

    # @abstractmethod
    # def auth_sms(self, code):
    #     pass


# D - dependency inversion : ensure subclasses depend on abstractions and not concrete classes
# problem: composition with concrete SMSAuth class
# fix: have an Authoriser ABC


class Authoriser(ABC):
    @abstractmethod
    def is_authorised(self) -> bool:
        pass


# I - interface segregation - debit and paypal accept 2FA but credit does not,
# therefore it is bad practice to make credit inherit sth it does not need
# instead of having one general-purpose interface, it is split so subclasses have meaningful behaviour
# fix: create a PaymentProcessor subclass to handle 2FA; use composition with a new class
# subclasses use Authoriser with composition instead of SMSAuth,
# so it is easier to integrate a different authentication method in the programme if needed e.g. NotARobot


class SMSAuth(Authoriser):
    authorised: bool = False

    def verify_code(self, code):
        print(f"Verifying code {code}")
        self.authorised = True

    def is_authorised(self) -> bool:
        return self.authorised


class NotARobot(Authoriser):
    authorised: bool = False

    def not_a_robot(self):
        print("Are you a robot? No.")
        self.authorised = True

    def is_authorised(self) -> bool:
        return self.authorised


# L in SOLID, should be able to make instances of the class
# e.g. paypal does not use security codes but email addresses,
# therefore inheriting the PaymentProcessor as is (with the security_code parameter) abuses it,
# as it is defined to accept security codes
# fix: remove security_code param and add an initialiser in each subclass


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code: str, authoriser: Authoriser) -> None:
        self.security_code = security_code
        # self.verified = False
        self.authoriser = authoriser

    # def auth_sms(self, code):
    #     print(f"Verifying SMS code {code}")
    #     self.verified = True

    def pay(self, order: Order) -> None:  # sourcery skip: raise-specific-error
        if not self.authoriser.is_authorised():
            raise Exception("Not authorised")

        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        # so that status is only handled by the Order class
        order.set_status("paid")


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code: str) -> None:
        self.security_code = security_code

    def pay(self, order: Order) -> None:
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        # so that status is only handled by the Order class
        order.set_status("paid")


class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self, email_address: str, authoriser: Authoriser) -> None:
        self.email_address = email_address
        self.authoriser = authoriser

    def pay(self, order: Order) -> None:  # sourcery skip: raise-specific-error
        if not self.authoriser.is_authorised():
            raise Exception("Not authorised")

        print("Processing paypal payment type")
        print(f"Verifying security code: {self.email_address}")
        # so that status is only handled by the Order class
        order.set_status("paid")


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB Cable", 2, 5)

print(order.total_price())
# authoriser = SMSAuth()
authoriser = NotARobot()
processor = DebitPaymentProcessor(security_code="0372846", authoriser=authoriser)
# authoriser.verify_code(465839)
authoriser.not_a_robot()
processor.pay(order=order)
