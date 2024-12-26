import streamlit as st

def main():

    game = st.Page(
        "HeadsUp.py",
        title="Heads Up",
        url_path="Home"
    )

    pg = st.navigation([
        game
    ], position='hidden')

    pg.run()

if __name__ == '__main__':
    main()
