import streamlit as st


def hero(title: str, subtitle: str):
    """
    Menampilkan Hero Section Dashboard.
    """

    st.markdown(
        f"""
        <h1 class="hero-title">{title}</h1>
        <p class="hero-subtitle">{subtitle}</p>
        """,
        unsafe_allow_html=True,
    )