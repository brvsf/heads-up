import streamlit as st

def main():

    game = st.Page(
        "HeadsUp.py",
        title="Heads Up",
        url_path="Home"
    )

    about_us_pt = st.Page(
        "AboutUsPT.py",
        title="About Us PT",
        url_path="AboutUsPT"
    )

    about_us_en = st.Page(
        "AboutUsEN.py",
        title="About Us EN",
        url_path="AboutUsEN"
    )

    pg = st.navigation([
        game, about_us_pt, about_us_en
    ], position='hidden')

    pg.run()

if __name__ == '__main__':
    main()
