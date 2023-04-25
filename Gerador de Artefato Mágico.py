import random

#=================================================================
#Gerador de Artefato Mágico, criado por delunatriestocode (2022)
#Magic Artefact Generator, created by delunatriestocode (2022)
#=================================================================

#tipo de artefato (material não variável)
tipo_artf_opt = ["Algema","Amuleto","Anel","Apanhador de Sonhos","Berrante","Botão de Roupa","Bracelete","Brinco","Bússola","Cachimbo","Caixa","Chave","Chaveiro","Chupeta","Coçador de Costas","Concha","Coroa","Crânio (Cabra)","Crânio (Humano)","Crocks","Crucifixo","Cubo","Cubo Mágico","Dado (6 lados)","Dado (20 lados)","Dado (100 lados)","Dentadura","Elmo (Armadura)","Esfera","Espelho","Ferradura","Fidget Spinner","Fivela de Cinto","Flauta Doce","Flor","Hashi","Isqueiro","Maçã","Manopla","Máscara","Medalha","Moeda","Monóculo","Ocarina","Óculos","Origami","Peça de Xadrez","Peitoral (Armadura)","Pena","Pin (Acessório) ","Porca Sextavada","Prendedor de Cabelo (Palito)","Prendedor de Cabelo (Piranha)","Prendedor de Cabelo (Presilha)","Prótese (Dente)","Prótese (Olho)","Relógio de Bolso","Relógio de Pulso","Sino","Troféu"]
tipo_artf = random.choice(tipo_artf_opt)

#material do artefato
mat_artf_opt = ["Aço","Ágata","Alumínio","Âmbar","Ametista","Bismuto","Bronze","Chumbo","Cobre","Diamante","Esmeralda","Estanho","Ferro","Granito","Jade","Latão","Mármore","Obsidiana","Ónix","Ouro","Pedra","Prata","Quartzo","Rubi","Safira","Topázio","Titânio","Tungstênio","Turquesa",

"Argila","Cimento","Concreto","Lego","Papel Machê","Porcelana","Resina","Vidro","Vidro Temperado","Vidro Vulcânico"]

mat_artf = random.choice(mat_artf_opt)

#habilidade do artefato
hab_artf_opt = ["Manipulação de Água","Manipulação do Ar","Manipulação de Cristais","Manipulação da Eletricidade","Manipulação de Fogo","Manipulação de Gelo","Manipulação de Gravidade","Manipulação de Luz","Manipulação de Peso","Manipulação de Plantas","Manipulação de Sombras","Manipulação de Sangue",

"Causar Explosões","Criação de Barreiras Invisíveis","Envenenamento à Distância","Ilusionismo (Sonoro)","Ilusionismo (Visual)","Invisibilidade","Invulnerabilidade","Ler Mentes","Levitação","Necromancia","Prever o Futuro","Shape-Shifting","Telecinese","Teletransporte","Teletransporte Único","Transformar Ferro em Ouro","Visão Além do Alcance","Visão Noturna"]

hab_artf = random.choice(hab_artf_opt)

#template
print("===============================================\nTipo de artefato: {}\nMaterial do Artefato: {}\nHabilidade do artefato: {}\n===============================================".format(tipo_artf,mat_artf,hab_artf))






