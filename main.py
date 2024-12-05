import string

def clean_string(s):
    return ''.join(c.lower() for c in s if c.isalpha())

#check if the string is a palindrome
def is_palindrome(s):
    s = clean_string(s)
    
    # If string is empty or has one character it's a palindrome
    if len(s) <= 1:
        return True
    #Check first and last characters
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

#count vowels and consonants
def count_vowels_and_consonants(s):
    vowels = "aeiou"
    
    # Clean the string first
    s = clean_string(s)
    
    # Base case: If the string is empty, return 0 vowels and consonants
    if len(s) == 0:
        return (0, 0)
    
    # Check the first character and recurse for the rest of the string
    first_char = s[0]
    rest_vowels, rest_consonants = count_vowels_and_consonants(s[1:])
    
   
    if first_char in vowels:
        return (rest_vowels + 1, rest_consonants)
   
    elif first_char.isalpha():
        return (rest_vowels, rest_consonants + 1)
    
    return (rest_vowels, rest_consonants)

#determine if the string is a palindrome and if it has more vowels than consonants
def analyze_string(s):
    palindrome_result = is_palindrome(s)
    vowels, consonants = count_vowels_and_consonants(s)
    
    print(f"Is the string a palindrome? {palindrome_result}")
    print(f"Number of vowels: {vowels}")
    print(f"Number of consonants: {consonants}")
    
    if vowels > consonants:
        print("The string has more vowels than consonants.")
    else:
        print("The string has more consonants than vowels.")

# Example
input_string = "A man, a plan, a canal, Panama!"
analyze_string(input_string)

