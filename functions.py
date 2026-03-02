def add(a, b):
    return a + b


def is_even(n):
    return n % 2 == 0


def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def count_vowels(s):
    vowels = "aeiou"
    return sum(1 for ch in s.lower() if ch in vowels)


def first_word(text):
    return text.split()[0]