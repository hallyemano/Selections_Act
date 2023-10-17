def find_chinese_zodiac_sign(year):
    zodiac_signs = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]
    year_difference = year - 1924

    zodiac_index = year_difference % 12
    return zodiac_signs[zodiac_index]

if __name__ == "__main__":
    year = int(input("Enter a year: "))
    zodiac_sign = find_chinese_zodiac_sign(year)
    print(f"The Chinese Zodiac sign for the year {year} is {zodiac_sign}.")






