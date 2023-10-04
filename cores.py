# padrao ansi   \033[0:30:40m - e ai muda entre [ m
#style 0 comum // 1 negrito // 4 sublinhado // 7 inverter configuração
#text do 30 ate 37 pode escolher as cores
#back fundo de letra 40 ate 47
print('\033[0:30:25m teste + \033[0:30:40m teste\33[m') # o \33[m serve para voltar o padrao original
print('\033[0:31:25m teste + \033[0:30:41m teste\33[m')
print('\033[0:32:25m teste + \033[0:30:42m teste\33[m')
print('\033[0:33:25m teste + \033[0:30:43m teste\33[m')
print('\033[0:34:25m teste + \033[0:30:44m teste\33[m')
print('\033[0:35:25m teste + \033[0:30:45m teste')
print('\033[0:36:25m teste + \033[0:30:46m teste')
print('\033[0:37:25m teste + \033[0:30:47m teste')