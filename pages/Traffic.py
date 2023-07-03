import streamlit as st
import pandas as pd
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px

# Config trang -----------------------------------------
st.set_page_config(
    page_title="Traffic Dashboard",
    page_icon="📊",
    layout="wide"
)

col1, col2, col3 = st.columns([1,6,1])
with col1:
    st.write("")
with col2:
    st.markdown("<h1 style='text-align: center; color: #B799FF;'>TRAFFIC DASHBOARD</h1>", unsafe_allow_html=True)
with col3:
    st.write("")

path_to_excel_file = "Sample_Customore_Traffic raw.xlsx"
df = pd.read_excel(path_to_excel_file)

st.markdown("##### Overview", unsafe_allow_html=True)
col1, col2, col3, col4, col5  = st.columns(5)
col1.metric(
    label="Total Users",
    value=df['Users'].iloc[-1],
)
col2.metric(
    label="Total New Users",
    value=df['New Users'].iloc[-1],
)
col3.metric(
    label="Total Sessions",
    value=df['Sessions'].iloc[-1],
)
col4.metric(
    label="Avg. Bounce Rate",
    value=df['Bounce Rate'].iloc[-1],
)
col5.metric(
    label="Avg. Pages/Session",
    value=df['Pages / Session'].iloc[-1],
)

col6, col7, col8, col9 = st.columns(4)
col6.metric(
    label="Avg. Session Duration",
    value=df['Avg. Session Duration'].iloc[-1],
)
col7.metric(
    label="Avg. Ecommerce Conversion Rate",
    value=df['Ecommerce Conversion Rate'].iloc[-1],
)
col8.metric(
    label="Total Transactions",
    value=df['Transactions'].iloc[-1],
)
col9.metric(
    label="Total Revenue",
    value=df['Revenue'].iloc[-1],
)
df = df.drop(df.index[-1])
new_source = []
new_medium = []
for value in df["Source / Medium"]:
    if str(value) == 'nan':
        pass
    else:
        value = str(value)
        value = value.split("/")
        new_source.append(value[0].strip())
        new_medium.append(value[1].strip())
df["new_source"] = new_source
df["new_medium"] = new_medium
col_list = ["Users" , "New Users", "Sessions", "Transactions", "Revenue"]
tab1, tab2, tab3, tab4, tab5 = st.tabs(col_list)
with tab1:
    user_col1, user_col2 = st.columns([5,5])
    with user_col1:
        medium_users = df.groupby('new_medium')['Users'].sum()
        fig = go.Figure(data=go.Bar(x=medium_users.index, y=medium_users))
        fig.update_layout(
            title="Partitions Users by Medium",
            xaxis_title="new_medium",
            yaxis_title="Users",
        )
        st.plotly_chart(fig,use_container_width=True,height=800)
    with user_col2:
        medium_users = df.groupby('new_medium')['Users'].sum()
        fig = go.Figure(data=go.Pie(labels=medium_users.index, values=medium_users))
        fig.update_layout(
            title="Partitions Users by Medium",
            showlegend=True,
        )
        st.plotly_chart(fig,use_container_width=True,height=800)
with tab2:
    new_user_col1, new_user_col2 = st.columns([5,5])
    with new_user_col1:
        medium_users = df.groupby('new_medium')['New Users'].sum()
        fig = go.Figure(data=go.Bar(x=medium_users.index, y=medium_users))
        fig.update_layout(
            title="Partitions New Users by Medium",
            xaxis_title="new_medium",
            yaxis_title="New Users",
        )
        st.plotly_chart(fig,use_container_width=True,height=800)
    with new_user_col2:
        medium_users = df.groupby('new_medium')['New Users'].sum()
        fig = go.Figure(data=go.Pie(labels=medium_users.index, values=medium_users))
        fig.update_layout(
            title="Partitions New Users by Medium",
            showlegend=True,
        )
        st.plotly_chart(fig,use_container_width=True,height=800)
with tab3:
    session_col1, session_col2 = st.columns([5,5])
    with session_col1:
        medium_users = df.groupby('new_medium')['Sessions'].sum()
        fig = go.Figure(data=go.Bar(x=medium_users.index, y=medium_users))
        fig.update_layout(
            title="Partitions Sessions by Medium",
            xaxis_title="new_medium",
            yaxis_title="Sessions",
        )
        st.plotly_chart(fig,use_container_width=True,height=800)
    with session_col2:
        medium_users = df.groupby('new_medium')['Sessions'].sum()
        fig = go.Figure(data=go.Pie(labels=medium_users.index, values=medium_users))
        fig.update_layout(
            title="Partitions Sessions by Medium",
            showlegend=True,
        )
        st.plotly_chart(fig,use_container_width=True,height=800)
with tab4:
    trans_col1, trans_col2 = st.columns([5,5])
    with trans_col1:
        medium_users = df.groupby('new_medium')['Transactions'].sum()
        fig = go.Figure(data=go.Bar(x=medium_users.index, y=medium_users))
        fig.update_layout(
            title="Partitions Transactions by Medium",
            xaxis_title="new_medium",
            yaxis_title="Transactions",
        )
        st.plotly_chart(fig,use_container_width=True,height=800)
    with trans_col2:
        medium_users = df.groupby('new_medium')['Transactions'].sum()
        fig = go.Figure(data=go.Pie(labels=medium_users.index, values=medium_users))
        fig.update_layout(
            title="Partitions Transactions by Medium",
            showlegend=True,
        )
        st.plotly_chart(fig,use_container_width=True,height=800)
with tab5:
    reve_col1, reve_col2 = st.columns([5,5])
    with reve_col1:
        medium_users = df.groupby('new_medium')['Revenue'].sum()
        fig = go.Figure(data=go.Bar(x=medium_users.index, y=medium_users))
        fig.update_layout(
            title="Partitions Revenue by Medium",
            xaxis_title="new_medium",
            yaxis_title="Revenue",
        )
        st.plotly_chart(fig,use_container_width=True,height=800)
    with reve_col2:
        medium_users = df.groupby('new_medium')['Revenue'].sum()
        fig = go.Figure(data=go.Pie(labels=medium_users.index, values=medium_users))
        fig.update_layout(
            title="Partitions Revenue by Medium",
            showlegend=True,
        )
        st.plotly_chart(fig,use_container_width=True,height=800)
st.info("""**Key findings**: 
- Transactions =  New users * Conversion rate
⇒ To improve the quantity of transactions, we have to improve 2 metrics: Number of new users & Conversion rate.
- There are slightly different between the medium allocation in the number of transactions and new users.

**Propose:**
- Improving new users of medium accounts for most of the revenue. 
""", icon="📝")