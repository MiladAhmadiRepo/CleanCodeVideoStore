import unittest

unittest.TestLoader.sortTestMethodsUsing = None
from Main.Statement import Statement
from Main.Movie import Movie
from Main.Rental import Rental


class VideoStoreTest(unittest.TestCase):
    def setUp(self):
        print("Starting all the tests.")
        self.statement = Statement("Customer")

    def test_0000_testSingleNewReleaseStatementTotals(self):
        self.statement.addRental(Rental(Movie("The Cell", Movie.NEW_RELEASE), 3))
        # self.assertEqual("Rental Record for Fred\n"
        #                  "\tThe Cell\t9.0\n"
        #                  "You owed 9.0\n"
        #                  "You earned 2 frequent renter points\n"
        #                  , self.customer.statement())
        self.statement.generate()
        self.assertEqual(9.0, self.statement.getTotal())
        self.assertEqual(2, self.statement.getFrequentRenterPoints())

    def test_0001_testDualNewReleaseStatementTotals(self):
        self.statement.addRental(Rental(Movie("The Cell", Movie.NEW_RELEASE), 3))
        self.statement.addRental(Rental(Movie("The Tigger Movie", Movie.NEW_RELEASE), 3))
        # self.assertEqual("Rental Record for Fred\n"
        #                  "\tThe Cell\t9.0\n"
        #                  "\tThe Tigger Movie\t9.0\n"
        #                  "You owed 18.0\nYou earned 4 frequent renter points\n",
        #                  self.statement.generate())

        self.statement.generate()
        self.assertEqual(18.0, self.statement.getTotal())
        self.assertEqual(4, self.statement.getFrequentRenterPoints())

    def test_0010_testSingleChildrensStatementTotals(self):
        self.statement.addRental(Rental(Movie("The Tigger Movie", Movie.CHILDRENS), 3))
        # self.assertEqual("Rental Record for Fred\n"
        #                  "\tThe Tigger Movie\t1.5\n"
        #                  "You owed 1.5\n"
        #                  "You earned 1 frequent renter points\n",
        #                  self.statement.generate())

        self.statement.generate()
        self.assertEqual(1.5, self.statement.getTotal())
        self.assertEqual(1, self.statement.getFrequentRenterPoints())

    def test_0100_testMultipleRegularStatementTotals(self):
        self.statement.addRental(Rental(Movie("Plan 9 from Outer Space", Movie.REGULAR), 1))
        self.statement.addRental(Rental(Movie("8 1/2", Movie.REGULAR), 2))
        self.statement.addRental(Rental(Movie("Eraserhead", Movie.REGULAR), 3))
        # self.assertEqual("Rental Record for Fred\n"
        #                  "\tPlan 9 from Outer Space\t2.0\n"
        #                  "\t8 1/2\t2.0\n"
        #                  "\tEraserhead\t3.5\n"
        #                  "You owed 7.5\nYou earned 3 frequent renter points\n",
        #                  self.statement.generate())
        self.statement.generate()
        self.assertEqual(7.5, self.statement.getTotal())
        self.assertEqual(3, self.statement.getFrequentRenterPoints())

    def test_0101_testMultipleRegularStatementFormat(self):
        self.statement.addRental(Rental(Movie("Plan 9 from Outer Space", Movie.REGULAR), 1))
        self.statement.addRental(Rental(Movie("8 1/2", Movie.REGULAR), 2))
        self.statement.addRental(Rental(Movie("Eraserhead", Movie.REGULAR), 3))
        self.assertEqual("Rental Record for Customer\n"
                         "\tPlan 9 from Outer Space\t2.0\n"
                         "\t8 1/2\t2.0\n"
                         "\tEraserhead\t3.5\n"
                         "You owed 7.5\nYou earned 3 frequent renter points\n",
                         self.statement.generate())

if __name__ == '__main__':
    unittest.main()
