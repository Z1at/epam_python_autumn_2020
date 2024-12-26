"""
We have a file that works as key-value storage,
each like is represented as key and value separated by = symbol,
example:
    name=kek
    last_name=top
    song_name=shadilay
    power=9001

Values can be strings or integer numbers.
If a value can be treated both as a number and a string, it is treated as number.

Write a wrapper class for this key value storage that works like this:

storage = KeyValueStorage('path_to_file.txt')
that has its keys and values accessible as collection items and as attributes.
Example:
    storage['name'] # will be string 'kek'
    storage.song_name # will be 'shadilay'
    storage.power # will be integer 9001

In case of attribute clash existing built-in attributes take precedence.
In case when value cannot be assigned to an attribute
(for example when there's a line 1=something) ValueError should be raised.
File size is expected to be small, you are permitted to read it entirely into memory.

"""
from string import ascii_letters, digits
from typing import Union


class KeyValueStorage:
    """Key-value storage class.

    Args:
        path_to_file: Path to file.

    Attributes:
        pairs: A dictionary containing a key and value pair.

    Examples:
        >>> pair = KeyValueStorage("task1.txt")
        >>> pair['some_key']
        some_value

    """

    def __init__(self, path_to_file: str) -> None:
        with open(path_to_file) as data:
            key_and_value = data.read().strip().split()

        for pair in key_and_value:
            pair = pair.split("=")

            if self.__correct_attribute(pair[0]):
                try:
                    self.__setattr__(pair[0], int(pair[1]))
                except (ValueError, TypeError):
                    self.__setattr__(pair[0], pair[1])

    def __correct_attribute(self, attribute: str) -> Union[bool, None]:
        """Checks whether the received string object can be an attribute.

        Args:
            attribute: Possible attribute.

        Returns:
            True if successful.

        """
        if attribute[0] not in f"_{ascii_letters}":
            raise ValueError(f"the value {attribute} cannot be an attribute.")

        for char in attribute:
            if char not in f"_{ascii_letters}{digits}":
                raise ValueError(f"the value {attribute} cannot be an attribute.")

        if attribute not in self.__dir__():
            return True

    def __getitem__(self, key: str) -> Union[int, str]:
        return self.__dict__[key]

    def __setitem__(self, key: str, value: Union[int, str]) -> None:
        self.__dict__[key] = value



