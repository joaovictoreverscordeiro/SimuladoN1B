import matplotlib.pyplot as plt
import numpy as np
import random

#Parte A
omega0=6.7*(10**6)
a=0.134
R=1.8

#Variáveis a descobrir
Ron=3.35
Vsup=0.67
Vinf=-8.978

#cabeçalho
print('='*15,'Parte B','='*15)
print()

#frquência
freq=44.89*10**9
dt=100*10**(-12)

#voltagem
volt0=float(input('Digite a amplitude de voltagem V0 (sem unidade; range: 0 a 15.0): ').strip())
volt=(1+random.uniform(-0.05,0.05))*volt0

if volt0>15:
    input('ERRO. Valor fora do range possível, que compreende 0 a 15. Clique ENTER para encerrar o programa. ')
    exit()
else:
    pass

voff=(1+random.uniform(-0.05,0.05))*a*volt*np.exp(-freq/omega0)

#funções
def V(t):
    return voff+volt*np.cos(freq*t)

def ddp(t):
    Vt = V(t)
    return np.where(
        Vt > Vsup,
        (Vt - Vsup) / (1 + Ron/R),
        np.where(
            Vt < Vinf,
            Vt - Vinf,
            0
        )
    )

#eixos/intervalos
valuesdv=['0.1','0.25', '0.5', '0.75', '1','2','1.5']
strdv=str(input('Digite uma das escalas permitidas para a voltagem: ').strip())

for i in range(7):
    if strdv==valuesdv[i]:
        dv=float(valuesdv[i])
    else:
        pass

if bool(dv)==False:
    input('ERRO. Escala para V inválida, os valores válidos são 0.1, 0.25, 0.5, 0.75, 1, 1.5, 2. Clique ENTER para encerrar o programa. ')
    exit()
else:
    pass

t1=np.arange(0,5*dt,0.002*dt)

#plot
plt.plot(t1,ddp(t1),'k')
plt.axis((0,5*dt,-10*dv,10*dv))
plt.xlabel('t (S)')
plt.ylabel('ddp (V)')
plt.show()

print()

input('Clique ENTER para encerrar o programa. ')
