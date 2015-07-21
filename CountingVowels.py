s = 'azcbobobegghakl'

numberOfVowels = 0

for x in range (0, len(s)):
    if s[x] in 'aeiou':
        numberOfVowels += 1

print "Number of vowels: " + str(numberOfVowels)