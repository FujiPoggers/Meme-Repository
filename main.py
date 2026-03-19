word = input('Digite uma palavra moderna que você não entende (escreva toda a palavra em letras maiúsculas')

meme_dict = {
            'BRAINROT': 'um tipo de meme sem sentido, de baixa qualidade',
            'CRINGE': 'Investigar a vida de alguém online',
            'TANKAR': 'aguentar alguma situação, seja fisicamente ou psicologicamente',
            'GAP': 'é basicamente ser humilhado de alguma forma, por exemplo: se seu time de futebol perder de 10x2, ele levou gap',
            'INTANKAVEL': 'é quando algo é TÃO vergonhoso, TÃO ridículo que é simplesmente impossível de aguentar'
}

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print('Sua palavra não foi encontrada!')
