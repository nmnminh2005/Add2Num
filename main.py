import logging
from my_big_number import MyBigNumber

def main():
    logging.getLogger().setLevel(logging.INFO)
    
    calculator = MyBigNumber()
    num1 = "1235"
    num2 = "897"
    
    print(f"=== Calculating: {num1} + {num2} ===")
    result = calculator.sum(num1, num2)
    print(f"==> RESULT: {result}")

if __name__ == "__main__":
    main()