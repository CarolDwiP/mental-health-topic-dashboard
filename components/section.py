import streamlit as st


def section_title(title):

    st.markdown(
        f"""
        <h2 class="section-title">{title}</h2>
        """,
        unsafe_allow_html=True,
    )


def section_text(text):

    st.markdown(
        f"""
        <p class="section-text">
        {text}
        </p>
        """,
        unsafe_allow_html=True,
    )


def info_box(text):

    st.markdown(
        f"""
        <div class="info-box">
        {text}
        </div>
        """,
        unsafe_allow_html=True,
    )