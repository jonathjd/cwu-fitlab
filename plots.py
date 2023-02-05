import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# Example data for example plots
def example_data():
    vo2_assess = ['YMCA', 'YMCA', 'YMCA', 'Queens College Step Test', 'Queens College Step Test']
    push_up = [18, 19, 22, 25, 30]
    weight = [234, 229, 227, 225, 220]
    skin_fold = [28.2, 25.3, 26, 22.6, 17]
    height = [70, 70, 70, 70, 70]
    systolic = [134, 132, 126, 122, 118]
    diastolic = [84, 82, 82, 80, 78]
    rest_hr = [82, 80, 80, 74, 66]
    sit_reach = [24, 22, 28, 29, 30]
    age = [22, 22, 22, 22, 23]
    vo2 = [30, 34, 34, 39, 45]
    dates = ['2023-01-13', '2023-01-28', '2023-02-09', '2023-02-23', '2023-03-11']
    example = pd.DataFrame(zip(weight, vo2_assess, push_up, skin_fold, height, systolic, diastolic, rest_hr, sit_reach, age, vo2, dates))
    example.columns = ['Weight','VO2 Assessment', 'Push Ups', 'Body Fat (%)', 'Height (in)', 'Systolic BP (mmHg)', 'Diastolic BP (mmHg)', 'Resting Heart Rate (BPM)', 'Sit and Reach (cm)', 'Age', 'VO2Max (ml/kg/min)', 'Visit Date']
    example['Visit Date'] = pd.to_datetime(example['Visit Date'])
    return example

def plot_vo2(df):
    if len(df) == 1:
        df['VO2Max (ml/kg/min)'] = df['VO2Max (ml/kg/min)'].round() 
        # Generate fake data
        fake_data = np.arange(df['VO2Max (ml/kg/min)'].iloc[0], 60)
        fake_dates = pd.date_range(df['Visit Date'].iloc[0], periods=7)
        
        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=fake_dates, 
            y=fake_data,
            mode='lines+markers',
            name='Future progress!',
            line=dict(shape='linear', color='#FF3F3F', dash='dot'),
            marker=dict(size=12,
            line=dict(width=1.1)
            )))

        fig.add_trace(go.Scatter(
            x=df['Visit Date'],
            y=df['VO2Max (ml/kg/min)'],
            mode='lines+markers',
            name='Your Visit',
            line=dict(shape='linear', color='black', dash='dot'),
            marker=dict(size=14,
            line=dict(width=1.1)
            )))
        fig.update_layout(
            xaxis=dict(
                showline=True,
                showgrid=False,
                showticklabels=True,
                linewidth=3,
                ticks='outside',
                tickwidth=2,
                tickcolor='black',
                tickfont=dict(
                    family='Arial',
                    size=12,
                    color='rgb(82, 82, 82)',
                ),
                title='Visit Date'
            ),
            yaxis=dict(
                showgrid=True,
                linewidth=3,
                showline=True,
                showticklabels=True,
                ticks='outside',
                ticklen=4,
                tickwidth=2,
                tickcolor='black',
                title='VO2Max (ml/kg/min)'
            ),
            autosize=False,
            legend=dict(
                orientation="h",
                entrywidth=90,
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            ),
            margin=dict(
                autoexpand=False,
                l=100,
                r=20,
                t=110,
            ),
            showlegend=True,
            plot_bgcolor='white'
            )

        st.plotly_chart(fig, use_container_width=True)
        return

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df['Visit Date'],
        y=df['VO2Max (ml/kg/min)'],
        mode='lines+markers',
        name='Your Visit',
        line=dict(shape='linear', color='#FF3F3F'),
        marker=dict(size=14,
        line=dict(width=1.1)
        )))
        
    fig.update_layout(
        xaxis=dict(
            showline=True,
            showgrid=False,
            showticklabels=True,
            linewidth=3,
            ticks='outside',
            tickwidth=2,
            tickcolor='black',
            tickfont=dict(
                family='Arial',
                size=12,
                color='black',
            ),
            title='Visit Date'
        ),
        yaxis=dict(
            showgrid=True,
            linewidth=3,
            showline=True,
            showticklabels=True,
            ticks='outside',
            ticklen=4,
            tickwidth=2,
            tickcolor='black',
            tickfont=dict(
                family='Arial',
                size=12,
                color='black'
            ),
            title='VO2Max (ml/kg/min)'
        ),
        autosize=False,
        margin=dict(
            autoexpand=False,
            l=100,
            r=20,
            t=110,
        ),
        plot_bgcolor='white'
        )
    st.plotly_chart(fig, use_container_width=True)
    return

def plot_push_ups(df):
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df['Visit Date'],
        y=df['Push Ups'],
        mode='lines+markers',
        line=dict(shape='linear', color='#FF3F3F'),
        marker=dict(size=14,
        line=dict(width=1.1)
        )))
        
    fig.update_layout(
        xaxis=dict(
            showline=True,
            showgrid=False,
            showticklabels=True,
            linewidth=3,
            ticks='outside',
            tickwidth=2,
            tickcolor='black',
            tickfont=dict(
                family='Arial',
                size=12,
                color='black',
            ),
            title='Visit Date'
        ),
        yaxis=dict(
            showgrid=True,
            linewidth=3,
            showline=True,
            showticklabels=True,
            ticks='outside',
            ticklen=4,
            tickwidth=2,
            tickcolor='black',
            tickfont=dict(
                family='Arial',
                size=12,
                color='black'
            ),
            title='Push Ups'
        ),
        autosize=False,
        margin=dict(
            autoexpand=False,
            l=100,
            r=20,
            t=110,
        ),
        plot_bgcolor='white'
        )
    st.plotly_chart(fig, use_container_width=True)
    return

def plot_bf(df):
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df['Visit Date'],
        y=df['Body Fat (%)'],
        mode='lines+markers',
        line=dict(shape='linear', color='#FF3F3F'),
        marker=dict(size=14,
        line=dict(width=1.1)
        )))
        
    fig.update_layout(
        xaxis=dict(
            showline=True,
            showgrid=False,
            showticklabels=True,
            linewidth=3,
            ticks='outside',
            tickwidth=2,
            tickcolor='black',
            tickfont=dict(
                family='Arial',
                size=12,
                color='black',
            ),
            title='Visit Date'
        ),
        yaxis=dict(
            showgrid=True,
            linewidth=3,
            showline=True,
            showticklabels=True,
            ticks='outside',
            ticklen=4,
            tickwidth=2,
            tickcolor='black',
            tickfont=dict(
                family='Arial',
                size=12,
                color='black'
            ),
            title='Body Fat (%)'
        ),
        autosize=False,
        margin=dict(
            autoexpand=False,
            l=100,
            r=20,
            t=110,
        ),
        plot_bgcolor='white'
        )
    st.plotly_chart(fig, use_container_width=True)
    return

def plot_bp(df):

    fig = go.Figure()

    fig.add_trace(go.Scatter( # Systolic data
        x=df['Visit Date'],
        y=df['Systolic BP (mmHg)'],
        mode='lines+markers',
        line=dict(shape='linear', color='#FF3F3F'),
        marker=dict(size=14,
        line=dict(width=1.1)
        )))

    fig.add_trace(go.Scatter( # Diastolic data
        x=df['Visit Date'],
        y=df['Diastolic BP (mmHg)'],
        mode='lines+markers',
        line=dict(shape='linear', color='#FF3F3F'),
        marker=dict(size=14,
        line=dict(width=1.1)
        )))

    fig.update_layout(
        xaxis=dict(
            showline=True,
            showgrid=False,
            showticklabels=True,
            linewidth=3,
            ticks='outside',
            tickwidth=2,
            tickcolor='black',
            tickfont=dict(
                family='Arial',
                size=12,
                color='black',
            ),
            title='Visit Date'
        ),
        yaxis=dict(
            showgrid=True,
            linewidth=3,
            showline=True,
            showticklabels=True,
            ticks='outside',
            ticklen=4,
            tickwidth=2,
            tickcolor='black',
            tickfont=dict(
                family='Arial',
                size=12,
                color='black'
            ),
            title='Systolic & Diastolic BP (mmHg)'
        ),
        autosize=False,
        margin=dict(
            autoexpand=False,
            l=100,
            r=20,
            t=110,
        ),
        plot_bgcolor='white'
        )
    st.plotly_chart(fig, use_container_width=True)
    return

def plot_rhr(df):
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df['Visit Date'],
        y=df['Resting Heart Rate (BPM)'],
        mode='lines+markers',
        line=dict(shape='linear', color='#FF3F3F'),
        marker=dict(size=14,
        line=dict(width=1.1)
        )))
        
    fig.update_layout(
        xaxis=dict(
            showline=True,
            showgrid=False,
            showticklabels=True,
            linewidth=3,
            ticks='outside',
            tickwidth=2,
            tickcolor='black',
            tickfont=dict(
                family='Arial',
                size=12,
                color='black',
            ),
            title='Visit Date'
        ),
        yaxis=dict(
            showgrid=True,
            linewidth=3,
            showline=True,
            showticklabels=True,
            ticks='outside',
            ticklen=4,
            tickwidth=2,
            tickcolor='black',
            tickfont=dict(
                family='Arial',
                size=12,
                color='black'
            ),
            title='Resting Heart Rate (BPM)'
        ),
        autosize=False,
        margin=dict(
            autoexpand=False,
            l=100,
            r=20,
            t=110,
        ),
        plot_bgcolor='white'
        )
    st.plotly_chart(fig, use_container_width=True)
    return

def plot_sit_reach(df):
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df['Visit Date'],
        y=df['Sit and Reach (cm)'],
        mode='lines+markers',
        name='Your Visit',
        line=dict(shape='linear', color='#FF3F3F'),
        marker=dict(size=14,
        line=dict(width=1.1)
        )))
        
    fig.update_layout(
        xaxis=dict(
            showline=True,
            showgrid=False,
            showticklabels=True,
            linewidth=3,
            ticks='outside',
            tickwidth=2,
            tickcolor='black',
            tickfont=dict(
                family='Arial',
                size=12,
                color='black',
            ),
            title='Visit Date'
        ),
        yaxis=dict(
            showgrid=True,
            linewidth=3,
            showline=True,
            showticklabels=True,
            ticks='outside',
            ticklen=4,
            tickwidth=2,
            tickcolor='black',
            tickfont=dict(
                family='Arial',
                size=12,
                color='black'
            ),
            title='Sit and Reach (cm)'
        ),
        autosize=False,
        margin=dict(
            autoexpand=False,
            l=100,
            r=20,
            t=110,
        ),
        plot_bgcolor='white'
        )
    st.plotly_chart(fig, use_container_width=True)
    return
