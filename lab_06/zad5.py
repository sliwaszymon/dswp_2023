import codecs
# przez anakondę mam problemy z pipem więc będzie łopatologicznie
group1 = 'AĄBCĆDEĘFGHIJKLM'
group2 = 'NŃOÓPRSŚTUVWXYZŹŻ'

nazwiska = ['Śliwa', 'Martyniuk', 'Albrecht']

def foo(nazwiska):
    # A-M_nazwiska.txt
    # N-Ż_nazwiska.txt
    gr1 = [x for x in nazwiska if x[0] in list(group1)]
    gr2 = [x for x in nazwiska if x[0] in list(group2)]
    # nie mam zbytnio czasu, tak bym coś pokombinował z popem z "nazwiska", mam wrażenie że mogło by być bardziej optymalne
    with codecs.open('A-M_nazwiska.txt', 'w', 'utf-8-sig') as f:
        for x in gr1:
            f.write(x + '\n') 
    with codecs.open('N-Ż_nazwiska.txt', 'w', 'utf-8-sig') as f:
        for x in gr2:
            f.write(x + '\n')

foo(nazwiska)