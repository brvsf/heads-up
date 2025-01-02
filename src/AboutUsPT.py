import streamlit as st

def page():

    with st.sidebar:
        st.header("Menu")
        if st.button("🕹️ Voltar ao jogo"):
            st.switch_page("HeadsUp.py")

    st.title('Projeto: Jogo de "Heads Up" no Streamlit e Slack')

    st.markdown("""
    ## Olá, sou o Bruno, criador deste projeto!

    Neste espaço, vou te contar um pouco mais sobre o **Heads Up**, um jogo descontraído que você pode jogar no trabalho ou com os amigos.

    O projeto nasceu de uma conversa entre amigos, com o objetivo de tornar os ambientes de trabalho mais divertidos e descontraídos. A ideia é simples: criar um bot no Slack que permite jogar o famoso jogo **"Heads Up"** (ou **"Quem sou eu"**) em grupo, com os colegas.

    A página do **Streamlit** serve como prova de conceito, sendo o primeiro passo para a integração com o Slack.

    ## O que é esse projeto?

    Este é um **projeto Open Source**, o que significa que você pode analisar, clonar e até brincar com o código disponível no [GitHub](https://github.com/brvsf/heads-up).

    Fique à vontade para explorar e contribuir com o desenvolvimento!

    ## Informações de Contato

    Se você quiser entrar em contato, estou disponível nos seguintes canais:

    - **[E-mail](mailto:brvieirasf@gmail.com)**
    - **[LinkedIn](https://www.linkedin.com/in/brvsf)**
    - **[GitHub](https://github.com/brvsf)**

    Fique à vontade para mandar uma mensagem ou conectar-se!
    """)

if __name__ == "__page__":
    page()
