import logging

# CUSTOM LOGGER SETTINGS

# to create a custom logger (avoid using the root logger)
logger = logging.getLogger(__name__)

# to set the level of the custom logger
logger.setLevel(logging.INFO)

# CUSTOM FILE HANDLER SETTINGS

# to create a formatter for the file handler (not the logger)
formatter = logging.Formatter("%(asctime)s: %(name)s: %(levelname)s: %(message)s")

# to create a custom file handler for the custom logger
file_handler = logging.FileHandler("employee.log")

# to add the created formatter to the created file handler
file_handler.setFormatter(formatter)

# to add the file handler to the custom logger
logger.addHandler(file_handler)

# DEFAULT LOGGER SETTINGS

# logging.basicConfig(
#     level=logging.INFO,
#     filename="employee.log",
#     format="%(asctime)s: %(name)s: %(levelname)s: %(message)s",
# )


class Employee:
    def __init__(self, first: str, last: str) -> None:
        self.first = first
        self.last = last

        logger.info(f"Created Employee {self.fullname} - {self.email}")  # logger here

    @property  # used as a getter
    def email(self) -> str:
        return f"{self.first.lower()}.{self.last.lower()}@email.com"

    @property  # used as a getter
    def fullname(self) -> str:
        return f"{self.first} {self.last}"

    @fullname.setter  # used as a setter
    def fullname(self, name: str) -> None:
        first, last = name.split(" ")
        self.first = first
        self.last = last

        logger.info("Employee full name changed.")

    @fullname.deleter  # used as a deleter
    def fullname(self) -> None:
        print("Deleted name.")
        self.first = None
        self.last = None


emp1 = Employee("Gicheru", "Murakaru")
print(emp1.email)
# notice the email was defined as a method but is accessed as an attribute
# the @property allows this - acts as a getter

print(emp1.fullname)  # 'get' operation
emp1.fullname = "Sylvia Murakaru"  # 'set' operation
# notice employee full name was defined as a method but is being SET as an ATTRIBUTE
# the @property in the first method makes it act like a getter
# the @fullname.setter in the second method makes it act like a setter
print(emp1.email)  # 'get' operation

# in order to delete an attribute, a deleter is created (peep above)
# del emp1.fullname
# print(emp1.fullname)

emp2 = Employee(first="Shawn", last="Mwitia")
