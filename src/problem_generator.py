import random
import math
from fractions import Fraction
from typing import List, Tuple, Dict, Union

class ProblemGenerator:
    def __init__(self):
        self.operators = ['+', '-', '×', '÷']
        self.poly_variables = ['x', 'y', 'z']
    
    def generate_problem(self, level: int = 1, problem_type: str = "basic") -> Tuple[str, Union[int, float, str]]:
        """
        Generate a math problem with given level and type.
        
        Args:
            level: Difficulty level from 1-10
            problem_type: "basic", "fraction", "polynomial", "algebra", "calculus"
        
        Returns:
            Tuple of (problem_string, answer)
        """
        if problem_type == "basic":
            return self._generate_basic_arithmetic(level)
        elif problem_type == "fraction":
            return self._generate_fraction_problem(level)
        elif problem_type == "polynomial":
            return self._generate_polynomial_problem(level)
        elif problem_type == "algebra":
            return self._generate_algebra_problem(level)
        elif problem_type == "calculus":
            return self._generate_calculus_problem(level)
        else:
            return self._generate_basic_arithmetic(level)
    
    def _generate_basic_arithmetic(self, level: int) -> Tuple[str, Union[int, float]]:
        """Generate basic arithmetic problems +-*/"""
        if level <= 3:
            # Level 1-3: Simple integers
            a = random.randint(1, 10 * level)
            b = random.randint(1, 10 * level)
            op = random.choice(['+', '-', '×'])
        elif level <= 6:
            # Level 4-6: Include division and larger numbers
            a = random.randint(10 * level, 100 * level)
            b = random.randint(1, 10 * level)
            op = random.choice(self.operators)
        else:
            # Level 7-10: Decimals and complex operations
            a = round(random.uniform(1, 100 * level/2), 1)
            b = round(random.uniform(1, 10 * level/2), 1)
            op = random.choice(self.operators)
        
        # Ensure valid operations
        if op == '÷' and b == 0:
            b = random.randint(1, 10)
        
        problem = f"{a} {op} {b}"
        
        # Calculate answer
        if op == '+':
            answer = a + b
        elif op == '-':
            answer = a - b
        elif op == '×':
            answer = a * b
        elif op == '÷':
            answer = round(a / b, 2)
        
        return problem, answer
    
    def _generate_fraction_problem(self, level: int) -> Tuple[str, Fraction]:
        """Generate fraction problems"""
        if level <= 3:
            # Simple fractions
            num1, den1 = random.randint(1, 5), random.randint(2, 6)
            num2, den2 = random.randint(1, 5), random.randint(2, 6)
            op = random.choice(['+', '-'])
        elif level <= 6:
            # Medium fractions with multiplication/division
            num1, den1 = random.randint(1, 10), random.randint(2, 12)
            num2, den2 = random.randint(1, 10), random.randint(2, 12)
            op = random.choice(self.operators)
        else:
            # Complex fractions
            num1, den1 = random.randint(1, 20), random.randint(2, 15)
            num2, den2 = random.randint(1, 20), random.randint(2, 15)
            op = random.choice(self.operators)
        
        frac1 = Fraction(num1, den1)
        frac2 = Fraction(num2, den2)
        
        problem = f"{frac1} {op} {frac2}"
        
        # Calculate answer
        if op == '+':
            answer = frac1 + frac2
        elif op == '-':
            answer = frac1 - frac2
        elif op == '×':
            answer = frac1 * frac2
        elif op == '÷':
            answer = frac1 / frac2
        
        return problem, answer
    
    def _generate_polynomial_problem(self, level: int) -> Tuple[str, str]:
        """Generate polynomial problems"""
        var = random.choice(self.poly_variables)
        
        if level <= 3:
            # Simple linear equations: ax + b = c
            a = random.randint(1, 5)
            b = random.randint(1, 10)
            c = a * random.randint(1, 5) + b
            problem = f"{a}{var} + {b} = {c}"
            answer = f"{var} = {(c - b) / a}"
            
        elif level <= 6:
            # Quadratic equations: ax² + bx + c = 0
            a = random.randint(1, 3)
            b = random.randint(-10, 10)
            c = random.randint(-10, 10)
            problem = f"{a}{var}² + {b}{var} + {c} = 0"
            
            # Calculate roots
            discriminant = b**2 - 4*a*c
            if discriminant >= 0:
                root1 = (-b + math.sqrt(discriminant)) / (2*a)
                root2 = (-b - math.sqrt(discriminant)) / (2*a)
                answer = f"{var} = {round(root1, 2)}, {round(root2, 2)}"
            else:
                answer = "No real roots"
                
        else:
            # Higher degree polynomials or systems
            degree = random.randint(2, min(3 + level//3, 5))
            coefficients = [random.randint(-5, 5) for _ in range(degree + 1)]
            
            terms = []
            for i, coef in enumerate(coefficients):
                if coef != 0:
                    if i == 0:
                        terms.append(str(coef))
                    elif i == 1:
                        terms.append(f"{coef}{var}")
                    else:
                        terms.append(f"{coef}{var}^{i}")
            
            problem = " + ".join(terms) + " = 0"
            answer = f"Polynomial of degree {degree} - solve for roots"
        
        return problem, answer
    
    def _generate_algebra_problem(self, level: int) -> Tuple[str, str]:
        """Generate algebra word problems"""
        problems = [
            # Level 1-3 problems
            ("If x + 5 = 12, what is x?", "7"),
            ("A number multiplied by 3 is 15. What is the number?", "5"),
            ("The sum of two consecutive numbers is 25. What are they?", "12 and 13"),
            
            # Level 4-6 problems
            ("Solve: 2(x + 3) = 16", "5"),
            ("A rectangle has length 2x and width x. If area is 50, find x.", "5"),
            ("The sum of three consecutive even numbers is 48. Find them.", "14, 16, 18"),
            
            # Level 7-10 problems
            ("A train travels 300 km. If speed was 10 km/h faster, it would take 1 hour less. Find original speed.", "50 km/h"),
            ("Solve the system: x + y = 10, 2x - y = 5", "x=5, y=5"),
            ("A invests $5000, B invests $3000. They share $2400 profit proportionally. How much does each get?", "A: $1500, B: $900")
        ]
        
        # Select problem based on level
        index = min(level - 1, len(problems) - 1)
        return problems[index]
    
    def _generate_calculus_problem(self, level: int) -> Tuple[str, str]:
        """Generate basic calculus problems"""
        if level <= 3:
            # Simple derivatives
            problems = [
                ("Find derivative of x²", "2x"),
                ("Find derivative of 3x + 5", "3"),
                ("Find derivative of sin(x)", "cos(x)")
            ]
        elif level <= 6:
            # More complex derivatives
            problems = [
                ("Find derivative of x³ - 2x² + 5x - 1", "3x² - 4x + 5"),
                ("Find derivative of e^x", "e^x"),
                ("Find derivative of ln(x)", "1/x")
            ]
        else:
            # Integrals and advanced calculus
            problems = [
                ("Find integral of 2x dx", "x² + C"),
                ("Find integral of 3x² dx", "x³ + C"),
                ("Find derivative of x·sin(x)", "sin(x) + x·cos(x)")
            ]
        
        return random.choice(problems)
    
    def generate_problem_set(self, count: int = 10, level: int = 1, 
                           problem_types: List[str] = None) -> List[Tuple[str, Union[int, float, str]]]:
        """Generate a set of problems"""
        if problem_types is None:
            problem_types = ["basic", "fraction", "polynomial", "algebra"]
        
        problems = []
        for _ in range(count):
            problem_type = random.choice(problem_types)
            problems.append(self.generate_problem(level, problem_type))
        
        return problems
    
    def get_available_problem_types(self) -> List[str]:
        """Return list of available problem types"""
        return ["basic", "fraction", "polynomial", "algebra", "calculus"]
    
    def get_level_description(self, level: int) -> str:
        """Get description of what each level includes"""
        descriptions = {
            1: "Basic arithmetic with small numbers",
            2: "Basic arithmetic with medium numbers",
            3: "Basic arithmetic with all operations",
            4: "Fractions and simple algebra",
            5: "Complex fractions and linear equations", 
            6: "Quadratic equations and word problems",
            7: "Polynomials and systems of equations",
            8: "Advanced algebra and basic calculus",
            9: "Complex calculus and real-world problems",
            10: "University-level mathematics"
        }
        if level > descriptions.__len__():
            raise ValueError(f"Level must be between 1 and {descriptions.__len__()}")
        return descriptions.get(level, "Advanced mathematics")


# Example usage and testing
if __name__ == "__main__":
    generator = ProblemGenerator()
    
    print("=== Problem Generator Demo ===")
    
    # Test different levels
    for level in range(1, 11):
        print(f"\n--- Level {level}: {generator.get_level_description(level)} ---")
        
        # Generate one of each type
        for p_type in generator.get_available_problem_types():
            try:
                problem, answer = generator.generate_problem(level, p_type)
                print(f"{p_type:>10}: {problem} = ? (Answer: {answer})")
            except:
                print(f"{p_type:>10}: [Error generating problem]")
    
    # Generate a problem set
    print(f"\n--- Problem Set (Level 5, 5 problems) ---")
    problem_set = generator.generate_problem_set(5, 5)
    for i, (problem, answer) in enumerate(problem_set, 1):
        print(f"{i}. {problem} = ? (Answer: {answer})")
        