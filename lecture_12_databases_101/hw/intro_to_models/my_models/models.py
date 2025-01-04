from __future__ import annotations

import datetime
from collections import defaultdict

from django.db import models


class DeadlineError(models.Model, Exception):
    """The deadline is now"""

    pass


class Homework(models.Model):
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

    text = models.CharField(max_length=50)
    deadline = models.DurationField()
    created = models.DateTimeField()

    def is_active(self) -> bool:
        """Whether the time for completing your homework is up.

        Returns:
            True if successful, False otherwise.

        """
        return (
            datetime.datetime.now(datetime.timezone.utc) - self.created < self.deadline
        )


class Person(models.Model):
    """Creates a new Person object from the given str object and str object.
    Given str object and str object are the student's last name and first name.

    Args:
        first_name: First name of a person.
        last_name: Last name of a person.

    Attributes:
        first_name: First name of a person.
        last_name: Last name of a person.

    """

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


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
            # return HomeworkResult(self, hw, solution)
            return HomeworkResult(
                author=self,
                homework=hw,
                solution=solution,
                created=datetime.datetime.now(datetime.timezone.utc),
            )
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
        return Homework(
            text=text,
            deadline=deadline,
            created=datetime.datetime.now(datetime.timezone.utc),
        )

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


class HomeworkResult(models.Model):
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

    author = models.ForeignKey(Student, on_delete=models.CASCADE, default=1)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE, default=1)
    solution = models.CharField(max_length=50)
    created = models.DateTimeField()


class OutOfAJob(models.Model):
    """For personal use."""

    class_var = models.CharField(max_length=50)
    class_var2 = models.CharField(max_length=50)
