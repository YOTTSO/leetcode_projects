def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    latin_dictionary = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    arabic_dictionary = ['1', '5', '10', '50', '100', '500', '1000']
    arabic = []
    result = 0
    count = 0
    if len(s) < 1 or len(s) > 15:
        return ("bad length")
    for i in range(len(s)):
        if s[i] in latin_dictionary:
            if len(s) >= i + 3 and s[i:i + 3] == 'III':
                arabic.append('3')
                break
            elif len(s) >= i + 2 and s[i:i + 2] == 'II':
                arabic.append('2')
                break
            arabic.append(arabic_dictionary[latin_dictionary.index(s[i])])
        if int(arabic[i - count]) > int(arabic[i - 1 - count]):
            arabic[i - 1 - count] = str(int(arabic[i - count]) - int(arabic[i - 1 - count]))
            arabic.pop()
            count += 1
    for i in range(len(arabic)):
        result += int(arabic[i])
    return result


string = "MDCCCLXXXIV"
print(romanToInt(string))