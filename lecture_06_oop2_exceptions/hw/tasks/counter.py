"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров, возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования

"""
import functools


def instances_counter(cls: type) -> type:
    """A decorator that is applied to a class and adds two new methods to it:
    - get_created_instances
    - reset_instances_counter

    Args:
        cls: Reference to the class.

    Returns:
        A reference to a class with two new methods.

    """
    cls.__instance_counter = 0

    link_to_the_old_init = cls.__init__

    @functools.wraps(cls.__init__)
    def __init__(self, *args, **kwargs):
        cls.__instance_counter += 1

        return link_to_the_old_init(self, *args, **kwargs)

    cls.__init__ = __init__

    @classmethod
    def get_created_instances(cls: type) -> type:
        """Counts the number of instances of the class.

        Args:
            cls: Reference to the class.

        Returns:
            The number of instances of the class.

        """
        return cls.__instance_counter

    cls.get_created_instances = get_created_instances

    @classmethod
    def reset_instances_counter(cls: type) -> type:
        """Resets the instance counter.

        Args:
            cls: Reference to the class.

        Returns:
            The number of instances of the class before resetting.

        """
        local_instance_counter = cls.__instance_counter
        cls.__instance_counter = 0

        return local_instance_counter

    cls.reset_instances_counter = reset_instances_counter

    return cls


@instances_counter
class User:
    def __init__(self, num):
        self.num = num


if __name__ == "__main__":

    User.get_created_instances()  # 0
    User.__init__  # <function User.__init__ at 0x01CA85C8>
    user, _, _ = User(7), User(4), User(5)
    user.num  # 7
    _.num  # 5
    User.get_created_instances()  # 3
    user.get_created_instances()  # 3
    user.reset_instances_counter()  # 3
