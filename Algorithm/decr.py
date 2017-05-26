import RC5
import key_expand


def decr(lefty, righty, keyy, roundss, length):
    roundss = int(roundss)
    size = len(keyy)
    keyy = key_expand.keyexpansion(keyy, size, roundss)
    text = [0] * len(lefty)
    for y in range(len(lefty)):
        text[y] = RC5.DEC(lefty[y], righty[y], keyy, roundss)
    tex = ''.join(text)
    tex = tex[:length]
    return tex
