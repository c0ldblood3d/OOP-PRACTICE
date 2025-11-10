class ArmstrongChecker:
    @staticmethod
    def is_armstrong(__number):
        num_str = str(__number)
        digits = len(num_str)
        total = 0
        for digit in num_str:
            total += int(digit) ** digits
        return total == __number