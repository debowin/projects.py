__author__ = 'debojeet.chatterjee'

tokens_large = ["Thousand", "Million", "Billion", "Trillion", "Quadrillion", "Quintillion", "Sextillion", "Septillion", "Octillion", "Nonillion"]

tokens_small = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "10": "Ten",
    "11": "Eleven",
    "12": "Twelve",
    "13": "Thirteen",
    "14": "Fourteen",
    "15": "Fifteen",
    "16": "Sixteen",
    "17": "Seventeen",
    "18": "Eighteen",
    "19": "Nineteen",
    "20": "Twenty",
    "30": "Thirty",
    "40": "Forty",
    "50": "Fifty",
    "60": "Sixty",
    "70": "Seventy",
    "80": "Eighty",
    "90": "Ninety"
}


def num2alpha(num, alpha):
    if num[0] != '0':
        alpha.append(tokens_small[num[0]])
        alpha.append("Hundred and")
    if num[1:3] in tokens_small.keys():
        alpha.append(tokens_small[num[1:3]])
    else:
        if num[1] != '0':
            alpha.append(tokens_small[num[1] + "0"])
        if num[2] != '0':
            alpha.append(tokens_small[num[2]])
    large_index = len(num)/3 - 2
    if 0 <= large_index < len(tokens_large):
        alpha.append(tokens_large[large_index]+',')
    num = num[3:]
    if not num:
        return
    num2alpha(num, alpha)


def main():
    num = raw_input("Enter a number: ")
    alpha = []
    if len(num) % 3 == 1:
        num = "00" + num
    elif len(num) % 3 == 2:
        num = "0" + num
    num2alpha(num, alpha)
    print " ".join(alpha)


if __name__ == "__main__":
    main()