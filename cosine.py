from math import sqrt
import re
from collections import Counter


def cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in list(vec1.keys())])
    sum2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])
    denominator = sqrt(sum1) * sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return round(float(numerator)/denominator, 6)
    

WORD = re.compile(r"\w+")
def conv_vec(text):
    words = WORD.findall(text)
    return Counter(words)


# sentence1 = "".lower()
# sentence2 ="".lower()



# vect1 = conv_str_to_vec(sentence1)
# vect2 = conv_str_to_vec(sentence2)

# result = cosine(vect1, vect2)

# print("Cosine Similarity(words similar)", sentence1 , "and", sentence2, "is", result)