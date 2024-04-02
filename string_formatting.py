chars = "   Oui... j'ai sept chats!"
for ponctuaction in ['.', ',', '?', '!', "'"]:
    chars = chars.replace(ponctuaction, ' ')
chars_list = [word for word in chars.split(' ') if word != '']
print(chars_list)