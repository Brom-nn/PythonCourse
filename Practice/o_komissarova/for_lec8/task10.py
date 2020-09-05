class Money:
    def __init__(self, rub, kop):
        self._rub = rub
        self._kop = kop

    @property
    def dollar_course(self):
        return self._dollar_course

    @dollar_course.setter
    def dollar_course(self, value):
        self._dollar_course = float(value)

    def convert(self):
        number = float(str(self).replace(",", "."))
        return number*self._dollar_course

    def __str__(self):
        return "{},{}".format(self._rub, self._kop)

    def __add__(self, other):
        if isinstance(other, Money):
            number1 = float(str(self).replace(",", "."))
            number2 = float(str(other).replace(",", "."))
            number3 = round(number1 + number2, 2)
            result = str(number3).split('.')
            money = Money(result[0], result[1])
            return money

    def __sub__(self, other):
        if isinstance(other, Money):
            number1 = float(str(self).replace(",", "."))
            number2 = float(str(other).replace(",", "."))
            number3 = round(number1 - number2, 2)
            result = str(number3).split('.')
            money = Money(result[0], result[1])
            return money

    def __mul__(self, other):
        if isinstance(other, Money):
            number1 = float(str(self).replace(",", "."))
            number2 = float(str(other).replace(",", "."))
            number3 = round(number1 * number2, 2)
            result = str(number3).split('.')
            money = Money(result[0], result[1])
            return money

    def __truediv__(self, other):
        if isinstance(other, Money):
            number1 = float(str(self).replace(",", "."))
            number2 = float(str(other).replace(",", "."))
            number3 = round(number1 / number2, 2)
            result = str(number3).split('.')
            money = Money(result[0], result[1])
            return money

    def __lt__(self, other):
        if isinstance(other, Money):
            number1 = float(str(self).replace(",", "."))
            number2 = float(str(other).replace(",", "."))
            if number1 < number2:
                return True
            return False

    def __gt__(self, other):
        if isinstance(other, Money):
            number1 = float(str(self).replace(",", "."))
            number2 = float(str(other).replace(",", "."))
            if number1 > number2:
                return True
            return False

    def __eq__(self, other):
        if isinstance(other, Money):
            number1 = float(str(self).replace(",", "."))
            number2 = float(str(other).replace(",", "."))
            if number1 == number2:
                return True
            return False


money1 = Money(20, 15)
money2 = Money(10, 21)
money3 = Money(20, 15)
print(money1, money2)
print(money1 + money2)
print(money1 - money2)
print(money1 * money2)
print(money1 / money2)
print(money1 < money2)
print(money1 > money2)
print(money1 == money3)
money1.dollar_course = 75.5
print(money1.convert())
