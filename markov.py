import random
import sys

def genMarkov(input):
    # generates the actual Markov chain
    markov = {}
    words = input.split(" ")
    index = 1
    size = index

    for word in words[index:]:
        window = " ".join(words[(index-size):index])
        if window in markov:
            # each window is a key for words
            # nested dictionary have words that are keys
            # words have weights
            if word in markov[window]:
                markov[window][word] += 1
            else:
                markov[window][word] = 1
        else:
            markov[window] = {word: 1}
        index += 1
    return markov

def genText(markov):
    #generates text
    words = random.choice(list(markov.keys())).split(" ")
    text = " ".join(words) + " "
    for _ in range(50):
        # joins the words to make a window
        window = " ".join(words)
        if window in markov:
            # checks the words in the window currently
            next_words = markov[window]
            choices = []
            weights = []
            #sets the choices and weights
            for word, weight in next_words.items():
                choices.append(word)
                weights.append(weight)
            addition = random.choices(choices, weights=weights)[0]
            text += addition + " "
            # slides the window up so it contains the new word
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
