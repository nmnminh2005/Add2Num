import logging

# Standard logging setup (Console Output)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class MyBigNumber:
    """
    Core class to handle addition of two large numbers represented as strings.
    Simulates elementary school addition algorithm (right-to-left digit-by-digit).
    """
    def sum(self, stn1: str, stn2: str) -> str:
        i = len(stn1) - 1
        j = len(stn2) - 1
        carry = 0
        step = 1

        # Pre-allocate bytearray memory with fixed size (max_len + 1)
        result = bytearray(max(len(stn1), len(stn2)) + 1)
        position = len(result) - 1

        # Loop from right to left
        while i >= 0 or j >= 0 or carry:
            digit1 = int(stn1[i]) if i >= 0 else 0
            digit2 = int(stn2[j]) if j >= 0 else 0
            
            total = digit1 + digit2 + carry
            current_digit = total % 10
            new_carry = total // 10

            # English & Math notation step logging
            log_msg = f"Step {step}: {digit1} + {digit2} = {digit1 + digit2}"
            if carry > 0:
                log_msg += f" (+ carry {carry}) = {total}"
            log_msg += f" -> Save {current_digit}, Carry {new_carry}"
            logging.info(log_msg)

            # Direct ASCII writing (No append, No reverse)
            result[position] = current_digit + 48
            carry = new_carry

            i -= 1
            j -= 1
            position -= 1
            step += 1

        # Strip leading zero if unused
        if result[0] == 0:
            return result[1:].decode()
        return result.decode()