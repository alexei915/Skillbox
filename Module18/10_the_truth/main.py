def encrypt(text):
    translate = ''
    for char in text:
        if char in letters:
            char_index = letters.find(char)
            translate += letters[char_index - 1]
        else:
            translate += char
    return translate


letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
message = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou ' \
          'fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf' \
          ' uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ' \
          'ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq ' \
          'odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. ' \
          'boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ' \
          'ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op ' \
          'gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up ' \
          'bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'


new_message = []
x = -3
y = encrypt(message).split()

for word in y:
    if len(word) > abs(x):
        new_message.append(word[x:] + word[:x])
    if len(word) < abs(x):
        new_message.append(word[x % len(word):] + word[:x % len(word)])
    if '/' in word:
        x -= 1

final_text = ' '.join(new_message).replace('/', '.\n').replace('..', '-').\
    replace('+', '').replace('(', "'").replace('"', '!')
print(final_text)
