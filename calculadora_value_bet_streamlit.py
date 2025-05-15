
import streamlit as st

st.title("🎾 Calculadora de Value Bet - Tênis")

st.markdown("Preencha os dados dos jogadores e veja se há uma **value bet** com base em Elo, Elo de superfície e odds.")

# Entrada de dados
st.header("📋 Dados dos Jogadores")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Jogador 1")
    elo1 = st.number_input("Elo Geral (J1)", value=1760.2, step=0.1)
    celo1 = st.number_input("Elo Superfície (J1)", value=1674.5, step=0.1)
    odd1 = st.number_input("Odd da Casa (J1)", value=1.57)

with col2:
    st.subheader("Jogador 2")
    elo2 = st.number_input("Elo Geral (J2)", value=1618.0, step=0.1)
    celo2 = st.number_input("Elo Superfície (J2)", value=1565.9, step=0.1)
    odd2 = st.number_input("Odd da Casa (J2)", value=2.32)

if st.button("🔍 Calcular"):
    # Cálculo Elo
    p_elo_1 = 1 / (1 + 10 ** ((elo2 - elo1) / 400))
    p_elo_2 = 1 - p_elo_1

    # Cálculo cElo
    p_celo_1 = 1 / (1 + 10 ** ((celo2 - celo1) / 400))
    p_celo_2 = 1 - p_celo_1

    # Probabilidade implícita
    p_odd_1 = 1 / odd1
    p_odd_2 = 1 / odd2
    total = p_odd_1 + p_odd_2

    # Ajuste vigorish
    p_market_1 = p_odd_1 / total
    p_market_2 = p_odd_2 / total

    # Prob modelo
    p_model_1 = 0.25 * p_elo_1 + 0.45 * p_celo_1 + 0.30 * p_market_1
    p_model_2 = 1 - p_model_1

    # Value
    value_1 = p_model_1 - p_market_1
    value_2 = p_model_2 - p_market_2

    st.subheader("📊 Resultados")

    st.write(f"**Probabilidade (modelo) - Jogador 1:** {p_model_1:.3f}")
    st.write(f"**Probabilidade (mercado) - Jogador 1:** {p_market_1:.3f}")
    st.write(f"**Value Bet - Jogador 1:** {value_1:.2%} {'✅' if value_1 > 0.03 else '❌'}")

    st.write("---")

    st.write(f"**Probabilidade (modelo) - Jogador 2:** {p_model_2:.3f}")
    st.write(f"**Probabilidade (mercado) - Jogador 2:** {p_market_2:.3f}")
    st.write(f"**Value Bet - Jogador 2:** {value_2:.2%} {'✅' if value_2 > 0.03 else '❌'}")
