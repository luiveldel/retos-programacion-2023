# Created by luiveldel


# Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
# Ejemplos:
# - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
# - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"


class Number:
    def __init__(self, number):
        self.number = number
        
    def is_prime(self):
        if self.number <= 1:
            return False
        for i in range(2, int(self.number**0.5) + 1):
            if self.number % i == 0:
                return False
        return True
    
    def is_perfect_square(self, x):
        sqrt_x = int(x ** 0.5)
        return sqrt_x * sqrt_x == x

    def is_fibonacci(self):
        if self.number < 0:
            return False
        return self.is_perfect_square(5 * self.number * self.number + 4) or self.is_perfect_square(5 * self.number * self.number - 4)    
        
    def is_even(self):
        return self.number % 2 == 0
    
    def check_properties(self):  
        properties_str = f"{self.number}"
        properties_str += f"{' es primo' if self.is_prime() else ' no es primo'}"
        properties_str += f"{', es fibonacci' if self.is_fibonacci() else ', no es fibonacci'}"
        properties_str += f"{' y es par' if self.is_even() else ' y es impar'}"
        return properties_str      
        
user_input = int(input('Give me a number: '))
number_input = user_input or 'N/A'
number_instance = Number(number_input)
result = number_instance.check_properties()
print(result)