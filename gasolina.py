

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('gasolina.csv', sep=',')

# Configurar o estilo do fundo para "dark"
plt.style.use('dark_background')

# Configurar o gráfico
plt.figure(figsize=(10, 6))
ax = sns.lineplot(data=df, x='dia', y='venda', marker='o', color="cyan", markersize=8, linewidth=2.5)

# Ajustar o título e as etiquetas
ax.set_title("Preço Médio de Vendas", fontsize=18, weight='bold', color='white')
ax.set_xlabel("Dias", fontsize=14, color='lightgray')
ax.set_ylabel(None)

# Ajustar a legenda e a grade
plt.legend(["Preço Médio Diário"], loc="upper left", fontsize=12, facecolor='black', edgecolor='white')
ax.grid(visible=True, color="gray", linestyle="--", linewidth=0.7)

# Ajustes extras de visualização
plt.xticks(fontsize=12, color='lightgray')
plt.yticks(fontsize=12, color='lightgray')
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_color("gray")
ax.spines["bottom"].set_color("gray")

# Mostrar o gráfico
plt.tight_layout()
plt.savefig('grafico_vendas.png', dpi=300)

