"""
A decorator for methods that override superclass methods.
"""


def override(superclass: type):
    """
    Construct a decorator
    to check whether a method can override a superclass method.
    """

    if not isinstance(superclass, type):
        raise TypeError(
            "The `superclass` attribute"
            " must be a class which the given method overrides."
        )

    def check_override(method):
        """
        Check whether a method can validly override a superclass method.
        """

        if not hasattr(superclass, method.__name__):
            raise AttributeError(
                f"The superclass `{superclass.__name__}`"
                f" has no method named `{method.__name__}`."
            )

        superclass_method = getattr(superclass, method.__name__)

        if not type(superclass_method) is type(method):
            raise TypeError(
                f"The superclass `{superclass.__name__}`"
                f" has an attribute named `{method.__name__}`,"
                f" but the attribute should be a method to override."
            )

        return method

    return check_override
