from pathlib import Path

import pandas as pd
import streamlit as st


@st.cache_data
def load_csv(path: Path):
    """
    Membaca file CSV.
    """
    return pd.read_csv(path)


def load_css(css_file: Path):
    """
    Memuat file CSS.
    """
    with open(css_file) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True,
        )


def metric_card(title, value):
    """
    Card sederhana untuk metrik.
    """
    st.markdown(
        f"""
        <div class="metric-card">
            <h4>{title}</h4>
            <h2>{value}</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )