def count_vowels(text):
    vowels = "aeiou"
    
    if len(text)==0:
     return 0

    first_char = text[0].lower()
    is_vowel = 1 if first_char in vowels else 0
    return is_vowel + count_vowels(text[1:])

phrase = "I love python"
result = count_vowels(phrase)
print("Number of vowels", result)

print(" ")

numbers = [40, 35, 10, 15, 20]
squared = list(map(lambda x : x*x,numbers))
print(squared)