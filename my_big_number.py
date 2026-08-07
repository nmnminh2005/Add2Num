import logging


class MyBigNumber:

    def sum(self, stn1, stn2, enable_logging=False):

        i = len(stn1) - 1
        j = len(stn2) - 1
        carry = 0

        result = bytearray(max(len(stn1), len(stn2)) + 1)
        position = len(result) - 1

        while i >= 0 or j >= 0 or carry:
            digit1 = int(stn1[i]) if i >= 0 else 0
            digit2 = int(stn2[j]) if j >= 0 else 0

            total = digit1 + digit2 + carry

            result[position] = (total % 10) + 48
            carry = total // 10

            if enable_logging:
                logging.info(
                    "Step: %d + %d + carry -> total=%d",
                    digit1,
                    digit2,
                    total
                )

            i -= 1
            j -= 1
            position -= 1

        if result[0] == 0:
            answer = result[1:].decode()
        else:
            answer = result.decode()

        if enable_logging:
            logging.info("Result: %s", answer)

        return answer