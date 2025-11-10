from armstrongchecker import ArmstrongChecker

for number in range(100, 501):
    if ArmstrongChecker.is_armstrong(number):
        print(f'{number} - число армстронга')