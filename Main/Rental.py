from Main.Movie import Movie


class Rental:

    def __init__(self,movie, daysRented):
        self._movie = movie
        self._daysRented = daysRented
    # ----------------------------------------------------------------------------------------------------------

    def getDaysRented(self):
        return self._daysRented
    # ----------------------------------------------------------------------------------------------------------

    def getMovie(self):
        return self._movie
    # ----------------------------------------------------------------------------------------------------------

    def getTitle(self):
        return self._movie.getTitle()
    # ----------------------------------------------------------------------------------------------------------

    def rentalDeterminesAmount(self):
        return self._movie.determinesAmount(self._daysRented)

    # ----------------------------------------------------------------------------------------------------------

    def rentalDetermineFrequentRenterPoints(self):
       return  self._movie.determineFrequentRenterPoints(self._daysRented)