#give repeated words count
#use function and do thats good...


sentence = input("Enter a sentence: ")
words = sentence.split()

word_count = {}
for w in words:
    w = w.strip(".,!?:;")
    if w in word_count:
        word_count[w] += 1
    else:
        word_count[w] = 1

for w, count in word_count.items():
    print(f"{w}: {count}")