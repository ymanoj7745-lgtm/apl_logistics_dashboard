import streamlit as st
import pandas as pd
import plotly.express as px

# ⚠️ Must be first Streamlit command
st.set_page_config(
    page_title="APL Logistics Risk Dashboard",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- Global CSS for Corporate Styling ----------
st.markdown("""
<style>
/* Bold corporate heading style */
h1, h2, h3, h4 {
    font-family: Arial Black, sans-serif;
    font-weight: 800 !important;
    color: #1E3A8A !important;
}

/* Bold metric values */
.stMetricValue {
    font-size: 28px !important;
    font-weight: 700 !important;
    color: #1E3A8A !important;
}

/* Sidebar filter header */
[data-testid="stSidebar"] h2 {
    font-family: Arial Black, sans-serif;
    font-size: 18px;
    color: #0C2340;
}

/* Highlight data table headers */
table thead th {
    background: #1E3A8A !important;
    color: white !important;
}

/* Links */
a {
    color: #1E3A8A !important;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.title("📦 APL Logistics Risk Dashboard")
st.markdown("Interactive and stylish corporate dashboard for delivery delay risk.")

# ---------- Load Data ----------
df = pd.read_csv("APL_Logistics_orders_with_risk.csv")
df.columns = df.columns.str.strip()
df['Order_ID'] = df.index.astype(str)

# ---------- Sidebar Filters ----------
st.sidebar.header("Filters")

regions = ["All"] + sorted(df['Order Region'].dropna().unique().tolist())
region_filter = st.sidebar.selectbox("Select Region", regions)

shipping_expr = ["All"] + sorted(df['Shipping_Mode_Express'].dropna().unique().tolist())
shipping_filter = st.sidebar.selectbox(
    "Shipping Express Mode",
    shipping_expr,
    format_func=lambda x: "All" if x == "All" else ("Express" if x == 1 else "Standard")
)

risk_cats = ["All"] + sorted(df['Risk_Category'].dropna().unique().tolist())
risk_filter = st.sidebar.selectbox("Select Risk Category", risk_cats)

filtered = df.copy()
if region_filter != "All":
    filtered = filtered[filtered['Order Region'] == region_filter]
if shipping_filter != "All":
    filtered = filtered[filtered['Shipping_Mode_Express'] == shipping_filter]
if risk_filter != "All":
    filtered = filtered[filtered['Risk_Category'] == risk_filter]

# ---------- Delay Risk Overview ----------
with st.expander("📊 Delay Risk Overview"):
    st.subheader("Risk Category Distribution")
    dist = filtered['Risk_Category'].value_counts().reset_index()
    dist.columns = ['Risk_Category','Count']
    fig = px.pie(
        dist, names='Risk_Category', values='Count',
        color='Risk_Category',
        color_discrete_map={"High Risk":"#E74C3C","Medium Risk":"#F1C40F","Low Risk":"#27AE60"},
        title="Overall Risk Distribution"
    )
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("### Key KPIs")
    total = len(filtered)
    high_risk = filtered['Risk_Category'].value_counts().get("High Risk", 0)
    avg_prob = filtered['Late_Delivery_Prob'].mean() if total else 0
    k1, k2, k3 = st.columns(3)
    k1.metric("Total Orders", total)
    k2.metric("High Risk Orders", high_risk)
    k3.metric("Avg Late Delivery Prob", f"{avg_prob:.2%}")

# ---------- Order-Level Risk ----------
with st.expander("📝 Order-Level Risk Prediction"):
    st.subheader("Order-Level Risk Details")
    order_id = st.selectbox("Choose Order ID", options=filtered['Order_ID'].tolist())
    order = filtered[filtered['Order_ID'] == order_id].iloc[0]
    st.markdown(f"**Late Delivery Probability:** {order['Late_Delivery_Prob']:.2%}")
    st.markdown(f"**Risk Category:** {order['Risk_Category']}")
    st.markdown("### Key Contributing Features (Proxies)")
    st.write(pd.DataFrame({
        "Feature": [
            "Shipping Pressure Index",
            "Regional Congestion Index",
            "Order Complexity Score",
            "Days for Shipping (real)"],
        "Value": [
            order['Shipping_Pressure_Index'],
            order['Regional_Congestion_Index'],
            order['Order_Complexity_Score'],
            order['Days for shipping (real)']
        ]
    }))

# ---------- Region & Shipping Risk Analysis ----------
with st.expander("🌍 Region & Shipping Analysis"):
    st.subheader("Avg Late Delivery Prob by Region")
    region_risk = filtered.groupby('Order Region')['Late_Delivery_Prob'].mean().reset_index()
    fig_r = px.bar(
        region_risk, x='Order Region', y='Late_Delivery_Prob',
        title="Avg Late Delivery Probability by Region", text_auto=True
    )
    st.plotly_chart(fig_r, use_container_width=True)
    st.subheader("Risk by Shipping Mode Express")
    mode_risk = filtered.groupby('Shipping_Mode_Express')['Late_Delivery_Prob'].mean().reset_index()
    mode_risk['Shipping Mode'] = mode_risk['Shipping_Mode_Express'].apply(lambda x: "Express" if x==1 else "Standard")
    fig_m = px.bar(
        mode_risk, x='Shipping Mode', y='Late_Delivery_Prob',
        title="Avg Late Delivery Probability by Shipping Type", text_auto=True
    )
    st.plotly_chart(fig_m, use_container_width=True)

# ---------- Operations Action Panel ----------
with st.expander("⚡ Operations Action Panel"):
    st.subheader("High-Risk Orders Needing Attention")
    hr_orders = filtered[filtered['Risk_Category']=="High Risk"]
    st.dataframe(hr_orders.sort_values('Late_Delivery_Prob', ascending=False).reset_index(drop=True))