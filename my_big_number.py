# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 12:29:29 2026

@author: Owner
"""


class MyBigNumber:

    def sum(self, stn1, stn2):
        i = len(stn1) - 1
        j = len(stn2) - 1

        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:

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

        result.reverse()

        return "".join(result)