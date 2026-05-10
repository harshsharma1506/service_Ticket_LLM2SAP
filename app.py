import streamlit as st

from llm_service import analyze_incident

st.set_page_config(
    page_title="SAP Incident AI",
    layout="wide"
)

st.title("SAP Incident AI")

st.write(
    "Convert raw incidents into structured SAP-ready incident records."
)

incident_text = st.text_area(
    "Describe the incident",
    height=200
)

if st.button("Analyze Incident"):

    if not incident_text.strip():
        st.warning("Please enter an incident.")
    else:

        with st.spinner("Analyzing..."):

            try:

                result = analyze_incident(incident_text)

                st.success("Analysis complete")

                col1, col2 = st.columns(2)

                with col1:
                    st.subheader("Business Summary")
                    st.write(result["business_summary"])

                    st.subheader("Module")
                    st.write(result["module"])

                    st.subheader("Priority")
                    st.write(result["priority"])

                    st.subheader("Reproducibility")
                    st.write(result["reproducibility"])

                with col2:
                    st.subheader("Technical Summary")
                    st.write(result["technical_summary"])

                    st.subheader("Probable Root Cause")
                    st.write(result["probable_root_cause"])

                    st.subheader("Suggested Team")
                    st.write(result["suggested_team"])

                st.subheader("Keywords")
                st.write(result["keywords"])

                st.subheader("Raw JSON")
                st.json(result)

            except Exception as e:
                st.error(str(e))