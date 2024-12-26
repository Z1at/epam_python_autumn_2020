"""
Task
Write a wrapper class TableData for database table,
that when initialized with database name and table acts as collection object
(implements Collection protocol). Assume all data has unique values in 'name' column.
So, if presidents = TableData(database_name='example.sqlite', table_name='presidents')

then
    len(presidents) will give current amount of rows in presidents table in database
    presidents['Yeltsin'] should return single data row for president with name Yeltsin
    'Yeltsin' in presidents should return if president with same name exists in table
    object implements iteration protocol. i.e. you could use it in for loops::
        for president in presidents:
            print(president['name'])
    all above mentioned calls should reflect most recent data.
    If data in table changed after you created collection instance,
    your calls should return updated data.

Avoid reading entire table into memory. When iterating through records,
start reading the first record, then go to the next one, until records are exhausted.
When writing tests, it's not always neccessary to mock database calls completely.
Use supplied example.sqlite file as database fixture file.

"""
import sqlite3
from typing import Tuple, Union


class TableData:
    """implements Collection protocol and Iterator protocol
    for working with the database.

    Args:
        database_name: Database name.
        table_name: Table name.

    Attributes:
        database_name: Database name.
        table_name: Table name.
        new_connection: Creates a new database connection.
        rows: Contains the name of the person and a row related to him.
        existing_names: Existing names in the database.

    """

    def __init__(self, database_name: str, table_name: str) -> None:
        self.database_name = database_name
        self.table_name = table_name
        self.next_is_not_used = True

    def __len__(self) -> int:
        """Counts the number of rows in the database.

        Returns:
            The number of rows in the database.

        """
        return sum(1 for _ in self.__new_connection())

    def __getitem__(self, item: str) -> Union[Tuple, None]:
        """Allows you to access the database by 'name' column.

        Args:
            item: Str object.

        Returns:
            A row in the form of a tuple.

        """
        for row in self.__new_connection():
            if row[0] == item:
                return row

    def __contains__(self, item: str) -> bool:
        """Checks whether an item exists in database.

        Args:
            item: Item to check.

        Returns:
            True if successful, False otherwise.

        """
        for row in self.__new_connection():
            if row[0] == item:
                return True
        return False

    def __iter__(self):
        return self

    def __next__(self) -> Tuple:
        """Generates the next row in the database.

        Returns:
            A row in the database.

        """
        if self.next_is_not_used:
            self.next_is_not_used = False
            self.new_connection = self.__new_connection()
            return next(self.new_connection)
        return next(self.new_connection)

    def __new_connection(self) -> Tuple:
        """Establishes a connection to the database.

        Returns:
            A row in the database.

        """
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()

        data = c.execute(f"SELECT * FROM {self.table_name}")

        for row in data:
            yield row

        conn.close()

        self.next_is_not_used = True
