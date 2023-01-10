# import packages
import streamlit as st
import pandas as pd
import plotly.express as px
from markdownlit import mdlit

st.set_page_config(
    page_title="Client Dashboard",
    layout='wide'
)

# fetches data from github
@st.cache
def fetch_data(url):
    df = pd.read_csv(url)
    return df

# subsets data
@st.cache
def subset_data(df):
    df_vo2 = df[df['CVDESVO2'].notna()]
    df_vo2 = df_vo2[df_vo2['CVDESVO2'] < 90]
    return df_vo2

df = fetch_data('https://raw.githubusercontent.com/jonathjd/cwu-fitlab/main/data/processed/nhanes_merged.csv')
df_vo2 = subset_data(df)

## Helper Methods ##
def plot_vo2_histogram(age, vo2max, gender):
    line_placement = vo2max
    if gender == "Male":
        men_df = df_vo2[df_vo2['RIAGENDR'] == 1]
        fig = px.histogram(
        men_df, 
        x='CVDESVO2', 
        nbins=25,
        labels={
            "CVDESVO2": "Estimated VO2max (ml/kg/min)"
        },
        template="simple_white",
        color_discrete_sequence = ['grey'],
    )

        male_mean_line = men_df['CVDESVO2'].mean() # vo2 mean male
        fig.add_vline(
            type="line",
            line_color="red",
            line_width=4,
            opacity=1,
            line_dash="dot",
            x=male_mean_line
        )
        fig.add_annotation(
            text="Avg Male VO2max",
            x=male_mean_line,
            y=1050,
            arrowhead=2,
            showarrow=True
        )
        fig.add_vline(
            type="line",
            line_color="black",
            line_width=4,
            opacity=1,
            line_dash="dot",
            x=line_placement
        )
        fig.add_annotation(
            text="You",
            x=line_placement,
            y=1050,
            arrowhead=2,
            showarrow=True
        )

    if gender == "Female":
        fem_df = df_vo2[df_vo2['RIAGENDR'] == 2]
        fig = px.histogram(
        fem_df, 
        x='CVDESVO2', 
        nbins=25,
        labels={
            "CVDESVO2": "Estimated VO2max (ml/kg/min)"
        },
        template="simple_white",
        color_discrete_sequence = ['grey'],
    )
        fem_mean_line = fem_df['CVDESVO2'].mean() # vo2 mean female
        fig.add_vline(
            type="line",
            line_color="red",
            line_width=4,
            opacity=1,
            line_dash="dot",
            x=fem_mean_line
        )
        fig.add_annotation(
            text="Avg female VO2max",
            x=fem_mean_line,
            y=1050,
            arrowhead=2,
            showarrow=True
        )
        fig.add_vline(
            type="line",
            line_color="black",
            line_width=4,
            opacity=1,
            line_dash="dot",
            x=line_placement
        )
        fig.add_annotation(
            text="You",
            x=line_placement,
            y=1050,
            arrowhead=2,
            showarrow=True
        )
    if gender == "Both":
        fig = px.histogram(
        df_vo2, 
        x='CVDESVO2', 
        nbins=25,
        labels={
            "CVDESVO2": "Estimated VO2max (ml/kg/min)"
        },
        template="simple_white",
        color_discrete_sequence = ['grey'],
    )
        mean_line = df_vo2['CVDESVO2'].mean() # vo2 mean
        fig.add_vline(
            type="line",
            line_color="red",
            line_width=4,
            opacity=1,
            line_dash="dot",
            x=mean_line
        )
        fig.add_annotation(
            text="Avg VO2max",
            x=mean_line,
            y=2050,
            arrowhead=2,
            showarrow=True
        )
        fig.add_vline(
            type="line",
            line_color="black",
            line_width=4,
            opacity=1,
            line_dash="dot",
            x=line_placement
        )
        fig.add_annotation(
            text="You",
            x=line_placement,
            y=1050,
            arrowhead=2,
            showarrow=True
        )
    fig.update_layout(
    font=dict(
        size=18,  # Set the font size here
    )
)

    st.plotly_chart(fig, use_container_width=True)

def describe_vo2(line_placement):
    pass

with st.sidebar:
    st.markdown(
        '<img src="https://github.com/jonathjd/cwu-fitlab/blob/main/img/cwu-long.png?raw=true" alt="0" style="width: 304px;margin-top: -400px;">',
        unsafe_allow_html=True
    )
    mdlit (
        """Check out our [calendar](https://calendly.com/cwu-fitlab/assessment) to schedule an assessment or come to [red]Heath 
        Sciences 117[/red] during open hours! 
        If you have any further questions feel free to email **[blue]fitlab@cwu.edu[/blue]**.
        """
    )
    st.subheader("Hours of Operation")
    st.write(
        """
        - Monday: 5-7pm
        - Tuesday: 1-4pm
        """
    )
    st.subheader("Location")
    st.write(
        """
        - Central Washington University Health Sciences Building
        - Room 117
        """
    )

# cols to center title
l_0, mid, r_0 = st.columns([1, 2, 1])
with mid:
    st.title('Client Dashboard')

st.markdown(
    """
    Welcome to the Fitlab's Client Dashboard! Here you can input your results from your
    recent fitness assessment and see how your measurements rank amongst similar individuals.
    You also will be able to observe your growth over time if you are a repeat 
    client (**coming soon!**). These normative charts were created from [NHANES](https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/overviewexam.aspx?BeginYear=1999)
    data ranging from 1999-2003.
    """
)

## VO2 ##
l_hist, r_hist = st.columns([1.2,3])
with l_hist:
    st.subheader('Normative values for VO2max')
    gender_options = ["Male", "Female", "Both"]
    c_gender = st.selectbox('Select gender', gender_options)
    c_vo2 = st.slider(label="Estimated VO2max (ml/kg/min)", 
        min_value=10.0, max_value=80.0, value=40.0
        )
    c_age = st.slider(label="Enter age", 
        min_value=18, max_value=80, value=25
        )
with r_hist:
    plot_vo2_histogram(c_age, c_vo2, c_gender)

## BF% ##
