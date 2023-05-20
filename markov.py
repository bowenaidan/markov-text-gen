import random
import sys

def genMarkov(input):
    # generates the actual Markov chain
    markov = {}
    words = input.split(" ")
    index = 2

    for word in words[index:]:
        key = " ".join(words[(index-2):index])
        if key in markov:
            if word in markov[key]:
                markov[key][word] += 1
            else:
                markov[key][word] = 1
        else:
            markov[key] = {word: 1}
        index += 1
    return markov

def genText(markov):
    words = random.choice(list(markov.keys())).split(" ")
    text = " ".join(words) + " "
    for _ in range(50):
        key = " ".join(words)
        if key in markov:
            next_words = markov[key]
            choices = []
            weights = []
            for word, weight in next_words.items():
                choices.append(word)
                weights.append(weight)
            addition = random.choices(choices, weights=weights)[0]
            text += addition + " "
            words.pop(0)
            words.append(addition)
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
