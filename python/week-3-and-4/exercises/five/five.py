letter = str(input("Enter a letter: "));

vowels = ["a", "e", "i", "o", "u"];

is_a_vowel = False;

for value in vowels:
  if value == letter:
    is_a_vowel = True
    break


if is_a_vowel:
  print("is vowel!!")
else:
  print("is consonant!!")