
import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Arhena AI", layout="centered")

# --- Header ---
st.title("Arhena AI")
st.subheader("AI-Powered Drug Discovery")
st.markdown("*Built to Understand All Women.*")

# --- Focus Area Selection ---
st.markdown("### Select Your Focus Area")
focus_area = st.selectbox("Choose one:", ["Women's Health", "Regenerative Medicine", "Oncology"])

# --- Condition Input ---
st.markdown("### Describe the Condition or Target")
condition = st.text_input("Enter your condition or area of interest (e.g., endometriosis, cervical cancer):")

# --- Language Option ---
st.markdown("### Preferred Output Language")
language = st.selectbox("Choose a language:", ["English", "Spanish", "French", "Mandarin", "Arabic", "Hindi"])

# --- Consent Notice ---
st.markdown("### Consent and Disclaimer")
consent = st.checkbox("I acknowledge this is an informational tool, not medical advice.")

# --- Submit Button ---
if st.button("Generate Results", key="generate_btn"):
    if condition and consent:
        st.markdown("### 🧬 Nova AI Results")
        st.write(f"**🔬 Focus Area:** {focus_area}")
        st.write(f"**🩺 Condition:** {condition}")
        st.write("**🧪 Suggested Compounds:** [Sample Compound A, Sample Compound B]")
        st.write("**⚙️ Mechanism of Action:** [e.g., Anti-inflammatory, Estrogen Receptor Modulation]")
        st.write("**🔗 Clinical Trials:** [Link to PubMed, ClinicalTrials.gov]")
        st.write("**🧠 Arhena Score:** 82 (Beta™)")
        st.download_button("Download Results (PDF)", "Coming soon", disabled=True)
        st.button("Translate Results")
    else:
        st.warning("Please enter a condition and accept the disclaimer.")

