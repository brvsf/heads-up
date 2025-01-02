import streamlit as st

def page():

    with st.sidebar:
        st.header("Menu")
        if st.button("🕹️ Back to the game"):
            st.switch_page("HeadsUp.py")

    st.title('Project: "Heads Up" game on Streamlit and Slack')

    st.markdown("""
    ## Hi, I'm Bruno, the creator of this project!

    In this section, I'll tell you a little more about **Heads Up**, a casual game you can play at work or with friends.

    The project was born from a conversation among friends, aiming to make work environments more fun and relaxed. The idea is simple: create a bot on Slack that allows people to play the famous game **"Heads Up"** (or **"Who Am I"**) in a group with colleagues.

    The **Streamlit** page serves as a proof of concept, being the first step towards integration with Slack.

    ## What is this project?

    This is an **Open Source project**, which means you can explore, clone, and even play around with the code available on [GitHub](https://github.com/brvsf/heads-up).

    Feel free to explore and contribute to the development!

    ## Contact Information

    If you'd like to get in touch, you can reach me through the following channels:

    - **[E-mail](mailto:brvieirasf@gmail.com)**
    - **[LinkedIn](https://www.linkedin.com/in/brvsf)**
    - **[GitHub](https://github.com/brvsf)**

    Feel free to send a message or connect!
    """)

if __name__ == "__page__":
    page()
