# Override

The `override` Python package
provides the `override` decorator,
which improves readability
by indicating the superclass
that a method overrides.

# Checks

The decorator performs certain checks
on the method and the given superclass.

- Whether the superclass has an attribute with the same name.
- Whether the attribute of the superclass is a function.

# Example

Although the example below is relatively simple,
the decorator helps especially
in larger applications and packages
or where class has multiple superclasses.

```python
from override import override


class Animal:
    """
    An animal with a greeting.
    """

    def greet(self):
        """
        Greet another animal.
        """

        print("Hello!")


class Dog(Animal):
    """
    A dog with a greeting.
    """

    @override(Animal)
    def greet(self):
        """
        Greet another dog.
        """

        print("Woof!")
```
