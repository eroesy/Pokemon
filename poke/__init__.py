from time import sleep

from os import system



def cores(cor='clear'):

    dic ={
        'azul2':'\033[34m',
        'azul':'\033[36m',
        'clear':'\033[m',
        'red':'\033[31m',
        'verd':'\033[32m',
        'yell':'\033[33m',
        'roxo':'\033[35m',
        'cinza':'\033[37m',
        'reverse':'\033[7;4m'
        

         }
    return f"{dic[cor]}"
    


def pokemons(poke='bulbasaur'):

    pokers={
        'bulbasaur':f'{cores("verd")}Bulbasaur{cores()}',
        'charmander':f'{cores("red")}Charmander{cores()}',
        'squirtle':f'{cores("azul")}Squirtle{cores()}',
        'pikachu':f'{cores("yell")}Pikachu{cores()}'

    }
    return pokers[poke]

def dados(pok='bulbasaur'):
    
    pokedex ={
    
            'bulbasaur': {'Nome':pokemons("bulbasaur"),'Vida': 300, 'Dano':150 , 'Velocidade': 50 ,'Habilidade':'(Cura): Bulbasaur se cura em 5% a cada round', 'Descrição': f'{cores("roxo")}Bulbasaur tem uma variedade de habilidades do tipo Grama que concedidod pelo bulbo crescendo em suas costas. Pós, cheiros, pétalas e sementes podem vir da ponta do bulbo, e vinhas e folhas podem vir da base. Ao manipular-los em movimentos como Semente sanguessuga , Chicote de Vinha, Folha Navalha, Dança de Pétalas, Bomba de Semente, and Doce Incenso, Bulbasaur tem um arsenal muito à sua disposição.{cores("clear")}'},
            'charmander':{'Nome':pokemons("charmander"),'vida' :150, 'Dano': 300, 'Velocidade': 50,'Descrição':f'{cores("roxo")}Charmander é um pequeno dinossauro bípede como pokémon. A maioria da cor do seu corpo é laranja, enquanto o seu ventre baixo é de cor amarelo-claro. Charmander, como suas evoluções, tem uma chama na ponta de sua cauda que arde constantemente.{cores("clear")}'},
            'squirtle':{'Nome':pokemons("squirtle"),'vida' :200, 'Dano': 200, 'Velocidade': 50,'Descrição':f'{cores("roxo")}O casco de Squirtle não é apenas usado para a proteção. A forma arredondada do casco e as ranhuras em sua superfície ajudam a minimizar a resistência na água, permitindo que este Pokémon nade em altas velocidades.{cores("clear")}'},
            'pikachu':{'Nome':pokemons("pikachu"),'vida' :150, 'Dano': 300, 'Velocidade': 50,'Habilidade':f'(Paralisia): {pokemons("pikachu")} tem 5% de chance de paralisar o oponente(paralisia dura {cores("cinza")}3{cores()} turnos)  ','Descrição':f'{cores("roxo")}Pikachu é um Pokémon roedor meio gordinho, com o pêlo amarelo em todo o seu corpo. A sua cauda é em forma de raio Zigzag de estilo, com um pedaço de pele marrom na base da cauda. Embora seja tecnicamente um quadrúpede , em várias ocasiões tem sido mostrado para ser capaz de ficar de pé e andar ereto sobre as patas traseiras.{cores("clear")}'},

                 
                 
                 }
   
    
    
    
    for i,k in pokedex[pok].items():
        
        print(f'{i}: {k}')
        sleep(0.7)
        
        
       
        
def ler(texto='vai se fuder giselly liege: ', modo ='int'):

    if modo == 'int':
        
        
        while True:
            try:
                n = int(input(texto))
            except (ValueError, TypeError):
                print(f'{cores("red")}ERROR!!! Digite um numero inteiro.{cores("clear")}')
            except(KeyboardInterrupt):
                print(f'{cores("red")}ERROR!!! Usuario não digitou um numero.{cores("clear")}')
            else:
                break
        
        
    elif modo == 'string':
        while True:
            try:
                n = str(input(texto))
            except(IndexError):
                print(f'{cores("red")}ERROR!!! Digite uma string.{cores("clear")}')
            else:
                break
        
            
            
    
    return n
                


def mapas(mapa= 'floresta'):
    
    mapas = {
        'floresta': f'A{cores("verd")} floresta {cores()}cheia de pokemons maravilhosos. Um otimo lugar para um noob!\nDifilcudade: {cores("azul")} FACIL {cores()}',
        'montanha': f'A {cores("yell")}MONTANHA{cores()} Lar de pokemons pedras e voadores extraordinarios,Cuidado com os {cores("roxo")}"Cães"{cores()}.\nDifilcudade: {cores("azul2")}MEDIA {cores()}',
        'deserto': f'O {cores("red")}DESERTO{cores("clear")}, Casa dos pokemons nordestinos, secas e vento forte são do contidiano dos moradores({cores("roxo")}VEM PRO NORDESTE MADONA{cores()}).\nDifilcudade: {cores("red")}DIFICIL{cores()}',
        'hell': f'O {cores("roxo")}Lugar assombradooooo{cores("clear")}\n\n"Se você ja morreu alguma vez sua alma não me pertence"\n\n {cores("red")}                                        - O Tinhoso xxx\n\n{cores("clear")}\nDifilcudade: {cores("red")}VOCê JA ESTA MORTO, NÃO TEM COMO PIORAR ><.{cores()}',
        'dreamcore': f'{cores("reverse")}Como aliviar sua dor, ficar no Dreamcore?{cores("clear")}(Não a Informação do local OBS: {cores("red")}NIGUEM NUNCA VOLTOU!!!!){cores("clear")}\nDifilcudade: {cores("reverse")}Talvez não seja tão ruim assim?{cores()}'}

    for i in mapas[mapa]:
        print(i,end="")
        
        
    

def aventura(local='floresta'):
    print('Voce finalmente esta pronto(a) para começar a sua AVENTURA!')
    sleep(0.3)
    print(f'''
    
        [ 1 ] {cores('verd')}FLORESTA{cores()}
        [ 2 ] {cores('yell')}MONTANHA{cores()}
        [ 3 ] {cores('red')}DESERTO{cores()}
        [ 4 ] {cores('roxo')}HELL{cores()}
        [ 5 ] {cores('reverse')}DREAMCORE{cores()}
    
    
    ''')
    while True:
        while True:
            num = ler(texto='Escolha um lugar para começar: ', modo='int')
           
            if num == 1:
                local = 'floresta'
                break
            elif num == 2:
                local = 'montanha'
                break
            elif num == 3:
                local = 'deserto'
                break
            elif num == 4:
                local = 'hell'
                break
            elif num == 5:
                local = 'dreamcore'
                break
           
            
           
            
            print(f'{cores("red")}Somente as opçôes mostradas estão validas!{cores()}')
        mapas(local)
        resp = ler('\nVai esse msm?[S/N]: ', modo='string').upper()
        system('cls')
        print(f'''

    [ 1 ] {cores('verd')}FLORESTA{cores()}
    [ 2 ] {cores('yell')}MONTANHA{cores()}
    [ 3 ] {cores('red')}DESERTO{cores()}
    [ 4 ] {cores('roxo')}HELL{cores()}
    [ 5 ] {cores('reverse')}DREAMCORE{cores()}


''')
        if resp[0] =='S':
            break


    
def iniciais():
    while True:
        print(f"""
        [1] {pokemons()}
        [2] {pokemons('charmander')}
        [3] {pokemons('squirtle')}
        [4] {pokemons('pikachu')}
        """)
        while True:
            
            opç = str(ler('Qual vai ser a opção?: ',modo='string'))
            if opç in '1234':
                break
            if opç == 'VSFD' or 'vsfd':
                print(f'{cores("red")}VAI SE FUDER VOCÊ \n LIXO, GABIRU, TIMBU, ESCAMBO.{cores("clear")}')
            print('Somente as opçôes mostradas estão validas!')
        
        
        inic={
            '1':'bulbasaur',
            '2':'charmander',
            '3':'squirtle',
            '4':'pikachu'
        }
        
        print(f'Você escolheu {pokemons(inic[opç])}')
        
        dados(inic[opç])
        resp = ler('\nVai esse msm?[S/N]: ', modo='string').upper()
        if resp[0] =='S':
            break
       
        
            
    print('OK.')
    aventura()
    print('OK.')
       
   
aventura()