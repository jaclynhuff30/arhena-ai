import streamlit as st
import pandas as pd

# Load your expanded CSV
df = pd.read_csv("arhena_ai_master_spreadsheet.csv")

st.set_page_config(page_title="Arhena AI Compound Explorer", layout="wide")
st.title("🧬 Arhena AI: Compound Discovery Dashboard")

st.sidebar.header("🔍 Filter Options")

# Sidebar filters
condition = st.sidebar.multiselect("Condition", options=sorted(df["Condition"].unique()))
focus_area = st.sidebar.multiselect("Focus Area", options=sorted(df["Focus Area"].unique()))
target = st.sidebar.multiselect("Molecular Target(s)", options=sorted(df["Molecular Target(s)"].dropna().unique()))
trial_status = st.sidebar.multiselect("Clinical Trial Status", options=sorted(df["Clinical Trial Status"].dropna().unique()))
grant_source = st.sidebar.multiselect("Grant Source", options=sorted(df["Grant Source"].dropna().unique()))

# Arhena Score slider
score_range = st.sidebar.slider("Arhena Score Range", 0.0, 100.0, (70.0, 100.0))

# Filter logic
filtered_df = df[
    (df["Arhena Score"] >= score_range[0]) &
    (df["Arhena Score"] <= score_range[1])
]

if condition:
    filtered_df = filtered_df[filtered_df["Condition"].isin(condition)]
if focus_area:
    filtered_df = filtered_df[filtered_df["Focus Area"].isin(focus_area)]
if target:
    filtered_df = filtered_df[filtered_df["Molecular Target(s)"].isin(target)]
if trial_status:
    filtered_df = filtered_df[filtered_df["Clinical Trial Status"].isin(trial_status)]
if grant_source:
    filtered_df = filtered_df[filtered_df["Grant Source"].isin(grant_source)]

st.markdown("### 🔬 Filtered Results")
st.dataframe(filtered_df, use_container_width=True)

# Export option
st.download_button(
    label="📁 Download Filtered CSV",
    data=filtered_df.to_csv(index=False).encode('utf-8'),
    file_name="arhena_filtered_results.csv",
    mime="text/csv"
)

st.markdown("---")
st.caption("Arhena AI: Built for Healing. Powered by Science. ✨")
