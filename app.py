import streamlit as st

from llm_service import analyze_incident

st.set_page_config(
    page_title="SAP Incident AI",
    layout="wide"
)

st.title("SAP Incident AI")

st.write(
    "Convert raw incidents into structured SAP-ready enterprise incident records."
)

incident_text = st.text_area(
    "Describe the incident",
    height=200
)

if st.button("Analyze Incident"):

    if not incident_text.strip():
        st.warning("Please enter an incident.")

    else:

        with st.spinner("Analyzing incident..."):

            result = analyze_incident(incident_text)

            st.success("Analysis complete")

            st.subheader("Business Summary")
            st.write(result.get("business_summary", "N/A"))

            st.subheader("Technical Summary")
            st.write(result.get("technical_summary", "N/A"))

            col1, col2 = st.columns(2)

            with col1:

                st.subheader("SAP Module")
                st.write(result.get("sap_module", "UNKNOWN"))

                st.subheader("Incident Type")
                st.write(result.get("incident_type", "UNKNOWN"))

                st.subheader("Priority")
                st.write(result.get("priority", "UNKNOWN"))

                st.subheader("Reproducibility")
                st.write(result.get("reproducibility", "Unknown"))

            with col2:

                st.subheader("Business Impact")
                st.write(result.get("business_impact", "N/A"))

                st.subheader("Probable Root Cause")
                st.write(result.get("probable_root_cause", "N/A"))

                st.subheader("Suggested Team")
                st.write(result.get("suggested_team", "UNKNOWN"))

                st.subheader("SAP Object")
                st.write(result.get("sap_object", "UNKNOWN"))

            st.subheader("Keywords")
            st.write(result.get("keywords", []))

            st.subheader("Suggested Debugging Steps")

            debugging_steps = result.get(
                "suggested_debugging_steps",
                []
            )

            for step in debugging_steps:
                st.write(f"- {step}")

            st.subheader("Confidence Score")

            confidence = result.get(
                "confidence_score",
                0.0
            )

            st.progress(confidence)

            st.subheader("Raw JSON")
            st.json(result)