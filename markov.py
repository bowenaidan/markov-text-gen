import random, sys

def genMarkov(input):
    # generates the actual markov chain
    markov = {}
    words = input.split(" ")
    index = 2

    for word in words[index:]:
        key = " ".join(words[(index-2):index])
        #slices words into groupings of 2
        if key in markov:
            markov[key].append(word)
        else:
            markov[key] = [word]
        index += 1
    return markov

def genText(markov):
    words = random.choice(list(markov.keys())).split(" ")
    text = " ".join(words) + " "
    # text = text + " "
    for _ in range(50):
        key = " ".join(words)
        if key in markov:
            newword = random.choice(markov[key])
            text += newword + " "
            words.pop(0)
            words.append(newword)
        else:
            break
    return text

def main():
    with open(sys.argv[1], encoding='utf8') as f:
        input = f.read()
    markov = genMarkov(input)
    text = genText(markov)
    print(text)

if __name__ == '__main__':
    main()