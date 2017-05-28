deadMan = {'post': {'horizontal': ('|'.ljust(5, u"\u203E")), 
                   'vertical': '|\n'},
            'head': 'O'.rjust(5),
            'body': '|',
            'armLeft': '/',
            'armRight': '\\',
            'legLeft': '/',
            'legRight': '\\',
            'noose': '|'}


post = [deadMan['post']['horizontal'],
    deadMan['post']['vertical'] * 4]

print(deadMan['post']['horizontal'])
print(deadMan['post']['vertical'].strip() + deadMan['head'])
print(deadMan['post']['vertical'] * 2)

