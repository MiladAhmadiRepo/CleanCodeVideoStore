from Main.Movie import Movie


class Statement:
    # _name = ""
    # _rentals = []

    # ----------------------------------------------------------------------------------------------------------

    # default constructor
    def __init__(self, customerName):
        self.customerName = customerName
        self.rentals=[]

    # ----------------------------------------------------------------------------------------------------------

    def addRental(self, rental):
        self.rentals.append(rental)

    # ----------------------------------------------------------------------------------------------------------

    def getCustomerName(self):
        return self.customerName

    # ----------------------------------------------------------------------------------------------------------

    def generate(self):
        self.initialize()
        _statementText= self.header()
        _statementText = self.rentalLines(_statementText)

        _statementText+= "You owed " + "{:.1f}".format(self._totalAmount) + "\n"
        _statementText+= "You earned " + str(self._frequentRenterPoints) + " frequent renter points\n"

        return _statementText
    # ----------------------------------------------------------------------------------------------------------

    def rentalLines(self, _statementText):
        for rental in self.rentals:
            _thisAmount = 0
            # determines the amount for each line
            if rental.getMovie().getPriceCode() == Movie.REGULAR:
                _thisAmount += 2
                if rental.getDaysRented() > 2:
                    _thisAmount += (rental.getDaysRented() - 2) * 1.5
            elif rental.getMovie().getPriceCode() == Movie.NEW_RELEASE:
                _thisAmount += rental.getDaysRented() * 3
            elif rental.getMovie().getPriceCode() == Movie.CHILDRENS:
                _thisAmount += 1.5
                if rental.getDaysRented() > 3:
                    _thisAmount += (rental.getDaysRented() - 3) * 1.5

            self._frequentRenterPoints += 1
            if rental.getMovie().getPriceCode() == Movie.NEW_RELEASE and rental.getDaysRented() > 1:
                self._frequentRenterPoints += 1
            _statementText += "\t" + rental.getMovie().getTitle() + "\t" + "{:.1f}".format(_thisAmount) + "\n"
            self._totalAmount += _thisAmount
        return _statementText

    # ----------------------------------------------------------------------------------------------------------

    def header(self):
        return "Rental Record for " + self.customerName + "\n"

    # ----------------------------------------------------------------------------------------------------------

    def initialize(self):
        self._totalAmount = 0
        self._frequentRenterPoints = 0

    # ----------------------------------------------------------------------------------------------------------
    def getTotal(self):
        return self._totalAmount
    # ----------------------------------------------------------------------------------------------------------

    def getFrequentRenterPoints(self):
        return self._frequentRenterPoints
