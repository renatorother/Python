velocidade_carro = 80
local_carro = 10

RADAR = 100
LOCAL_RADAR = 80
RANGE_FRENTE = LOCAL_RADAR + 10
RANGE_TRAS = LOCAL_RADAR - 10
PASSOU_RADAR = local_carro == LOCAL_RADAR or local_carro >= RANGE_FRENTE or local_carro >= RANGE_TRAS
MULTA = velocidade_carro > RADAR
REGULAR = velocidade_carro <= RADAR


if PASSOU_RADAR :
    print(f'O carro passou pelo Radar no Km{LOCAL_RADAR} da Rodovia!')
else:
    print(f'O carro não passou pelo Radar!')

if PASSOU_RADAR and MULTA:
    print(f'Multado com velocidade de {velocidade_carro}Km/h!')

if PASSOU_RADAR and REGULAR:
    print(f'Velocidade dentro do limite permitido!')





