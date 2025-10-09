"""
A clean Python module with no code quality issues.
This demonstrates that new clean code passes the quality gate.
"""

def add_numbers(a, b):
    """
    Add two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The sum of a and b
    """
    return a + b


def multiply_numbers(a, b):
    """
    Multiply two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The product of a and b
    """
    return a * b


if __name__ == "__main__":
    # Example usage
    result = add_numbers(5, 3)
    print(f"5 + 3 = {result}")
    
    result = multiply_numbers(4, 7)
    print(f"4 × 7 = {result}")