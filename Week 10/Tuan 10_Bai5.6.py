class Polynomial:
    def __init__(self, coeffs: list):
        self.coeffs = list(coeffs)

    def __str__(self):
        terms = []
        n = len(self.coeffs) - 1  # The highest degree
        
        for i, coeff in enumerate(self.coeffs):
            if coeff == 0:
                continue
            
            power = n - i

            if power == 0:
                terms.append(str(coeff))
            else:
                if coeff == 1:
                    term_str = ""
                elif coeff == -1:
                    term_str = "-"
                else:
                    term_str = str(coeff)
                
                if power == 1:
                    terms.append(f"{term_str}x")
                else:
                    terms.append(f"{term_str}x^{power}")
                    
        if not terms:
            return "0"
            
        return ' + '.join(terms).replace('+ -', '- ')

    def __call__(self, x: float):
        result = 0
        n = len(self.coeffs) - 1
        for i, coeff in enumerate(self.coeffs):
            power = n - i
            result += coeff * (x ** power)
        return result

    def __add__(self, other):
        if isinstance(other, Polynomial):
            deg_self = len(self.coeffs)
            deg_other = len(other.coeffs)
            max_len = max(deg_self, deg_other)
            
            c1 = [0] * (max_len - deg_self) + self.coeffs
            c2 = [0] * (max_len - deg_other) + other.coeffs
            
            new_coeffs = [c1[i] + c2[i] for i in range(max_len)]

            while len(new_coeffs) > 1 and new_coeffs[0] == 0:
                new_coeffs.pop(0)
                
            return Polynomial(new_coeffs)
        return NotImplemented