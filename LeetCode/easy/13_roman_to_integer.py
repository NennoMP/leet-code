# https://leetcode.com/problems/roman-to-integer/

roman_numerals =  {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500, 
            'M': 1000
}

roman_subtractions =  {
                'IV': 4,
                'IX': 9,
                'XL': 40,
                'XC': 90,
                'CD': 400, 
                'CM': 900
}


class Solution:
    def romanToInt(self, s: str) -> int:
        result: int = 0

        i = 0
        n = len(s)
        while i < n:
            try:
                aux = s[i] + s[i+1]
                if aux in roman_subtractions:
                    result += roman_subtractions[aux]
                    i += 2
                else:
                    result += roman_numerals[s[i]]
                    i += 1
            except IndexError:
                result += roman_numerals[s[i]]
                i += 1

        return result