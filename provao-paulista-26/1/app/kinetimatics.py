import streamlit as st
import numpy as np
import plotly.graph_objects as go


# ============================================================
# CONFIGURAÇÃO
# ============================================================

st.set_page_config(
    page_title="Dashboard de Cinemática",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# CSS
# ============================================================

st.markdown(
    """
    <style>

    .main {
        background-color: #0e1117;
    }

    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }

    .titulo {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0;
    }

    .subtitulo {
        color: #9aa4b2;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }

    .formula-box {
        background-color: #161b22;
        border-left: 4px solid #58a6ff;
        padding: 12px 20px;
        border-radius: 8px;
        margin: 15px 0;
    }

    .resultado {
        background-color: #161b22;
        padding: 18px;
        border-radius: 10px;
        text-align: center;
    }

    .resultado-valor {
        font-size: 1.8rem;
        font-weight: bold;
    }

    .resultado-label {
        color: #9aa4b2;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# FUNÇÕES
# ============================================================

def grafico_base(fig, titulo, x_title, y_title):
    fig.update_layout(
        title=titulo,
        template="plotly_dark",
        height=450,
        margin=dict(l=50, r=30, t=60, b=50),
        xaxis_title=x_title,
        yaxis_title=y_title,
        hovermode="x unified",
    )

    fig.update_xaxes(showgrid=True)
    fig.update_yaxes(showgrid=True)

    return fig


def card(label, valor, unidade=""):
    st.markdown(
        f"""
        <div class="resultado">
            <div class="resultado-label">{label}</div>
            <div class="resultado-valor">
                {valor} {unidade}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def formula(equacao):
    """
    Exibe uma equação usando o renderizador matemático
    nativo do Streamlit.
    """
    st.markdown('<div class="formula-box">', unsafe_allow_html=True)
    st.latex(equacao)
    st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# CABEÇALHO
# ============================================================

st.markdown(
    '<div class="titulo">🚀 Dashboard de Cinemática</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="subtitulo">'
    'Velocidade, aceleração, gráficos, MU, MUV, queda livre e lançamento vertical'
    '</div>',
    unsafe_allow_html=True,
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("📚 Conteúdos")

pagina = st.sidebar.radio(
    "Selecione o conteúdo:",
    [
        "🏠 Início",
        "📐 Velocidade e aceleração",
        "📈 Gráficos",
        "➡️ Movimento Uniforme",
        "🚗 Movimento Uniformemente Variado",
        "⬇️ Queda livre",
        "🚀 Lançamento vertical",
    ],
)


# ============================================================
# INÍCIO
# ============================================================

if pagina == "🏠 Início":

    st.header("Cinemática")

    st.write(
        """
        Este dashboard permite explorar os principais conceitos de Cinemática
        de forma interativa.

        Modifique as variáveis utilizando os controles e observe como
        os resultados e os gráficos são alterados.
        """
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Velocidade", "m/s")

    with col2:
        st.metric("Aceleração", "m/s²")

    with col3:
        st.metric("Tempo", "s")

    st.divider()

    st.subheader("Conteúdos")

    conteudos = [
        ("📐", "Velocidade e aceleração"),
        ("📈", "Representação gráfica"),
        ("➡️", "Movimento Uniforme"),
        ("🚗", "Movimento Uniformemente Variado"),
        ("⬇️", "Queda livre"),
        ("🚀", "Lançamento vertical"),
    ]

    cols = st.columns(3)

    for i, (icone, nome) in enumerate(conteudos):
        with cols[i % 3]:
            st.info(f"{icone} **{nome}**")


# ============================================================
# VELOCIDADE E ACELERAÇÃO
# ============================================================

elif pagina == "📐 Velocidade e aceleração":

    st.header("📐 Velocidade e Aceleração")

    # --------------------------------------------------------
    # VELOCIDADE MÉDIA
    # --------------------------------------------------------

    st.subheader("Velocidade escalar média")

    col1, col2, col3 = st.columns(3)

    with col1:
        s0 = st.number_input(
            "Posição inicial (m)",
            value=0.0,
            step=1.0,
        )

    with col2:
        sf = st.number_input(
            "Posição final (m)",
            value=100.0,
            step=1.0,
        )

    with col3:
        dt = st.number_input(
            "Intervalo de tempo (s)",
            min_value=0.01,
            value=10.0,
            step=1.0,
        )

    deslocamento = sf - s0
    velocidade_media = deslocamento / dt

    formula(r"v_m = \frac{\Delta s}{\Delta t}")

    card(
        "Velocidade média",
        f"{velocidade_media:.2f}",
        "m/s",
    )

    st.divider()

    # --------------------------------------------------------
    # ACELERAÇÃO MÉDIA
    # --------------------------------------------------------

    st.subheader("Aceleração média")

    col1, col2, col3 = st.columns(3)

    with col1:
        v0 = st.number_input(
            "Velocidade inicial (m/s)",
            value=0.0,
            key="acc_v0",
        )

    with col2:
        vf = st.number_input(
            "Velocidade final (m/s)",
            value=20.0,
            key="acc_vf",
        )

    with col3:
        tempo_acc = st.number_input(
            "Intervalo de tempo (s)",
            min_value=0.01,
            value=5.0,
            step=1.0,
            key="acc_t",
        )

    aceleracao_media = (vf - v0) / tempo_acc

    formula(r"a_m = \frac{\Delta v}{\Delta t}")

    card(
        "Aceleração média",
        f"{aceleracao_media:.2f}",
        "m/s²",
    )


# ============================================================
# GRÁFICOS
# ============================================================

elif pagina == "📈 Gráficos":

    st.header("📈 Representação gráfica")

    st.write(
        """
        Explore simultaneamente os gráficos de posição, velocidade
        e aceleração em função do tempo.
        """
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        s0 = st.slider(
            "Posição inicial (m)",
            -50.0,
            50.0,
            0.0,
        )

    with col2:
        v0 = st.slider(
            "Velocidade inicial (m/s)",
            -30.0,
            30.0,
            5.0,
        )

    with col3:
        a = st.slider(
            "Aceleração (m/s²)",
            -10.0,
            10.0,
            2.0,
        )

    tempo_max = st.slider(
        "Tempo da simulação (s)",
        1.0,
        30.0,
        10.0,
    )

    formula(
        r"s(t) = s_0 + v_0t + \frac{1}{2}at^2"
    )

    t = np.linspace(0, tempo_max, 300)

    s = s0 + v0 * t + 0.5 * a * t**2
    v = v0 + a * t
    aceleracao = np.full_like(t, a)

    col1, col2 = st.columns(2)

    with col1:

        fig_s = go.Figure()

        fig_s.add_trace(
            go.Scatter(
                x=t,
                y=s,
                mode="lines",
                name="s(t)",
                line=dict(width=3),
            )
        )

        fig_s = grafico_base(
            fig_s,
            "Posição × tempo",
            "Tempo (s)",
            "Posição (m)",
        )

        st.plotly_chart(
            fig_s,
            use_container_width=True,
        )

    with col2:

        fig_v = go.Figure()

        fig_v.add_trace(
            go.Scatter(
                x=t,
                y=v,
                mode="lines",
                name="v(t)",
                line=dict(width=3),
            )
        )

        fig_v = grafico_base(
            fig_v,
            "Velocidade × tempo",
            "Tempo (s)",
            "Velocidade (m/s)",
        )

        st.plotly_chart(
            fig_v,
            use_container_width=True,
        )

    fig_a = go.Figure()

    fig_a.add_trace(
        go.Scatter(
            x=t,
            y=aceleracao,
            mode="lines",
            name="a(t)",
            line=dict(width=3),
        )
    )

    fig_a = grafico_base(
        fig_a,
        "Aceleração × tempo",
        "Tempo (s)",
        "Aceleração (m/s²)",
    )

    st.plotly_chart(
        fig_a,
        use_container_width=True,
    )


# ============================================================
# MOVIMENTO UNIFORME
# ============================================================

elif pagina == "➡️ Movimento Uniforme":

    st.header("➡️ Movimento Uniforme — MU")

    st.write(
        """
        No Movimento Uniforme, a velocidade permanece constante e
        a aceleração é igual a zero.
        """
    )

    # CORREÇÃO:
    # Antes estava dentro de st.markdown com $...$.
    # Agora usa diretamente st.latex().
    formula(r"s(t) = s_0 + vt")

    col1, col2, col3 = st.columns(3)

    with col1:
        s0 = st.slider(
            "Posição inicial (m)",
            -100.0,
            100.0,
            0.0,
        )

    with col2:
        velocidade = st.slider(
            "Velocidade (m/s)",
            -30.0,
            30.0,
            10.0,
        )

    with col3:
        tempo_max = st.slider(
            "Tempo (s)",
            1.0,
            30.0,
            10.0,
        )

    t = np.linspace(0, tempo_max, 300)

    s = s0 + velocidade * t

    col1, col2 = st.columns(2)

    with col1:

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=t,
                y=s,
                mode="lines",
                name="posição",
                line=dict(width=3),
            )
        )

        fig = grafico_base(
            fig,
            "Posição × tempo",
            "Tempo (s)",
            "Posição (m)",
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    with col2:

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=t,
                y=np.full_like(t, velocidade),
                mode="lines",
                name="velocidade",
                line=dict(width=3),
            )
        )

        fig = grafico_base(
            fig,
            "Velocidade × tempo",
            "Tempo (s)",
            "Velocidade (m/s)",
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    st.metric(
        "Posição final",
        f"{s[-1]:.2f} m",
    )


# ============================================================
# MOVIMENTO UNIFORMEMENTE VARIADO
# ============================================================

elif pagina == "🚗 Movimento Uniformemente Variado":

    st.header("🚗 Movimento Uniformemente Variado — MUV")

    st.write(
        """
        No MUV, a aceleração permanece constante.
        """
    )

    formula(
        r"s(t) = s_0 + v_0t + \frac{1}{2}at^2"
    )

    formula(
        r"v(t) = v_0 + at"
    )

    col1, col2 = st.columns(2)

    with col1:

        s0 = st.slider(
            "Posição inicial (m)",
            -100.0,
            100.0,
            0.0,
            key="muv_s0",
        )

        v0 = st.slider(
            "Velocidade inicial (m/s)",
            -30.0,
            30.0,
            5.0,
            key="muv_v0",
        )

    with col2:

        a = st.slider(
            "Aceleração (m/s²)",
            -10.0,
            10.0,
            2.0,
            key="muv_a",
        )

        tempo_max = st.slider(
            "Tempo da simulação (s)",
            1.0,
            30.0,
            10.0,
            key="muv_t",
        )

    t = np.linspace(0, tempo_max, 400)

    s = s0 + v0 * t + 0.5 * a * t**2
    v = v0 + a * t
    acc = np.full_like(t, a)

    vf = v[-1]
    sf = s[-1]

    c1, c2, c3 = st.columns(3)

    with c1:
        card(
            "Posição final",
            f"{sf:.2f}",
            "m",
        )

    with c2:
        card(
            "Velocidade final",
            f"{vf:.2f}",
            "m/s",
        )

    with c3:
        card(
            "Aceleração",
            f"{a:.2f}",
            "m/s²",
        )

    st.divider()

    # --------------------------------------------------------
    # POSIÇÃO E VELOCIDADE
    # --------------------------------------------------------

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=t,
            y=s,
            mode="lines",
            name="Posição",
            line=dict(width=3),
        )
    )

    fig.add_trace(
        go.Scatter(
            x=t,
            y=v,
            mode="lines",
            name="Velocidade",
            yaxis="y2",
            line=dict(width=3),
        )
    )

    fig.update_layout(
        template="plotly_dark",
        height=500,
        title="Posição e velocidade",
        xaxis_title="Tempo (s)",
        yaxis=dict(
            title="Posição (m)",
        ),
        yaxis2=dict(
            title="Velocidade (m/s)",
            overlaying="y",
            side="right",
        ),
        hovermode="x unified",
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

    # --------------------------------------------------------
    # ACELERAÇÃO
    # --------------------------------------------------------

    fig2 = go.Figure()

    fig2.add_trace(
        go.Scatter(
            x=t,
            y=acc,
            mode="lines",
            name="Aceleração",
            line=dict(width=3),
        )
    )

    fig2 = grafico_base(
        fig2,
        "Aceleração × tempo",
        "Tempo (s)",
        "Aceleração (m/s²)",
    )

    st.plotly_chart(
        fig2,
        use_container_width=True,
    )

    # --------------------------------------------------------
    # TORRICELLI
    # --------------------------------------------------------

    st.subheader("Equação de Torricelli")

    delta_s = sf - s0

    if abs(delta_s) > 1e-12:

        torricelli = v0**2 + 2 * a * delta_s

        if torricelli >= 0:

            formula(
                r"v^2 = v_0^2 + 2a\Delta s"
            )

            st.latex(
                rf"v^2 = {torricelli:.2f}\;\mathrm{{m^2/s^2}}"
            )

            velocidade_torricelli = np.sqrt(torricelli)

            st.metric(
                "Módulo da velocidade final",
                f"{velocidade_torricelli:.2f} m/s",
            )

        else:

            st.warning(
                "O valor calculado para v² é negativo. "
                "Não existe velocidade real para esses parâmetros."
            )


# ============================================================
# QUEDA LIVRE
# ============================================================

elif pagina == "⬇️ Queda livre":

    st.header("⬇️ Queda Livre")

    st.write(
        """
        Na queda livre, desprezando a resistência do ar, o corpo
        sofre aceleração constante devido à gravidade.
        """
    )

    formula(
        r"h(t) = h_0 + v_0t - \frac{1}{2}gt^2"
    )

    formula(
        r"v(t) = v_0 - gt"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        altura = st.slider(
            "Altura inicial (m)",
            1.0,
            500.0,
            100.0,
        )

    with col2:

        g = st.slider(
            "Gravidade (m/s²)",
            1.0,
            20.0,
            9.8,
            step=0.1,
        )

    with col3:

        v0 = st.slider(
            "Velocidade inicial (m/s)",
            -20.0,
            20.0,
            0.0,
        )

    # --------------------------------------------------------
    # TEMPO DE QUEDA
    # --------------------------------------------------------

    discriminante = v0**2 + 2 * g * altura

    tempo_queda = (
        v0 + np.sqrt(discriminante)
    ) / g

    t = np.linspace(
        0,
        tempo_queda,
        400,
    )

    y = altura + v0 * t - 0.5 * g * t**2
    velocidade = v0 - g * t

    y = np.maximum(y, 0)

    c1, c2, c3 = st.columns(3)

    with c1:
        card(
            "Tempo de queda",
            f"{tempo_queda:.2f}",
            "s",
        )

    with c2:
        card(
            "Velocidade final",
            f"{velocidade[-1]:.2f}",
            "m/s",
        )

    with c3:
        card(
            "Gravidade",
            f"{g:.2f}",
            "m/s²",
        )

    st.divider()

    # --------------------------------------------------------
    # ALTURA
    # --------------------------------------------------------

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=t,
            y=y,
            mode="lines",
            name="Altura",
            line=dict(width=3),
        )
    )

    fig = grafico_base(
        fig,
        "Queda livre — altura × tempo",
        "Tempo (s)",
        "Altura (m)",
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

    # --------------------------------------------------------
    # VELOCIDADE
    # --------------------------------------------------------

    fig2 = go.Figure()

    fig2.add_trace(
        go.Scatter(
            x=t,
            y=velocidade,
            mode="lines",
            name="Velocidade",
            line=dict(width=3),
        )
    )

    fig2 = grafico_base(
        fig2,
        "Queda livre — velocidade × tempo",
        "Tempo (s)",
        "Velocidade (m/s)",
    )

    st.plotly_chart(
        fig2,
        use_container_width=True,
    )


# ============================================================
# LANÇAMENTO VERTICAL
# ============================================================

elif pagina == "🚀 Lançamento vertical":

    st.header("🚀 Lançamento Vertical")

    st.write(
        """
        Um corpo é lançado verticalmente para cima com velocidade
        inicial positiva. A aceleração da gravidade atua para baixo.
        """
    )

    formula(
        r"v(t) = v_0 - gt"
    )

    formula(
        r"y(t) = y_0 + v_0t - \frac{1}{2}gt^2"
    )

    formula(
        r"v^2 = v_0^2 - 2g\Delta y"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        v0 = st.slider(
            "Velocidade inicial (m/s)",
            1.0,
            100.0,
            20.0,
        )

    with col2:

        y0 = st.slider(
            "Altura inicial (m)",
            0.0,
            100.0,
            0.0,
        )

    with col3:

        g = st.slider(
            "Gravidade (m/s²)",
            1.0,
            20.0,
            9.8,
            step=0.1,
        )

    # --------------------------------------------------------
    # CÁLCULOS
    # --------------------------------------------------------

    tempo_subida = v0 / g

    altura_maxima = (
        y0 + v0**2 / (2 * g)
    )

    # Tempo para retornar à altura inicial
    tempo_total = 2 * tempo_subida

    t = np.linspace(
        0,
        tempo_total,
        400,
    )

    y = (
        y0
        + v0 * t
        - 0.5 * g * t**2
    )

    v = v0 - g * t

    c1, c2, c3 = st.columns(3)

    with c1:

        card(
            "Tempo de subida",
            f"{tempo_subida:.2f}",
            "s",
        )

    with c2:

        card(
            "Altura máxima",
            f"{altura_maxima:.2f}",
            "m",
        )

    with c3:

        card(
            "Tempo total",
            f"{tempo_total:.2f}",
            "s",
        )

    st.divider()

    # --------------------------------------------------------
    # POSIÇÃO
    # --------------------------------------------------------

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=t,
            y=y,
            mode="lines",
            name="Altura",
            line=dict(width=3),
        )
    )

    fig.add_hline(
        y=altura_maxima,
        line_dash="dash",
        annotation_text="Altura máxima",
    )

    fig = grafico_base(
        fig,
        "Lançamento vertical — posição × tempo",
        "Tempo (s)",
        "Altura (m)",
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

    # --------------------------------------------------------
    # VELOCIDADE
    # --------------------------------------------------------

    fig2 = go.Figure()

    fig2.add_trace(
        go.Scatter(
            x=t,
            y=v,
            mode="lines",
            name="Velocidade",
            line=dict(width=3),
        )
    )

    fig2.add_hline(
        y=0,
        line_dash="dash",
    )

    fig2 = grafico_base(
        fig2,
        "Lançamento vertical — velocidade × tempo",
        "Tempo (s)",
        "Velocidade (m/s)",
    )

    st.plotly_chart(
        fig2,
        use_container_width=True,
    )

    st.subheader("Equações")

    st.latex(
        r"v(t) = v_0 - gt"
    )

    st.latex(
        r"y(t) = y_0 + v_0t - \frac{1}{2}gt^2"
    )

    st.latex(
        r"v^2 = v_0^2 - 2g\Delta y"
    )