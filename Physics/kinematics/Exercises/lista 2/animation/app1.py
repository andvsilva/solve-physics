import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Simulador de Peso", layout="centered")

st.title("📊 Peso (P = m · g) com gráfico")

# Slider da gravidade
g = st.slider("Gravidade (m/s²)", 0.1, 20.0, 9.8)

# Slider da massa atual
m_atual = st.slider("Massa (kg)", 0.1, 20.0, 6.0)

# Cálculo do peso atual
P_atual = m_atual * g

st.markdown(f"## 💡 P = {P_atual:.2f} N")

# Dados para o gráfico
m = np.linspace(0, 20, 100)
P = m * g

# Criar gráfico
fig, ax = plt.subplots()

ax.plot(m, P, label="P = m·g")
ax.scatter([m_atual], [P_atual])  # ponto atual

ax.set_xlabel("Massa (kg)")
ax.set_ylabel("Peso (N)")
ax.set_title("Relação entre Massa e Peso")

ax.grid()

st.pyplot(fig)

# Explicação
st.markdown("---")