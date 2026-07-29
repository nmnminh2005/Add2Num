import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)


class MyBigNumber:

    def sum(self, stn1, stn2):
        logging.info("Starting addition: %s + %s", stn1, stn2)

        i = len(stn1) - 1
        j = len(stn2) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry > 0:
            digit1 = 0
            digit2 = 0

            if i >= 0:
                digit1 = ord(stn1[i]) - ord('0')
                i -= 1

            if j >= 0:
                digit2 = ord(stn2[j]) - ord('0')
                j -= 1

            total = digit1 + digit2 + carry
            result.append(str(total % 10))
            carry = total // 10

            logging.info(
                "Step: %d + %d + carry = %d",
                digit1,
                digit2,
                total
            )

        result.reverse()
        answer = "".join(result)

        logging.info("Result: %s", answer)

        return answer