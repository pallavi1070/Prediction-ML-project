import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

def shorten_categories(categories, cutoff):
    categorical_map = {}

    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = "Other"
    return categorical_map

def clean_experience(exp):
    if exp == "More than 50 years":
        return 50
    if exp == "Less than 1 year":
        return 0.5
    return float(exp)

def clean_education(edu):
    if 'Bachelor’s degree' in edu:
        return 'Bachelors degree'
    if 'Master’s degree' in edu:
        return 'Masters degree'
    if 'Professional degree' in edu or 'Other doctoral degree' in edu:
        return 'Post grad'
    return 'Less than a Bachelors'

@st.cache
def load_data():
    df = pd.read_csv("survey_results_public.csv")
    df = df[["Country", "EdLevel", "YearsCodePro", "Employment", "ConvertedComp"]]
    df = df.rename({"ConvertedComp": "Salary"}, axis=1)
    df = df[df["Salary"].notnull()]
    df = df.dropna()

    df = df[df["Employment"] == "Employed full-time"]
    df = df.drop("Employment", axis= 1)

    country_map = shorten_categories(df['Country'].value_counts(), 400)
    df['Country'] = df['Country'].map(country_map)

    df = df[df['Salary'] <= 250000]
    df = df[df['Salary'] >= 10000]
    df = df[df['Country']!= 'Other']

    df["YearsCodePro"] = df["YearsCodePro"].apply(clean_experience)
    df["EdLevel"] = df["EdLevel"].apply(clean_education)

    return df

df = load_data()

def show_explore_page():
    st.title("Explore Software Developer's Data")

    st.write("""
    ### Stack Overflow Survey
    """)
    data = df["Country"].value_counts().reset_index()
    data.column = ["Country","count"]

    #PIE CHART
    fig1 = px.pie(data, names ="Country" , values ="count",
                title = "Number of Data from different Countries",
                color_discrete_sequence=px.colors.sequential.RdBu,hole=0.3
                )

    fig1.update_traces(textinfo = 'percent+label')
    fig1.update_layout(template = 'plotly_dark')

    st.plotly_chart(fig1)

    #Scatter Plot

    df_sorted = df.sort_values(by="YearsCodePro")
    fig2 = px.scatter(df_sorted,x='YearsCodePro',y='Salary',color = "Country",
                    title='Years of Experience v/s Salary',
                    labels={'YearsCodePro':'Years of Experience','Salary':'Salary'},
                    animation_frame='YearsCodePro',hover_data=['EdLevel'])
    fig2.update_layout(template='plotly_dark')
    st.plotly_chart(fig2)

    #Box plot
    #salary distribution based on Edlevel

    fig3 = px.box(
        df,x='EdLevel',y='Salary',color='EdLevel',
        title="Salary Distribution by education level",
        labels={"EdLevel": "Education Level","Salary":"Salary"}
    )
    fig3.update_layout(template='plotly_dark')
    st.plotly_chart(fig3)