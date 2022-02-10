# Напишите программу, удаляющую из текста все слова содержащие "абв"
x = 'абв'
text = 'ujoiwvciqnmopvi, абв jioawnckdkабв jioand'

def replace (x, st):
    txt = st.split()
    text_new = ''
    for i in range (len(txt)):
        if txt[i].find(x) == -1:
            text_new += txt[i] + ' '
    return text_new

print(replace(x,text))