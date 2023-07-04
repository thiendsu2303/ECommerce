import streamlit as st
import pandas as pd
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px

# Config trang -----------------------------------------
st.set_page_config(
    page_title="Order Dashboard",
    page_icon="📊",
    layout="wide"
)

col1, col2, col3 = st.columns([1,6,1])
with col1:
    st.write("")
with col2:
    st.markdown("<h1 style='text-align: center; color: #B799FF;'>ORDER DASHBOARD</h1>", unsafe_allow_html=True)
with col3:
    st.write("")

path_to_excel_file = "Sample_Customore_Order raw.xlsx"
sheet_name = "raw"
df = pd.read_excel(path_to_excel_file, sheet_name=sheet_name)

st.markdown("##### Overview", unsafe_allow_html=True)
for value,count in df["order_status"].value_counts().items():
    if value == "COMPLETED":
        completed_count = count
    else:
        fail_count = count
col1, col2, col3, col4, col5  = st.columns(5)
col1.metric(
    label="Total Orders",
    value=df["order_id"].count(),
)
col2.metric(
    label="Total Quantitys",
    value=df["item_quantity"].sum(),
)
col3.metric(
    label="Completed Selling Price",
    value=df.loc[df["order_status"] == "COMPLETED", "selling_price"].sum(),
)
col4.metric(
    label="Orders Completed",
    value=completed_count,
    delta=f"{int((completed_count/(completed_count+fail_count)*100)+1)}%",
    delta_color='off'
)
col5.metric(
    label="Orders Cancelled",
    value=fail_count,
    delta=f"{int(fail_count/(completed_count+fail_count)*100)}%",
    delta_color='off'
)
st.info("""**Key findings**: 
- The number of canceled orders represents approximately 20% of the total number of orders placed in the month.
- The number of canceled orders is one-fourth (1/4) of the number of successful orders.

**Propose:**
- Enhancing the quantity of canceled orders has the potential to boost revenue by almost 25% in comparison to the previous month.
""", icon="📝")
new_payment_method = []
for value in df["payment_method"]:
    tmp = value
    value = value.split(' ')[0]
    if value == 'VN':
        tmp = 'VN Airpay Ibanking'
    else :
        pass
    new_payment_method.append(tmp)
df["new_payment_method"] = new_payment_method
new_payment_dict = df["new_payment_method"].value_counts().to_dict()
payment_list = []
for key, value in new_payment_dict.items():
    payment_list.append(key)
st.markdown("##### Filter by each payment method:", unsafe_allow_html=True)
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(payment_list)
with tab1:
    paycol1, paycol2, paycol3, paycol4, paycol5  = st.columns(5)
    paycol1.metric(
    label="Total Orders",
    value=df["new_payment_method"].eq("Cash on Delivery").sum(),
    )
    paycol2.metric(
        label="Total Quantitys",
        value=df.loc[df["new_payment_method"] == "Cash on Delivery", "item_quantity"].sum(),
    )
    paycol3.metric(
        label="Completed Selling Price",
        value=df.loc[(df["order_status"] == "COMPLETED") & (df["new_payment_method"] == "Cash on Delivery"), "selling_price"].sum(),
    )
    paycol4.metric(
        label="Orders Completed",
        value=df.loc[(df["new_payment_method"] == "Cash on Delivery") & (df["order_status"] == "COMPLETED")].shape[0],
    )
    paycol5.metric(
        label="Orders Cancelled",
        value=df.loc[(df["payment_method"] == "Cash on Delivery") & (df["order_status"] == "CANCELLED")].shape[0],
    )
with tab2:
    paycol1, paycol2, paycol3, paycol4, paycol5  = st.columns(5)
    paycol1.metric(
    label="Total Orders",
    value=df["new_payment_method"].eq("Airpay GIRO").sum(),
    )
    paycol2.metric(
        label="Total Quantitys",
        value=df.loc[df["new_payment_method"] == "Airpay GIRO", "item_quantity"].sum(),
    )
    paycol3.metric(
        label="Completed Selling Price",
        value=df.loc[(df["order_status"] == "COMPLETED") & (df["new_payment_method"] == "Airpay GIRO"), "selling_price"].sum(),
    )
    paycol4.metric(
        label="Orders Completed",
        value=df.loc[(df["new_payment_method"] == "Airpay GIRO") & (df["order_status"] == "COMPLETED")].shape[0],
    )
    paycol5.metric(
        label="Orders Cancelled",
        value=df.loc[(df["payment_method"] == "Airpay GIRO") & (df["order_status"] == "CANCELLED")].shape[0],
    )
with tab3:
    paycol1, paycol2, paycol3, paycol4, paycol5  = st.columns(5)
    paycol1.metric(
    label="Total Orders",
    value=df["new_payment_method"].eq("Cybersource").sum(),
    )
    paycol2.metric(
        label="Total Quantitys",
        value=df.loc[df["new_payment_method"] == "Cybersource", "item_quantity"].sum(),
    )
    paycol3.metric(
        label="Completed Selling Price",
        value=df.loc[(df["order_status"] == "COMPLETED") & (df["new_payment_method"] == "Cybersource"), "selling_price"].sum(),
    )
    paycol4.metric(
        label="Orders Completed",
        value=df.loc[(df["new_payment_method"] == "Cybersource") & (df["order_status"] == "COMPLETED")].shape[0],
    )
    paycol5.metric(
        label="Orders Cancelled",
        value=df.loc[(df["payment_method"] == "Cybersource") & (df["order_status"] == "CANCELLED")].shape[0],
    )
with tab4:
    paycol1, paycol2, paycol3, paycol4, paycol5  = st.columns(5)
    paycol1.metric(
    label="Total Orders",
    value=df["new_payment_method"].eq("Airpay Wallet V2").sum(),
    )
    paycol2.metric(
        label="Total Quantitys",
        value=df.loc[df["new_payment_method"] == "Airpay Wallet V2", "item_quantity"].sum(),
    )
    paycol3.metric(
        label="Completed Selling Price",
        value=df.loc[(df["order_status"] == "COMPLETED") & (df["new_payment_method"] == "Airpay Wallet V2"), "selling_price"].sum(),
    )
    paycol4.metric(
        label="Orders Completed",
        value=df.loc[(df["new_payment_method"] == "Airpay Wallet V2") & (df["order_status"] == "COMPLETED")].shape[0],
    )
    paycol5.metric(
        label="Orders Cancelled",
        value=df.loc[(df["payment_method"] == "Airpay Wallet V2") & (df["order_status"] == "CANCELLED")].shape[0],
    )
with tab5:
    paycol1, paycol2, paycol3, paycol4, paycol5  = st.columns(5)
    paycol1.metric(
    label="Total Orders",
    value=df["new_payment_method"].eq("VN Airpay Ibanking").sum(),
    )
    paycol2.metric(
        label="Total Quantitys",
        value=df.loc[df["new_payment_method"] == "VN Airpay Ibanking", "item_quantity"].sum(),
    )
    paycol3.metric(
        label="Completed Selling Price",
        value=df.loc[(df["order_status"] == "COMPLETED") & (df["new_payment_method"] == "VN Airpay Ibanking"), "selling_price"].sum(),
    )
    paycol4.metric(
        label="Orders Completed",
        value=df.loc[(df["new_payment_method"] == "VN Airpay Ibanking") & (df["order_status"] == "COMPLETED")].shape[0],
    )
    paycol5.metric(
        label="Orders Cancelled",
        value=df.loc[(df["payment_method"] == "VN Airpay Ibanking") & (df["order_status"] == "CANCELLED")].shape[0],
    )
with tab6:
    paycol1, paycol2, paycol3, paycol4, paycol5  = st.columns(5)
    paycol1.metric(
    label="Total Orders",
    value=df["new_payment_method"].eq("Shopee Wallet").sum(),
    )
    paycol2.metric(
        label="Total Quantitys",
        value=df.loc[df["new_payment_method"] == "Shopee Wallet", "item_quantity"].sum(),
    )
    paycol3.metric(
        label="Completed Selling Price",
        value=df.loc[(df["order_status"] == "COMPLETED") & (df["new_payment_method"] == "Shopee Wallet"), "selling_price"].sum(),
    )
    paycol4.metric(
        label="Orders Completed",
        value=df.loc[(df["new_payment_method"] == "Shopee Wallet") & (df["order_status"] == "COMPLETED")].shape[0],
    )
    paycol5.metric(
        label="Orders Cancelled",
        value=df.loc[(df["payment_method"] == "Shopee Wallet") & (df["order_status"] == "CANCELLED")].shape[0],
    )
with tab7:
    paycol1, paycol2, paycol3, paycol4, paycol5  = st.columns(5)
    paycol1.metric(
    label="Total Orders",
    value=df["new_payment_method"].eq("Cybersource (new)").sum(),
    )
    paycol2.metric(
        label="Total Quantitys",
        value=df.loc[df["new_payment_method"] == "Cybersource (new)", "item_quantity"].sum(),
    )
    paycol3.metric(
        label="Completed Selling Price",
        value=df.loc[(df["order_status"] == "COMPLETED") & (df["new_payment_method"] == "Cybersource (new)"), "selling_price"].sum(),
    )
    paycol4.metric(
        label="Orders Completed",
        value=df.loc[(df["new_payment_method"] == "Cybersource (new)") & (df["order_status"] == "COMPLETED")].shape[0],
    )
    paycol5.metric(
        label="Orders Cancelled",
        value=df.loc[(df["payment_method"] == "Cybersource (new)") & (df["order_status"] == "CANCELLED")].shape[0],
    )
st.markdown("##### The relationship between payment methods with :red[COMPLETED] order status:", unsafe_allow_html=True)
pie_pay_me_col1, pie_pay_me_col2, pie_pay_me_col3 = st.columns([3,3,3])
with pie_pay_me_col1:
    st.markdown("### Orders")
    df_completed = df[df["order_status"] == "COMPLETED"]
    thong_ke = df_completed['new_payment_method'].value_counts()
    fig = go.Figure(data=go.Pie(labels=thong_ke.index, values=thong_ke))
    fig.update_layout(
        title="Orders COMPLETED",
        showlegend=True,
        legend_title="Payment method"
    )
    st.plotly_chart(fig,use_container_width=True,height=800)
with pie_pay_me_col2:
    st.markdown("## Quantity")
    df_completed = df[df["order_status"] == "COMPLETED"]
    thong_ke = df_completed.groupby('new_payment_method')['item_quantity'].sum()
    fig = go.Figure(data=go.Pie(labels=thong_ke.index, values=thong_ke))
    fig.update_layout(
        title="Quantity COMPLETED",
        showlegend=True,
        legend_title="Payment method"
    )
    st.plotly_chart(fig,use_container_width=True,height=800)
with pie_pay_me_col3:
    st.markdown("## Selling Price")
    df_completed = df[df["order_status"] == "COMPLETED"]
    thong_ke = df_completed.groupby('new_payment_method')['selling_price'].sum()
    fig = go.Figure(data=go.Pie(labels=thong_ke.index, values=thong_ke))
    fig.update_layout(
        title="Selling Price COMPLETED",
        showlegend=True,
        legend_title="Payment method"
    )
    st.plotly_chart(fig,use_container_width=True,height=800)

st.markdown("##### The relationship between payment methods with :red[CANCELLED] order status:", unsafe_allow_html=True)
pie_pay_me_1_col1, pie_pay_me_1_col2, pie_pay_me_1_col3 = st.columns([3,3,3])
with pie_pay_me_1_col1:
    st.markdown("### Orders")
    df_completed = df[df["order_status"] == "CANCELLED"]
    thong_ke = df_completed['new_payment_method'].value_counts()
    fig = go.Figure(data=go.Pie(labels=thong_ke.index, values=thong_ke))
    fig.update_layout(
        title="Orders CANCELLED",
        showlegend=True,
        legend_title="Payment method"
    )
    st.plotly_chart(fig,use_container_width=True,height=800)
with pie_pay_me_1_col2:
    st.markdown("## Quantity")
    df_completed = df[df["order_status"] == "CANCELLED"]
    thong_ke = df_completed.groupby('new_payment_method')['item_quantity'].sum()
    fig = go.Figure(data=go.Pie(labels=thong_ke.index, values=thong_ke))
    fig.update_layout(
        title="Quantity CANCELLED",
        showlegend=True,
        legend_title="Payment method"
    )
    st.plotly_chart(fig,use_container_width=True,height=800)
with pie_pay_me_1_col3:
    st.markdown("## Selling Price")
    df_completed = df[df["order_status"] == "CANCELLED"]
    thong_ke = df_completed.groupby('new_payment_method')['selling_price'].sum()
    fig = go.Figure(data=go.Pie(labels=thong_ke.index, values=thong_ke))
    fig.update_layout(
        title="Selling Price CANCELLED",
        showlegend=True,
        legend_title="Payment method"
    )
    st.plotly_chart(fig,use_container_width=True,height=800)
st.markdown("##### Correlation between number of :red[COMPLETED] and :red[CANCELLED] of each payment method", unsafe_allow_html=True)
new_payment_method_status = pd.pivot_table(df, index="new_payment_method", columns="order_status", aggfunc="size", fill_value=0)
payment_methods = new_payment_method_status.index.tolist()
colors = ["blue", "red"]
traces = []
for i, order_status in enumerate(new_payment_method_status.columns):
    counts = new_payment_method_status[order_status].values
    trace = go.Bar(
        x=payment_methods,
        y=counts,
        name=order_status,
        marker=dict(color=colors[i])
    )
    traces.append(trace)
fig = go.Figure(data=traces)
fig.update_layout(
    title="Payment Method Status",
    xaxis_title="Payment Method",
    yaxis_title="Count",
    barmode='stack',
    legend_title="Order Status"
)
st.plotly_chart(fig,use_container_width=True,height=800)
st.info("""**Key findings**: 
- The number of orders, the quantity of products sold, and the revenue generated from payment methods are directly related to each other. There is no occurrence of a situation where there are low sales in terms of orders but high revenue.
- Cash on Delivery represents approximately 90% of the overall orders, encompassing the quantity of products sold and the selling price collected in both COMPLETED and CANCELLED order statuses.

**Propose:**
- By utilizing the Cash on Delivery payment method, we have the opportunity to enhance the quantity of canceled orders. This improvement in order numbers contributes to achieving a high conversion rate, particularly when transitioning from CANCELLED units to COMPLETED units.
- Improve the quality of transportation such as: faster delivery, synchronization of the delivery process, ... so that the time for customers to change their decision to buy or not is reduced.
- Vouchers can be increased on the most popular payment methods by users such as: VN Airpay Ibanking and Airpay GIRO to reduce the number of CANCELLED devices.
""", icon="📝")
st.markdown("##### Allocate :red[discount] percentage for each order status", unsafe_allow_html=True)
dis_list = []
for value1, value2 in zip(df["onsite_original_price"],df["selling_price"]):
    dis = value1 - value2
    dis_list.append(int((dis/value1)*100))
df["dis"] = dis_list
completed_orders = df[df["order_status"] == "COMPLETED"]
canceled_orders = df[df["order_status"] == "CANCELLED"]
bar_dis_col1, bar_dis_col2 = st.columns([5,5])
with bar_dis_col1:
    fig = go.Figure(data=[go.Histogram(x=completed_orders["dis"], nbinsx=50)])
    fig.update_layout(title_text="Completed Orders - Percentage of Discount",
                    xaxis_title="Dis Percentage",
                    yaxis_title="Count")
    st.plotly_chart(fig,use_container_width=True,height=800)
with bar_dis_col2:
    fig = go.Figure(data=[go.Histogram(x=canceled_orders["dis"], nbinsx=50)])
    fig.update_layout(title_text="Cancelled Orders - Percentage of Discount",
                    xaxis_title="Dis Percentage",
                    yaxis_title="Count")
    st.plotly_chart(fig,use_container_width=True,height=800)
st.info("""**Comments**: 
- Discount percentage distribution of COMPLETED and CANCELLED orders is almost the same.
""", icon="📝")

st.markdown("##### Allocate :red[the number of orders], :red[total number of products sold] and :red[revenue] by :red[day] of the month", unsafe_allow_html=True)
date_list = []
for value in df["created_day"]:
    date_list.append(value.day)
df["date"] = date_list
date_tab1, date_tab2, date_tab3 = st.tabs(["Orders", "Quantity", "Selling Price"])
with date_tab1:
    df_daily_orders = df.groupby(['date', 'order_status']).size().reset_index(name='count')
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_daily_orders[df_daily_orders['order_status'] == 'COMPLETED']['date'],
                            y=df_daily_orders[df_daily_orders['order_status'] == 'COMPLETED']['count'],
                            mode='lines+markers',
                            name='Completed',
                            line=dict(color='red'),
                            marker=dict(color='red', size=8)
                            ))
    fig.add_trace(go.Scatter(x=df_daily_orders[df_daily_orders['order_status'] == 'CANCELLED']['date'],
                            y=df_daily_orders[df_daily_orders['order_status'] == 'CANCELLED']['count'],
                            mode='lines+markers',
                            name='Cancelled',
                            line=dict(color='blue'),
                            marker=dict(color='blue', size=8)
                            ))
    fig.update_layout(title_text='Daily Order Count',
                    xaxis=dict(title='Date', type='category'),
                    yaxis=dict(title='Order Count'))
    st.plotly_chart(fig,use_container_width=True,height=800)
with date_tab2:
    df_daily_quantity = df.groupby(['date', 'order_status'])['item_quantity'].sum().reset_index(name='total_quantity')
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_daily_quantity[df_daily_quantity['order_status'] == 'COMPLETED']['date'],
                            y=df_daily_quantity[df_daily_quantity['order_status'] == 'COMPLETED']['total_quantity'],
                            mode='lines+markers',
                            name='Completed',
                            line=dict(color='red'),
                            marker=dict(color='red', size=8)
                            ))
    fig.add_trace(go.Scatter(x=df_daily_quantity[df_daily_quantity['order_status'] == 'CANCELLED']['date'],
                            y=df_daily_quantity[df_daily_quantity['order_status'] == 'CANCELLED']['total_quantity'],
                            mode='lines+markers',
                            name='Cancelled',
                            line=dict(color='blue'),
                            marker=dict(color='blue', size=8)
                            ))
    fig.update_layout(title_text='Daily Quantity Sold',
                    xaxis=dict(title='Date', type='category'),
                    yaxis=dict(title='Quantity Sold'))
    st.plotly_chart(fig,use_container_width=True,height=800)
with date_tab3:
    df_daily_price = df.groupby(['date', 'order_status'])['selling_price'].sum().reset_index(name='total_price')
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_daily_price[df_daily_price['order_status'] == 'COMPLETED']['date'],
                            y=df_daily_price[df_daily_price['order_status'] == 'COMPLETED']['total_price'],
                            mode='lines+markers',
                            name='Completed',
                            line=dict(color='red'),
                            marker=dict(color='red', size=8)
                            ))
    fig.add_trace(go.Scatter(x=df_daily_price[df_daily_price['order_status'] == 'CANCELLED']['date'],
                            y=df_daily_price[df_daily_price['order_status'] == 'CANCELLED']['total_price'],
                            mode='lines+markers',
                            name='Cancelled',
                            line=dict(color='blue'),
                            marker=dict(color='blue', size=8)
                            ))
    fig.update_layout(title_text='Daily Selling Price',
                    xaxis=dict(title='Date', type='category'),
                    yaxis=dict(title='Selling Price'))
    st.plotly_chart(fig,use_container_width=True,height=800)
st.info("""**Key findings**: 
- Sales in period 10 - 12 is higher, especially in 12th, the selling price of orders peak nearly 2.5B, 6 times than the previous day and 5 times than average.
- One week in a row from the 18th to the 25th, the sales are all lower than 200M.

**Propose:**
- To boost sales, it is proposed to run a one-week promotional campaign starting from the 18th and ending on the 25th, with the objective of achieving a sales target in the range of 700 million to 800 million.
""", icon="📝")
st.markdown("##### Universal :red[shipping fee] for each single status", unsafe_allow_html=True)
ship_col1, ship_col2 = st.columns([5,5])
with ship_col1:
    fig = go.Figure(data=[go.Histogram(x=completed_orders["shipping_fee"], nbinsx=100)])
    fig.update_layout(title_text="Completed Orders - Shipping Fee Histogram",
                    xaxis=dict(title="Shipping Fee"),
                    yaxis=dict(title="Count"))
    st.plotly_chart(fig,use_container_width=True,height=800)
with ship_col2:
    fig = go.Figure(data=[go.Histogram(x=canceled_orders["shipping_fee"], nbinsx=100)])
    fig.update_layout(title_text="Cancelled Orders - Shipping Fee Histogram",
                    xaxis=dict(title="Shipping Fee"),
                    yaxis=dict(title="Count"))
    st.plotly_chart(fig,use_container_width=True,height=800)
st.info("""**Key findings**: 
- The shipping fee allocation of canceled orders vs completed orders are similar.
- The highest price of COMPLETED orders is less than 200k but for CANCELLED orders, there are more orders appearing over 200k and the highest price is close to 400k.
- Above 100k there are more CANCELLED singles.

**Propose:**
- Lower shipping fees to help reduce CACELLED orders.
""", icon="📝")