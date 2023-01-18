# import packages
import streamlit as st
import pandas as pd
import plotly.express as px
from markdownlit import mdlit
from database import fetch_client_data, client_bool
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.colored_header import colored_header

st.set_page_config(
    page_title="Client Dashboard",
    layout='wide'
)

# Styles metric cards
style_metric_cards(
    border_left_color="#ffe9e9",
    border_size_px=1.2,
    border_radius_px=10,
    border_color="#000000"
)

# fetches data from github
@st.cache
def fetch_vo2_data(url):
    df = pd.read_csv(url)
    return df

# subsets data
@st.cache
def subset_data(df):
    df_vo2 = df[df['CVDESVO2'].notna()]
    df_vo2 = df_vo2[df_vo2['CVDESVO2'] < 90]
    return df_vo2

@st.cache
def fetch_bf_data(path):
    df = pd.read_csv(path)
    return df

#bf = fetch_bf_data('/Users/jdickinson/Documents/PersonalRepos/cwu-fitlab/data/final/dexa_nhanes_cleaned.csv')
df = fetch_vo2_data('https://raw.githubusercontent.com/jonathjd/cwu-fitlab/main/data/processed/nhanes_merged.csv')
df_vo2 = subset_data(df)

## Helper Methods ##
def plot_vo2_histogram(vo2max, gender):
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

## body fat figs ##


with st.sidebar:
    st.markdown(
        '<img src="https://github.com/jonathjd/cwu-fitlab/blob/main/img/cwu-long.png?raw=true" alt="0" style="width: 304px;margin-top: -400px;">',
        unsafe_allow_html=True
    )

    client = st.text_input(label="Enter Client ID", placeholder="e.g. EX01171996")
    if client_bool(client):
        st.success("Welcome!")

    mdlit (
        """Check out our [calendar](https://calendly.com/cwu-fitlab/assessment) to schedule an assessment or come to [red]Heath 
        Sciences 117[/red] during open hours! 
        If you have any further questions feel free to email **[blue]fitlab@cwu.edu[/blue]**.
        """
    )
    st.subheader("Hours of Operation")
    st.write(
        """
        - Monday: 4-7pm
        - Tuesday: 2-4pm
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
    client. These normative charts were created from [NHANES](https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/overviewexam.aspx?BeginYear=1999)
    data ranging from 1999-2003.
    """
)

###### Client data ######
if client_bool(client):
    data = fetch_client_data(client)
    if client == "EX01171996":
        st.info("This is an example of what your dashboard could look like!")

    colored_header(
        label="Welcome to your client dashboard",
        color_name= "red-70",
        description="Below you'll be able to see your data from your previous Fitlab visits."
    )
    # metric cards
    col1a, col2a, col3a = st.columns(3)
    col1b, col2b, col3b = st.columns(3)
    col1c, col2c, col3c = st.columns(3)
    col1d, col2d, col3d = st.columns(3)
    col1a.metric(label="Age", value=data["age"])
    col2a.metric(label="Height (in)", value=data["height"])
    col3a.metric(label="Weight (lbs)", value=data["weight"])
    col1b.metric(label="Resting Heart Rate (BPM)", value=data["rest_hr"])
    col2b.metric(label="Systolic (mmHg)", value=data["sys"])
    col3b.metric(label="Diastolic (mmHg)", value=data["dias"])
    col1c.metric(label="VO2max (ml/kg/min)", value=data["vo2"])
    col2c.metric(label="Body fat % (Hydrostatic)", value=data["gold_skinfold"])
    col3c.metric(label="Body fat % (Skinfold)", value=data["skinfold"])
    col1d.metric(label="Sit and Reach", value=data["sit_reach"])
    col2d.metric(label="Push ups", value=data["push_up"])

## VO2 ##
with st.expander("Normative values for VO2max"):
    l_hist, r_hist = st.columns([1.2,3])
    with l_hist:
        # st.subheader('Normative values for VO2max')
        gender_options = ["Male", "Female", "Both"]
        c_gender = st.selectbox('Select gender', gender_options)
        c_vo2 = st.slider(label="Estimated VO2max (ml/kg/min)", 
            min_value=10.0, max_value=80.0, value=40.0
            )
    with r_hist:
        plot_vo2_histogram(c_vo2, c_gender)

## BF% ##
