from SwimRace import SwimRace, Swimmer

swimmer1 = Swimmer("Майкл Фелпс")
swimmer2 = Swimmer("Ян Торп")
    
print("До изменения имени:", swimmer1)
swimmer1.set_name("Майкл Фелпс (чемпион)")
print("После изменения имени:", swimmer1)
print()

race = SwimRace(swimmer1, swimmer2)
race.race()
print(race.announce_medal())