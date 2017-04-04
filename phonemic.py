#todo: fix the names of the variables
#todo: Use the stressed syllable to change phonemes

glas = set(u'яиюыаоэуе')

zvonk = list(u'бвгджзрлнм')

gluh = list(u'пфктшс')
myagk = set(u'бпвфдтзсгкчмлнр')
tverd = set(u'бпвфдтзскхмлнрцжшг')

strong = list(u'иеёюя')
strong_change = {k:v for k,v in zip(strong,list(u'ыэоуа'))}
strong = set(strong)

gluh_swap = {k:v for k,v in zip(zvonk[:6], gluh[:6])}
shitty_shit = set(u'жшщц')

zvonk = set(zvonk)
gluh = set(gluh)

def g2p_word(word):
    phonemes = []
    word = word.lower().strip()
    for i, c in enumerate(word):
        if c in {u'ъ',u'ь'}:
            continue
        if c in strong:
            if c==u'и':
                if i>0 and word[i-1] in shitty_shit:
                    phonemes.append(strong_change[c])
                else:
                    phonemes.append(c)
            elif i==0 or word[i-1] in {u'ъ',u'ь',' '} or word[i-1] in glas:
                phonemes.append(u'й')
                phonemes.append(strong_change[c])
            else:
                phonemes.append(strong_change[c])
        elif (i == len(word) - 1 or (i < len(word) - 1 and word[i+1] in gluh )) and c in gluh_swap:
            phonemes.append(gluh_swap[c])
        else:
            phonemes.append(c)
        if  c in sogl and ((not c in tverd ) or i < len(word) - 1 and c in myagk and (word[i+1] in strong or word[i+1] == u'ь')):
            phonemes[-1] = phonemes[-1]+'\''
        
    return phonemes
            
            
all_tokens = []+list(filter(lambda c: not c in strong,glas))+[c+'\'' for c in myagk] + list(tverd)
phoneme2token = {v:i for i,v in enumerate(all_tokens)}
