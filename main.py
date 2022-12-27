import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(
    page_title="CWU Fitlab"
)

# -- CSS styling --
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# -- Header --
st.title("Welcome to CWU Fitlab!")

with st.container():
    fitlab_img = Image.open('img/fitlab-img.png')
    st.image(fitlab_img, caption="Students during Fitlab")
    st.header('Overview')
    st.subheader('What is fit lab? Who can participate? How much does it cost?')
    st.write(
        '''
        - CWU Fit Lab is a comprehensive fitness assessment experience provided by trained CWU students pursuing a degree in Exercise Science. 
        We offer two services: Full fitness assessments and body composition only assessments.  
        - Cost: These assessments are free of charge and available to anyone 18 years of age and older (community members, students, faculty, etc.).  
        
        Please note that proof of COVID-19 vaccination is required at the time of scheduling
        '''
    )

    st.header("FAQ")
    with st.expander("What exactly does each fitness evaluation (body composition vs. full fitness) assess?"):
        st.write(
            '''
            - Full fitness assessment: Includes a series of physical tests that assess five components of fitness: cardiorespiratory fitness (how well your heart and lungs can supply oxygen to your working muscles during exercise), body composition (proportion of fat versus fat free mass and associated health risk), flexibility, muscular strength and endurance. 
            - Body composition only assessment: The body composition only service focuses on two measurements for body composition (underwater weighing and three or seven site skinfold) with comparison of individual results to age-related norms and assessment of associated health risk. 
            
            - How long does it take? The full fitness assessment takes about 75 minutes.  The body composition only option takes approximately 40 minutes.
            When can I participate this quarter? Times and days vary based on the academic quarter.  
            '''
        )
    with st.expander("What can participants do with their assessment report?"):
        st.write(
            """
            A full fitness assessment will evaluate an individual's overall fitness level.
            Typically, a more fit individual has a lower risk for developing disease or disability, 
            an improved quality of life, and the capacity to complete activities of daily living 
            with greater ease.  The results from a full fitness assessment can help to establish 
            a baseline (determining the student's current fitness level and a starting point for 
            exercise programming) and if repeated after an exercise training program, can show progress 
            made toward health or fitness related goals. 
            """
        )

    with st.expander("How can athletes specifically benefit from taking the evaluation?"):
        st.write(
            """
            For athletes, a fitness evaluation serves to measure their readiness for sport-related 
            activities (for example, a higher cardiorespiratory fitness level may translate to 
            improved cardiovascular sport performance like running or cycling) and can also identify 
            areas in need of improvement to optimize sport performance. 
            """
        )
with st.sidebar:
    st.title('Fitlab')
    st.markdown("Click [here](https://calendly.com/) to schedule an assessment or come to Heath Sciences 117 during open hours!")
    st.subheader("Hours of Operation")
    st.write(
        """
        - Monday: 5-7pm
        - Wednesday: 1-4pm
        """
    )
    st.subheader("Location")
    st.write(
        """
        - Central Washington University Health Sciences Building
        - Room 117
        """
    )
