from Main.Rental import Rental


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

    def getTotal(self):
        return self._totalAmount

    # ----------------------------------------------------------------------------------------------------------

    def getFrequentRenterPoints(self):
        return self._frequentRenterPoints

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

        _thisAmount = rental.rentalDeterminesAmount()
        self._frequentRenterPoints += rental.rentalDetermineFrequentRenterPoints()
        self._totalAmount += _thisAmount
        return  self.rentalLineFormat(_thisAmount, rental)

    # ----------------------------------------------------------------------------------------------------------

    def rentalLineFormat(self, _thisAmount, rental):
        _rentalLine = ""
        _thisAmountFormat="{:.1f}".format(_thisAmount)
        _rentalLine += f"\t{rental.getTitle()}\t{_thisAmountFormat}\n"
        return _rentalLine


    # ----------------------------------------------------------------------------------------------------------

    def footer(self):
        self._totalAmountText="{:.1f}".format(self._totalAmount)
        self._frequentRenterPointsText=str(self._frequentRenterPoints)
        return f"You owed {self._totalAmountText}\nYou earned {self._frequentRenterPointsText} frequent renter points\n"

    # ----------------------------------------------------------------------------------------------------------
