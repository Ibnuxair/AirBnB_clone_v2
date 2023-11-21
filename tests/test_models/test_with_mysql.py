#!/usr/bin/python3

"""
This module defines a class named TestMysql.
"""

import os
import unittest
import MySQLdb


class TestMysql(unittest.TestCase):
    """A class that Tests mysql."""

    @unittest.skipIf(
        os.getenv(
            "HBNB_TYPE_STORAGE") != 'db', "Skipping test: Not using MySQL")
    def test_create_state(self):
        # Connect to the MySQL database
        with MySQLdb.connect(host='localhost', user='hbnb_test',
                             passwd='hbnb_test_pwd', db='hbnb_test_db') as db:
            cursor = db.cursor()

            # Get the number of current records in the table states
            cursor.execute("SELECT COUNT(*) FROM states")
            initial_count = cursor.fetchone()[0]

            # Execute the SQL command to create a State named California
            cursor.execute("INSERT INTO states (name) VALUES ('California')")

            # Get the number of records in the table states after the command
            cursor.execute("SELECT COUNT(*) FROM states")
            final_count = cursor.fetchone()[0]

            # Check if the difference is +1
            self.assertEqual(final_count - initial_count, 1)

    if __name__ == '__main__':
        unittest.main()
