"""
A decorator for methods that override superclass methods.
"""


def override(superclass: type):
    """
    Construct a decorator
    to check whether a method can validly override a superclass method.
    """

    assert isinstance(superclass, type), (
        "The `superclass` attribute must be"
        " a class which the given method overrides."
    )

    def check_override(method):
        """
        Check whether a method can validly override a superclass method.
        """

        assert hasattr(superclass, method.__name__), (
            f"The superclass `{superclass.__name__}`"
            f" has no method named `{method.__name__}`."
        )

        superclass_method = getattr(superclass, method.__name__)

        assert type(superclass_method) is type(method), (
            f"The superclass `{superclass.__name__}`"
            f" has an attribute named `{method.__name__}`,"
            f" but the attribute should be a method to override."
        )

        return method

    return check_override
