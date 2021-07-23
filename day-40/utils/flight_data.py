class FlightData:
    """
    This class is responsible for structuring the flight data
    """
    def __init__(self, destination_city, destination_airport,
                 leave_date, return_date, price, stopovers=0, via_city=''):
        self.origin_airport = 'ORD'
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.leave_date = leave_date
        self.return_date = return_date
        self.price = price
        self.stopovers = stopovers
        self.via_city = via_city