velocidade_carro = 50  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

velocidade_carro_passou_rad1 = velocidade_carro > RADAR_1
carro_passou_rad1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
     local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado = carro_passou_rad1 and velocidade_carro_passou_rad1

if velocidade_carro_passou_rad1:
    print('Carro multado')

if carro_passou_rad1:
    print('carro passou radar 1')

if carro_multado:
    print('carro multado em radar 1')
