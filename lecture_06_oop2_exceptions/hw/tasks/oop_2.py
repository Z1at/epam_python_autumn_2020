"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную


1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)

HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'

    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания

2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.

3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования

4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.

    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
from __future__ import annotations

import datetime
from collections import defaultdict


class DeadlineError(Exception):
    """The deadline is now"""

    pass


class Homework:
    """Create a new Homework object from the given str object and int object.
    The text and deadline arguments are required.

    Args:
        text: A string representing the homework.
        deadline: Number of days to complete your homework.

    Attributes:
        text: A string representing the homework.
        deadline: Number of days to complete your homework.
        created: The time when the Homework instance was created.

    """

    def __init__(self, text: str, deadline: int) -> None:
        self.text = text
        self.deadline = datetime.timedelta(days=deadline)
        self.created = datetime.datetime.now()

    def is_active(self) -> bool:
        """Whether the time for completing your homework is up.

        Returns:
            True if successful, False otherwise.

        """
        return datetime.datetime.now() - self.created < self.deadline


class Person:
    """Creates a new Person object from the given str object and str object.
    Given str object and str object are the student's last name and first name.

    Args:
        first_name: First name of a person.
        last_name: Last name of a person.

    Attributes:
        first_name: First name of a person.
        last_name: Last name of a person.

    """

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Student(Person):
    """Creates a new Student object from the given str object and str object.
    Given str object and str object are the student's last name and first name.

    Args:
        first_name: First name of a student.
        last_name: Last name of a student.

    Attributes:
        first_name: First name of a student.
        last_name: Last name of a student.

    """

    def do_homework(self, hw: Homework, solution: str) -> HomeworkResult:
        """Whether the time for completing your homework is up.

        Args:
            hw: Homework instance.
            solution: The solution of the student.

        Returns:
            HomeworkResult instance if successful.

        Raises:
            DeadlineError: If the deadline for completing your homework is over.

        """
        if hw.is_active():
            return HomeworkResult(self, hw, solution)
        raise DeadlineError("You are late.")


class Teacher(Person):
    """Creates a new Teacher object from the given str object and str object.
    Given str object and str object are the teacher's last name and first name.

    Args:
        first_name: First name of a teacher.
        last_name: Last name of a teacher.

    Attributes:
        first_name: First name of a teacher.
        last_name: Last name of a teacher.

    """

    homework_done = defaultdict(dict)

    @staticmethod
    def create_homework(text: str, deadline: int) -> Homework:
        """Creates a Homework instance.

        Args:
            text: A string representing the homework.
            deadline: Number of days to complete your homework.

        Returns:
            Homework instance.

        """
        return Homework(text, deadline)

    @classmethod
    def check_homework(cls, hw_result: HomeworkResult) -> bool:
        """Checks if the solution is longer than 5 characters.

        Args:
            hw_result: HomeworkResult instance.

        Returns:
            True is successful, False otherwise.

        """
        if len(hw_result.solution) < 6:
            return False

        if hw_result.solution not in cls.homework_done[hw_result.homework]:
            cls.homework_done[hw_result.homework][hw_result.solution] = hw_result

        return True

    @staticmethod
    def reset_results(homework: Homework = None) -> None:
        """Deletes the Homework object from the homework_done or
        clears the entire homework_done.

        Args:
            homework: Homework object.

        """
        if homework:
            Teacher.homework_done.pop(homework, None)
        else:
            Teacher.homework_done = defaultdict(dict)


class HomeworkResult:
    """Accepts Student and Homework objects and also str object to create a result object.

    Args:
        author: Student object.
        homework: Homework object.
        solution: The solution presented by the student.

    Attributes:
        author: Student object.
        homework: Homework object.
        solution: The solution presented by the student.
        created: The time when HomeworkResult instance was created.

    """

    def __init__(self, author: Student, homework: Homework, solution: str) -> None:
        if not isinstance(homework, Homework):
            raise TypeError(
                f"{homework} is not a Homework object. "
                f"Second parameter must be Homework object."
            )
        self.author = author
        self.homework = homework
        self.solution = solution
        self.created = datetime.datetime.now()



if __name__ == '__main__':
    opp_teacher = Teacher('Daniil', 'Shadrin')
    advanced_python_teacher = Teacher('Aleksandr', 'Smetanin')

    lazy_student = Student('Roman', 'Petrov')
    good_student = Student('Lev', 'Sokolov')

    oop_hw = opp_teacher.create_homework('Learn OOP', 1)
    docs_hw = opp_teacher.create_homework('Read docs', 5)

    result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
    result_2 = good_student.do_homework(docs_hw, 'I have done this hw too')
    result_3 = lazy_student.do_homework(docs_hw, 'done')
    try:
        result_4 = HomeworkResult(good_student, "fff", "Solution")
    except Exception:
        print('There was an exception here')
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2

    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)

    print(Teacher.homework_done[oop_hw])
    Teacher.reset_results()
