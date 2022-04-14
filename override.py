"""
A helper decorator to override methods from superclasses.
"""


def override(superclass: type):
    """
    Check that a subclass can override a superclass method.
    """

    assert isinstance(superclass, type), (
        "The `superclass` attribute must be"
        " a class which the given method overrides."
    )

    def check_override(method):
        """
        Check that the superclass has a method of the same name.
        """

        assert hasattr(superclass, method.__name__), (
            f"The superclass `{superclass}`"
            f" has no method named `{method.__name__}`."
        )

        superclass_method = getattr(superclass, method.__name__)

        assert type(superclass_method) is type(method), (
            f"The superclass `{superclass}`"
            f" has an attribute named `{method.__name__}`,"
            f" but the attribute should be a method to override."
        )

        return method

    return check_override
