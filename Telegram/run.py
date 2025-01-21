from telegram import TelegramBot

obj_telegram = TelegramBot()

print("Iniciando o robô aguarde um momento... ")
print("Escolha seu grupo alvo: ")
grupo_alvo = obj_telegram.get_groups()
membros = obj_telegram.get_members_of_groups(grupo_alvo)
print("%s membros encontrados no grupo" % len(membros))

print("Escolha o grupo que você quer adicionar os novos membros")
meu_grupo = obj_telegram.get_groups()

for membro in membros:
    adicionado = obj_telegram.add_member_to_group(membro, meu_grupo)
    if adicionado:
        print("Membro %s adicionado com sucesso" % membro.id)