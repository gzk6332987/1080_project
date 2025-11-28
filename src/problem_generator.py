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
            return self._generate_algebra_problem()
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
    
    def _generate_algebra_problem(self) -> Tuple[str, str]:
        """Generate algebra word problems"""
        problems = [
            ("If x - 8 = 5, what is x? (answer: number)", "13"),
            ("A number divided by 4 is 6. What is the number? (answer: number)", "24"),
            ("If 3x = 27, what is x? (answer: number)", "9"),
            ("Solve for y: y + 12 = 20 (answer: number)", "8"),
            ("Solve: 5x - 2 = 18 (answer: number)", "4"),
            ("If 4(x - 1) = 16, what is x? (answer: number)", "5"),
            ("Solve: (x/3) = 9 (answer: number)", "27"),
            
            ("The sum of two consecutive numbers is 33. What are they? (answer: X and Y)", "16 and 17"),
            ("The sum of three consecutive integers is 72. Find them. (answer: X, Y, Z)", "23, 24, 25"),
            ("The sum of three consecutive odd numbers is 57. What are they? (answer: X, Y, Z)", "17, 19, 21"),
            ("Find two consecutive even numbers whose sum is 86. (answer: X and Y)", "42 and 44"),
            
            ("A square has side length x. Perimeter is 52. Find x. (answer: number)", "13"),
            ("A rectangle's length is 5 and width is x. Perimeter is 22. Find x. (answer: number)", "6"),
            ("A triangle has base 10 and height x. Area is 35. Find x. (answer: number)", "7"),
            ("A cube has volume 64 cubic cm. Side length? (answer: X cm)", "4 cm"),
            
            ("John is twice as old as Jane. Sum of ages is 36. How old is Jane? (answer: number)", "12"),
            ("The sum of ages of mother and daughter is 50. In 5 years, mother will be 3 times as old. Daughter's age now? (answer: number)", "10"),
            
            ("A car travels 240 km in 4 hours. What is its speed? (answer: XX km/h)", "60 km/h"),
            ("A train travels 420 km in 3 hours. Average speed? (answer: XXX km/h)", "140 km/h"),
            ("Bike at 15 km/h for 2 hours. Distance traveled? (answer: XX km)", "30 km"),
            ("Plane flies 1500 miles at 500 mph. How long? (answer: X hours)", "3 hours"),
            ("Two cars: one north at 60 km/h, one east at 80 km/h. Distance apart after 1 hour? (answer: XXX km)", "100 km"),
            
            ("Solve the system: x + y = 15, x - y = 3 (answer: x=X, y=Y)", "x=9, y=6"),
            ("Solve: 2x + y = 11, 3x - y = 9 (answer: x=X, y=Y)", "x=4, y=3"),
            ("The sum of two numbers is 20, difference is 8. What are they? (answer: X and Y)", "14 and 6"),
            
            ("Tickets: $5 children, $12 adults. 100 tickets sold for $790. Children attended? (answer: XX children)", "70 children"),
            ("Ratio boys to girls is 3:2. 15 boys. How many girls? (answer: XX girls)", "10 girls"),
            ("5 pencils cost $1.50. Cost of 12 pencils? (answer: $X.XX)", "$3.60"),
            ("Shirt costs $40 after 20% discount. Original price? (answer: $XX)", "$50"),
            ("What is 25% of 200? (answer: number)", "50"),
            ("Number increased by 20% becomes 180. Original number? (answer: number)", "150"),
            
            ("A invests $6000, B invests $4000. Share $2000 profit. A's share? (answer: $XXXX)", "$1200"),
            ("A, B, C invest $2000, $3000, $5000. Share $5000 profit. How much more does C get than A? (answer: $XXXX)", "$1500"),
            
            ("Pipe A fills tank in 3 hours, Pipe B in 6 hours. How long with both? (answer: X hours)", "2 hours"),
            ("Worker A: 8 hours, Worker B: 12 hours. How long together? (answer: X.X hours)", "4.8 hours"),
            ("4 machines do job in 6 hours. How long for 6 machines? (answer: X hours)", "4 hours"),
            
            ("Product of two consecutive integers is 132. What are they? (answer: X and Y)", "11 and 12"),
            ("Rectangle length is 3 more than width. Area is 40. Dimensions? (answer: X and Y)", "8 and 5"),
            ("A number squared is 81. What is the number? (answer: X or -X)", "9 or -9"),
            ("Square of a number minus the number is 42. What is the number? (answer: X or -X)", "7 or -6"),
            ("Right triangle: hypotenuse 10 cm, one leg 6 cm. Other leg? (answer: X cm)", "8 cm"),
            
            ("Train travels 300 km. If speed was 10 km/h faster, it would take 1 hour less. Original speed? (answer: XX km/h)", "50 km/h"),
            ("Solve the system: x + y = 10, 2x - y = 5 (answer: x=X, y=Y)", "x=5, y=5"),
            ("A invests $5000, B invests $3000. Share $2400 profit. How much each? (answer: A: $XXXX, B: $XXXX)", "A: $1500, B: $900")
        ]
        # Select problem based on random number
        index = random.randint(0, len(problems) - 1)            

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
                ("Find derivative of x^3-2x^2+5x-1", "3x^2-4x+5"),
                ("Find derivative of e^x", "e^x"),
                ("Find derivative of ln(x)", "1/x")
            ]
        else:
            # Integrals and advanced calculus
            problems = [
                ("Find integral of 2x dx", "x^2+C"),
                ("Find integral of 3x² dx", "x^3+C"),
                ("Find derivative of x·sin(x), use *", "sin(x)+x*cos(x)")
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
        