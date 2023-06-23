
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class LetterNumberUnderscoreValidator:
    def __call__(self,username):
        for x in username:
            if not x.isalnum() and not x == '_':
                raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")

    def __eq__(self, other):
        return True

