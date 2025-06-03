import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Ponto médio dos intervalos (valores observados)
pontos_medios = np.array([34.5, 44.5, 54.5, 64.5, 74.5, 84.5, 94.5, 104.5])

# Percentuais acumulados (sem incluir o 100%)
percentuais = np.array([1.82, 3.64, 7.28, 14.55, 36.37, 58.19, 76.37, 98.19])

# Converter para proporções (de 0 a 1)
p = percentuais / 100

# Obter os valores z correspondentes (quantis da normal padrão)
z_teoricos = norm.ppf(p)

# Plotar gráfico Q-Q
plt.figure(figsize=(8, 6))
plt.scatter(z_teoricos, pontos_medios, color='blue', label='Dados Observados')
plt.plot(z_teoricos, np.poly1d(np.polyfit(z_teoricos, pontos_medios, 1))(z_teoricos), 
         color='red', linestyle='--', label='Linha de Regressão (esperada se normal)')

plt.title('Gráfico Q-Q: Verificação de Normalidade')
plt.xlabel('Quantis da Normal Padrão (z)')
plt.ylabel('Tempo de Espera (minutos)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
