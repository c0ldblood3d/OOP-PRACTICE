from datetime import *

class Membership:
    def __init__(self, member_name, membership_type, join_date):
        self.__member_name = member_name
        self.__membership_type = membership_type
        self.__join_date = join_date

    def get_member_name(self):
        return self.__member_name
    
    def get_membership_type(self):
        return self.__membership_type
    
    def get_join_date(self):
        return self.__join_date
    
    def membership_duration(self):
        today = date.today()
        years_difference = today.year - self.__join_date.year
        if (today.month, today.day) < (self.__join_date.month, self.__join_date.day):
            years_difference -= 1
        return years_difference
