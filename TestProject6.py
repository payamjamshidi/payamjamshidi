#WordCounter

WordCounter = input("please enter your farases: ")

count = 0
i = 0

while i < len(WordCounter):
    if WordCounter[i] == ' ':
        count += 1

        while i < len(WordCounter) and WordCounter[i] == ' ':
            i += 1
    else:
        i += 1

if count == 0 and len(WordCounter.strip()) > 0:
    print("count of word is ", 1)
else:
    print("count of word is ", count+1)

     