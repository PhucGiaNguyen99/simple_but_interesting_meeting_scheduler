class Meeting:
    """Represent a single meeting with date and time information"""

    MONTH_NAMES = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }

    def __init__(self, title, day, month, year, start_time, duration):
        self._title = title
        self._day = day
        self._month = month
        self._year = year
        self._start_time = start_time
        self._duration = duration

    def __str__(self):
        return (
            "Title: "
            + self.title
            + "\nDate: "
            + self.month
            + "/"
            + self.day
            + "/"
            + self.year
            + "/nStart time: "
            + self.start_time
            + "/nDuration: "
            + self.duration
        )

    def is_earlier_than(self, otherMeeting: Meeting):
        """Method to if the current meeting is ealier than another meeting."""
        if self.year < otherMeeting._year:
            return True
        elif self._year > otherMeeting._year:
            return False
        else:
            if self._month < otherMeeting._month:
                return True
            elif self._month > otherMeeting._month:
                return False
            else:
                if self._day < otherMeeting._day:
                    return True
                elif self._day > otherMeeting._day:
                    return False

    def convert_month_to_string(self):
        """Method to convert the current month to a string."""
        return self.MONTH_NAMES[self._month]

    def get_month_number1(self, month_name):
        """Method to convert given month_name to month number."""
        for key, val in self.MONTH_NAMES.items():
            if val == month_name:
                return key
        return -1

    def get_month_number2(self, month_name):
        """Method to convert given month_name to month number."""
        key = next((k for k, v in self.MONTH_NAMES.items() if v == month_name), -1)
        return key
        
    def remove_month_pair_given_month_number():
        if self._month in self.MONTH_NAMES:
            self.MONTH_NAMES.pop(self._month)
            
    
    def remove_month_pair_given_month_name(self, month_name):
        for key, val in self.MONTH_NAMES.items():
            if val==month_name:
                self.MONTH_NAMES.pop(key)
        