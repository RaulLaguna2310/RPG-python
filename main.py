from random import randint

#Cria uma lista 
lista_npcs = []

#Cria um dicionário
player = {
    "nome" : "Dilmo",
    "level" : 1,
    "exp" : 0,
    "exp_max" : 30,
    "hp" : 100,
    "hp_max" : 100,
    "dano" : 25,
}

#Criando um npc e mudando os seus status de acordo com seu nivel
def criar_npc(level):
    #Cria um dicionario para cada npc
    novo_npc = {
        "nome": f"Monstro #{level}",
        "level": level,
        "dano": 5 * level,
        "hp": 100 * level,
        "hp_max" : 100 * level,
        "exp" : 7 * level,
    }
    return novo_npc
    
#Gera npcs até um limite determinado manualmente na hora de chamar a função e adiciona o dicionario de cada npc dentro da lista_npcs 
def gerar_npcs(n_npcs):
    #Gera os npcs     
    for x in range(n_npcs):
        npc = criar_npc(x + 1)
        #Adiciona os dicionarios gerados dentro da lista_npcs
        lista_npcs.append(npc)

#Exibe as informações dos npcs
def exibir_npc(npc):
    print(
            f"Nome: {npc['nome']} // Nivel: {npc['level']} // Dano: {npc['dano']} // Vida: {npc['hp']}/{npc['hp_max']}"
        )

#Exibe todos os npcs dentro de lista_npcs
def exibir_npcs():
    for npc in lista_npcs:
        exibir_npc(npc)

#Exibe as informações do player
def exibir_player():
    print(
            f"Nome: {player['nome']} // Nivel: {player['level']} // Dano: {player['dano']} // Vida: {player['hp']}/{player['hp_max']} // EXP: {player['exp']}/{player['exp_max']}"
        )

#Função para que o npc ataque o player
def atacar_npc(npc):
    npc["hp"] -= player["dano"]

#Função para que o player ataque o npc
def atacar_player(npc):
    player['hp'] -= npc["dano"]

#Exibibe algumas informações do player e de um dos npcs que foi selecionado aleatoriamente
def exibir_info_batalha(npc):
    print(f"Player - {player['nome']}: {player['hp']}/{player['hp_max']}")
    print(f"NPC - {npc['nome']}: {npc['hp']}/{npc['hp_max']}")
    print('-----------------------------\n')

#Reseta a vida do player após a batalha
def reset_player():
    player['hp'] = player['hp_max']

def reset_npc(npc):
    npc['hp'] = npc['hp_max']

def level_up():
    if player['exp'] >= player['exp_max']:
        player['level'] += 1
        player['exp'] = 0
        player['exp_max'] = player['exp_max'] * 2
        player['hp_max'] = player['hp_max'] + 50 

#Laço de repetição que simula uma batalha entre npc e player
def iniciar_batalha(npc):
    while player['hp'] > 0 and npc['hp'] > 0: 
        atacar_npc(npc)
        atacar_player(npc)
        exibir_info_batalha(npc)
    
    if player['hp'] > 0:
        print(f"O {player['nome']} venceu {npc['nome']} e ganhou {npc['exp']} de EXP!")
        player['exp'] += npc['exp']
        exibir_player()
    else:
        print(f"O {npc['nome']} te matou!")
        exibir_npc(npc)

    level_up()
    reset_player()
    reset_npc(npc)

#Gerando e exibindo os npcs 
gerar_npcs(5) 
exibir_npcs()

#Radomizando o npc que será selecionado para a batalha
npc_aleatorio = randint(0, 4)
npc_selecionado = lista_npcs[npc_aleatorio]

#Atacando,  sendo atacado e exibindo infos dos status do player e npc
iniciar_batalha(npc_selecionado)
iniciar_batalha(npc_selecionado)
iniciar_batalha(npc_selecionado) 
iniciar_batalha(npc_selecionado) 
iniciar_batalha(npc_selecionado)
iniciar_batalha(npc_selecionado)    