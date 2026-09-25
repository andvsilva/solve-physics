import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parâmetros
R_terra = 6370  # km
h = 2560        # km
R_orbita = R_terra + h + 5000

# Tempo
t = np.linspace(0, 2*np.pi, 300)

# Figura
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect('equal')
ax.set_facecolor("black")

# Terra
terra = plt.Circle((0, 0), R_terra, color='blue', alpha=0.5)
ax.add_patch(terra)

# Órbita
orbita = plt.Circle((0, 0), R_orbita, linestyle='dashed', color='white', fill=False)
ax.add_patch(orbita)

# Satélite
sat, = ax.plot([], [], 'ro', markersize=6)

# Vetor peso (inicial não nulo!)
vetor = ax.quiver(0, 0, 1, 0, color='yellow', scale=10)

# Limites
lim = R_orbita + 4000
ax.set_xlim(-lim, lim)
ax.set_ylim(-lim, lim)

# Grid
ax.grid(color='gray', linestyle='--', linewidth=0.5)

# Função de atualização
def update(frame):
    ang = t[frame]
    
    # Posição do satélite
    x = R_orbita * np.cos(ang)
    y = R_orbita * np.sin(ang)
    
    # IMPORTANTE: precisa ser sequência
    sat.set_data([x], [y])
    
    # Vetor peso (aponta para o centro)
    vx = -x
    vy = -y
    
    # Normalizar com proteção contra divisão por zero
    norm = np.sqrt(vx**2 + vy**2)
    if norm == 0:
        norm = 1
    
    # Escala visual do vetor
    escala = 1.5
    vx = (vx / norm) * escala
    vy = (vy / norm) * escala
    
    # Atualizar vetor sem recriar
    vetor.set_offsets([x, y])
    vetor.set_UVC(vx, vy)
    
    return sat, vetor

# Animação
ani = FuncAnimation(
    fig,
    update,
    frames=len(t),
    interval=40,
    blit=True
)

plt.show()