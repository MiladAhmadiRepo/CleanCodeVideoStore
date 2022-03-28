from Main.Movie import Movie


class Statement:

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
        self.clearTotals()
        _statementText= self.header()
        _statementText += self.rentalLines()

        _statementText+= self.footer()

        return _statementText
    # ----------------------------------------------------------------------------------------------------------

    def clearTotals(self):
        self._totalAmount = 0
        self._frequentRenterPoints = 0

    # ----------------------------------------------------------------------------------------------------------

    def header(self):
        return "Rental Record for " + self.customerName + "\n"

    # ----------------------------------------------------------------------------------------------------------

    def rentalLines(self):
        rentalLines=""
        for rental in self.rentals:
            rentalLines += self.rentalLine(rental)
        return rentalLines
    # ----------------------------------------------------------------------------------------------------------

    def rentalLine(self, rental):

        _thisAmount =self.determinesAmount( rental)
        self._frequentRenterPoints +=self.determineFrequentRenterPoints(rental)
        self._totalAmount += _thisAmount
        return  self.rentalLineFormat(_thisAmount, rental)

    # ----------------------------------------------------------------------------------------------------------

    def rentalLineFormat(self, _thisAmount, rental):
        _rentalLine = ""
        _thisAmountFormat="{:.1f}".format(_thisAmount)
        _rentalLine += f"\t{rental.getMovie().getTitle()}\t{_thisAmountFormat}\n"
        return _rentalLine

    # ----------------------------------------------------------------------------------------------------------

    def determineFrequentRenterPoints(self, rental):
        _bounsIsEarned=rental.getMovie().getPriceCode() == Movie.NEW_RELEASE and rental.getDaysRented() > 1
        if _bounsIsEarned:
            return 2
        return 1

    # ----------------------------------------------------------------------------------------------------------

    def determinesAmount(self, rental):
        _rentalAmount=0
        if rental.getMovie().getPriceCode() == Movie.REGULAR:
            _rentalAmount += 2
            if rental.getDaysRented() > 2:
                _rentalAmount += (rental.getDaysRented() - 2) * 1.5
        elif rental.getMovie().getPriceCode() == Movie.NEW_RELEASE:
            _rentalAmount += rental.getDaysRented() * 3
        elif rental.getMovie().getPriceCode() == Movie.CHILDRENS:
            _rentalAmount += 1.5
            if rental.getDaysRented() > 3:
                _rentalAmount += (rental.getDaysRented() - 3) * 1.5
        return _rentalAmount

    # ----------------------------------------------------------------------------------------------------------

    def footer(self):
        self._totalAmountText="{:.1f}".format(self._totalAmount)
        self._frequentRenterPointsText=str(self._frequentRenterPoints)
        return f"You owed {self._totalAmountText}\nYou earned {self._frequentRenterPointsText} frequent renter points\n"

    # ----------------------------------------------------------------------------------------------------------

    def getTotal(self):
        return self._totalAmount

    # ----------------------------------------------------------------------------------------------------------

    def getFrequentRenterPoints(self):
        return self._frequentRenterPoints
