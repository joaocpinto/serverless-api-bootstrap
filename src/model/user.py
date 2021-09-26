from datetime import date

from pydantic import BaseModel, constr


class UserModel(BaseModel):
    """
    Model class for the user
    """

    username: constr(regex=r"[A-Za-z]+")  # noqa: F722
    dateOfBirth: date

    def is_birthday(self):
        dt = date.today()
        if self.dateOfBirth.month == dt.month and self.dateOfBirth.day == dt.day:
            return True
        else:
            return False
