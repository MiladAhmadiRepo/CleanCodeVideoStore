class Movie:
    CHILDRENS = 2
    REGULAR = 0
    NEW_RELEASE = 1

    # ----------------------------------------------------------------------------------------------------------

    # _title=""
    # _priceCode=0
    # ----------------------------------------------------------------------------------------------------------

    def __init__(self, title, priceCode):
        self._title = title
        self._priceCode = priceCode

    # ----------------------------------------------------------------------------------------------------------

    def getPriceCode(self):
        return self._priceCode

    # ----------------------------------------------------------------------------------------------------------

    def setPriceCode(self, code):
        self._priceCode = code

    # ----------------------------------------------------------------------------------------------------------

    def getTitle(self):
        return self._title
    # ----------------------------------------------------------------------------------------------------------

    def determinesAmount(self,_daysRented):
        _rentalAmount = 0
        if  self._priceCode == Movie.REGULAR:
            _rentalAmount += 2
            if _daysRented > 2:
                _rentalAmount += (_daysRented - 2) * 1.5
        elif self._priceCode == Movie.NEW_RELEASE:
            _rentalAmount += _daysRented * 3
        elif self._priceCode == Movie.CHILDRENS:
            _rentalAmount += 1.5
            if _daysRented > 3:
                _rentalAmount += (_daysRented- 3) * 1.5
        return _rentalAmount
    # ----------------------------------------------------------------------------------------------------------
    def determineFrequentRenterPoints(self,_daysRented):
        _bounsIsEarned=self._priceCode == Movie.NEW_RELEASE and _daysRented > 1
        if _bounsIsEarned:
            return 2
        return 1