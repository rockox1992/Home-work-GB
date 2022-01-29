from random import choices, sample

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n, repeat):
    # jokes with repeat, if repeat True
    if repeat:
        for noun, adverb, adjective in zip(choices(nouns, k=n), choices(adverbs, k=n), choices(adjectives, k=n)):
            print(f'"{noun} {adverb} {adjective}"')
    elif n > len(adverbs):
        n = len(adverbs)
        for noun, adverb, adjective in zip(sample(nouns, k=n), sample(adverbs, k=n),
                                           sample(adjectives, k=n)):
            print(f'"{noun} {adverb} {adjective}"')
    else:
        for noun, adverb, adjective in zip(sample(nouns, k=n), sample(adverbs, k=n),
                                           sample(adjectives, k=n)):
            print(f'"{noun} {adverb} {adjective}"')


get_jokes(3, 0)
get_jokes(5, 1)
get_jokes(7, 0)
get_jokes(7, 1)
