from membership import Membership
from datetime import *

member1 = Membership( "Иванов Иван " , "Золотой " , date (2018 , 3, 15))
member2 = Membership( "Петров Петр " , "Серебряный" , date (2020 , 6, 1))

print ("Член 1: ")
print ("Имя: " , member1.get_member_name () )
print ("Тип членства: " , member1.get_membership_type () )
print ("Дата вступления: " , member1.get_join_date () )
print ("Длительность членства : " , member1.membership_duration () )
print ("Член 2: ")
print ("Имя: " , member2.get_member_name () )
print ("Типч ленства: " , member2.get_membership_type () )
print ("Дата вступления: " , member2.get_join_date () )
print ("Длительность членства : " , member2.membership_duration () )