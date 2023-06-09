from time import sleep

def cores(cor='clear'):

    dic ={
        'azul':'\033[36m',
        'clear':'\033[m',
        'red':'\033[31m',
        'verd':'\033[32m',
        'yell':'\033[33m',
        'roxo':'\033[35m]',
        'cinza':'\033[37m]'
        

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
    
            'bulbasaur': {'Nome':pokemons("bulbasaur"),'Vida': 200, 'Dano':300 , 'Velocidade': 50 ,'Habilidade':'(Cura): Bulbasaur se cura em 5% a cada round', 'Descrição': f'{cores("roxo")}Bulbasaur tem uma variedade de habilidades do tipo Grama que concedidod pelo bulbo crescendo em suas costas. Pós, cheiros, pétalas e sementes podem vir da ponta do bulbo, e vinhas e folhas podem vir da base. Ao manipular-los em movimentos como Semente sanguessuga , Chicote de Vinha, Folha Navalha, Dança de Pétalas, Bomba de Semente, and Doce Incenso, Bulbasaur tem um arsenal muito à sua disposição.{cores("clear")}'},
            'charmander':{'Nome':pokemons("charmander"),'vida' :150, 'Dano': 300, 'Velocidade': 50,'Descrição':'Charmander é um pequeno dinossauro bípede como pokémon. A maioria da cor do seu corpo é laranja, enquanto o seu ventre baixo é de cor amarelo-claro. Charmander, como suas evoluções, tem uma chama na ponta de sua cauda que arde constantemente.'},
            'squirtle':{'Nome':pokemons("squirtle"),'vida' :150, 'Dano': 300, 'Velocidade': 50,'Descrição':'O casco de Squirtle não é apenas usado para a proteção. A forma arredondada do casco e as ranhuras em sua superfície ajudam a minimizar a resistência na água, permitindo que este Pokémon nade em altas velocidades.'},
            'pikachu':{'Nome':pokemons("pikachu"),'vida' :150, 'Dano': 300, 'Velocidade': 50,'Descrição':'Pikachu é um Pokémon roedor meio gordinho, com o pêlo amarelo em todo o seu corpo. As orelhas de Pikachu são longas e chegam a um ponto com pontas pretas. Ele tem uma boca pequena, que se assemelha a um lado tres, tem olhos negros com os alunos brancos e dois círculos vermelhos em suas bochechas. Seus antebraços são curtos e um pouco atarracado, com cinco dedos em cada "mão", e seus pés têm três dígitos. Ele tem duas listras marrons em suas costas, e sua cauda é em forma de raio Zigzag de estilo, com um pedaço de pele marrom na base da cauda. Embora seja tecnicamente um quadrúpede , em várias ocasiões tem sido mostrado para ser capaz de ficar de pé e andar ereto sobre as patas traseiras.'},

                 
                 
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
                print(f'{cores["red"]}ERROR!!! Usuario não digitou um numero.{cores("clear")}')
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
            print('Somente as opçôes mostradas estão validas!')
        
        
        inic={
            '1':'bulbasaur',
            '2':'charmander',
            '3':'squirtle',
            '4':'pikachu'
        }
        
        print(f'Você escolheu {pokemons(inic[opç])}')
        
        dados(inic[opç])
        resp = ler('Vai esse msm?[S/N]: ', modo='string').upper()
        if resp[0] =='S':
            break
       
        
    
    print('OK.')
       
   
iniciais()