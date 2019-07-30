from nltk.corpus import wordnet as wn
import nlp

def tokens(s):
    p=nlp.nlp(s)
    token=[]
    for i in p:
        token.append(i)
    for i in p:
        w=i
        synonyms = wn.synsets(w)
        l=list()
        t=[]

        for synset in synonyms:
            x=(synset.name().split('.')[0])
            j=synset.hyponyms()
            k=sorted(lemma.name() for m in j for lemma in m.lemmas())
            l.append(k)
            for k1 in k:
                t.append(k1)

        t1=[]
        for i in t:
            if i not in t1:
                t1.append(i)
        for i in t1:
            token.append(i)
    token1=[]
    for i in token:
        if i not in token1:
            token1.append(i)

    return token1