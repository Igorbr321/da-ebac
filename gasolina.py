# código de geração do gráfico 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('gasolina.csv', sep=',')

# Configurar estilo e temas do Seaborn e Matplotlib
sns.set(style="whitegrid", palette="muted", context="talk")

# Configurar o gráfico
plt.figure(figsize=(10, 6))
ax = sns.lineplot(data=df, x='dia', y='venda', marker='o', markersize=8, linewidth=2.5)

# Ajustar o título e as etiquetas
ax.set_title("Preço Médio de Vendas", fontsize=18, weight='bold', color='navy')
ax.set_xlabel("Dias", fontsize=14, color='gray')
ax.set_ylabel(None)

# Ajustar a legenda e a grade
plt.legend(["Preço Médio Diário"], loc="upper left", fontsize=12)
ax.grid(visible=True, color="lightgrey", linestyle="--", linewidth=0.7)

# Ajustes extras de visualização
plt.xticks(fontsize=12, color='dimgray')
plt.yticks(fontsize=12, color='dimgray')
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_color("lightgrey")
ax.spines["bottom"].set_color("lightgrey")

# Mostrar o gráfico
plt.tight_layout()
plt.show()
