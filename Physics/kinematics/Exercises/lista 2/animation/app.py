import streamlit as st

st.set_page_config(page_title="Simulador de Peso", layout="centered")

st.title("Força Peso (P = m · g)")

# Sliders
m = st.slider("Massa (kg)", 0.1, 20.0, 6.0)
g = st.slider("Gravidade (m/s²)", 0.1, 20.0, 6.0)

# Cálculo
P = m * g

# Resultado
st.markdown(f"## 💡 P = {P:.2f} N")

# Visual simples (bloco + seta)
st.markdown("---")
st.markdown("### Representação")

# Desenho simples com markdown
st.markdown(
    f"""
    <div style="text-align:center;">
        <div style="
            display:inline-block;
            padding:30px;
            background-color:#4A90E2;
            color:white;
            border-radius:10px;
            font-size:20px;">
            m = {m:.1f} kg
        </div>
        <div style="font-size:40px; color:red;">⬇</div>
        <div style="font-size:18px;">
            F = {P:.1f} N
        </div>
        <hr style="width:50%;">
        <div>g = {g:.1f} m/s²</div>
    </div>
    """,
    unsafe_allow_html=True
)

# Explicação
st.markdown("---")
st.markdown("""
### 📘 Fórmula
**P = m · g**

- P: peso (N)  
- m: massa (kg)  
- g: gravidade (m/s²)
""")