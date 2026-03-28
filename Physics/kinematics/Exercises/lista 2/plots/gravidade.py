import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

# Constantes
G = 6.67e-11
M = 6.0e24

# Dados
r = np.linspace(6.37e6, 2.0e7, 1000)
g = G * M / r**2

# Pontos importantes
r_terra = 6.37e6
g_terra = G * M / r_terra**2

r_sat = 7.0e6
g_sat = G * M / r_sat**2

# Estilo geral
plt.rcParams.update({
    "font.size": 14,
    "axes.labelsize": 16,
    "axes.titlesize": 18
})

plt.figure(figsize=(10,6))

# Curva
plt.plot(r, g, linewidth=2)

# Pontos destacados
plt.scatter(r_terra, g_terra)
plt.scatter(r_sat, g_sat)

# Anotações em LaTeX
plt.text(r_terra, g_terra,
         r"$ (6{,}37 \times 10^6\,\mathrm{m},\ 9{,}8\,\mathrm{m/s^2})$",
         verticalalignment='bottom')

plt.text(r_sat, g_sat,
         r"$ (7{,}0 \times 10^6\,\mathrm{m},\ 8{,}16\,\mathrm{m/s^2})$",
         verticalalignment='bottom')

plt.ylim(0, 12)

# Labels com LaTeX
plt.xlabel(r"Raio $r$ (m)")
plt.ylabel(r"Aceleração gravitacional $g$ (m/s$^2$)")
plt.title(r"$g(r) = \dfrac{GM}{r^2}$")

# Formatação do eixo X (base 10)
formatter = ScalarFormatter(useMathText=True)
formatter.set_powerlimits((6,6))  # força 10^6
plt.gca().xaxis.set_major_formatter(formatter)

# Grid mais visível
plt.grid(True, linewidth=0.8)

plt.tight_layout()

# 🔥 SALVAR EM PDF
plt.savefig("grafico_gravidade.pdf", format="pdf", bbox_inches="tight")

plt.show()