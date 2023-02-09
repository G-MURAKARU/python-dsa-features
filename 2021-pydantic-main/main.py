# this example uses the data.json file where information about books has been logged
import json
from typing import Optional
import pydantic


class ISBN10FormatError(Exception):
    """Custom error that is raised when ISBN10 number does not have the right format"""

    def __init__(self, value: str, message: str) -> None:
        self.value = value
        self.message = message
        super().__init__(message)


class ISBNMissingError(Exception):
    """Custom error that is raised when the is no ISBN number given"""

    def __init__(self, title: str, message: str) -> None:
        self.title = title
        self.message = message
        super().__init__(message)


# this works similarly to the dataclass operator from the dataclasses module
# pydantic shines in data validation and sanitation
class Book(pydantic.BaseModel):
    title: str
    author: str
    author: str
    publisher: str
    price: float
    isbn_10: Optional[str]
    isbn_13: Optional[str]
    subtitle: Optional[str]

    # this kind of validator runs checks on the whole model
    @pydantic.root_validator(pre=True)
    @classmethod
    def check_isbn10_or_isbn13(cls, values):
        """Makes sure there is either an ISBN10 and/or an ISBN14 number given"""

        # This is a validator function that checks whether the ISBN10 or ISBN13 number is present.
        if "isbn_10" not in values and "isbn_13" not in values:
            title = values["title"]
            raise ISBNMissingError(
                title=title,
                message=f"Document '{title}' should have either an ISBN10 or ISBN13 number.",
            )

        return values

    # this kind of validator only runs checks/validations on individual fields
    @pydantic.validator("isbn_10")
    @classmethod
    def isbn_10_validator(cls, value) -> None:
        """Validator function to check whether the ISBN10 number is valid."""

        # to create a list of the characters present in the ISBN10 number,
        # excluding redundant characters e.g. '-'
        characters = [i for i in value if i in "0123456789Xx"]

        # ISBN10 should have 10 digits to be valid
        # error catcher
        if len(characters) != 10:
            raise ISBN10FormatError(value=value, message="ISBN10 should be 10 digits.")

        def char_to_int(char: str) -> int:
            """Converts a string character to an integer"""
            if char in "Xx":
                return 10
            return int(char)

        # ISBN10 digits should have a weighted sum that is divisible by 11
        # Calculating the weighted sum of the ISBN10 number.
        weighted_sum = sum(
            (10 - index) * char_to_int(character) for index, character in enumerate(characters)
        )

        # error catcher
        if weighted_sum % 11 != 0:
            raise ISBN10FormatError(
                value=value, message="ISBN10 weighted digit sum should be divisible by 11."
            )

    class Config:
        """Pydantic config class. Used for model configurations and settings"""

        # it prevents the user from changing the values of the attributes of the Book class.
        allow_mutation = False


def main() -> None:
    """Main function"""

    # read data from a JSON file
    with open("data.json") as file:
        data = json.load(file)
        # Creating a list of Book objects from the data.json file.
        books: list[Book] = [Book(**item) for item in data]
        print(books[-1].title)

        # to convert the created pydantic models to dictionaries
        print(books[0].dict(exclude={"isbn_10"}))


if __name__ == "__main__":
    main()
