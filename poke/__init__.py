

def cores(cor='clear'):

    dic ={
        'azul':'\033[36m',
        'clear':'\033[m',
        'red':'\033[31m',
        'verd':'\033[32m',
        'yell':'\033[33m'

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

def dados(pok='bulbassaur'):
    
    pokedex ={
    
            'bulbassaur': {'Nome':pokemons("bulbasaur"),'Vida': 200, 'Dano':300 , 'Velocidade': 50 },
            'charmander':{'vida' :150, 'Dano': 300, 'Velocidade': 50}
                 
                 
                 }
   
    
    
    
    for i,k in pokedex[pok].items():
        print(f'{i}:{k}')
        
        
       
        
          

    
def iniciais():
    print(f"""
    [1] {pokemons()}
    [2] {pokemons('charmander')}
    [3] {pokemons('squirtle')}
    [4] {pokemons('pikachu')}
    """)
    opç = input(str('Qual vai ser a opção?: ').strip())
    inic={
        '1':pokemons(),
        '2':pokemons('charmander'),
        '3':pokemons('squirtle'),
        '4':pokemons('pikachu')
    }
    print(f'Você escolheu {inic[opç]}')
    dados('bulbasaur')


dados('charmander')