{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4c272de9-f574-49d7-891d-524273ae5ce8",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2026-02-21 21:05:58.903 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run D:\\New folder\\envs\\booksenv\\lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator(_root_container=0, _provided_cursor=None, _parent=None, _block_type=None, _form_data=None)"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# apl_logistics_dashboard.py\n",
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "# Load the dashboard-ready data\n",
    "df = pd.read_csv(\"APL_Logistics_orders_with_risk.csv\")\n",
    "\n",
    "# Page setup\n",
    "st.set_page_config(page_title=\"APL Logistics Risk Dashboard\", layout=\"wide\")\n",
    "st.title(\"📦 APL Logistics — Predictive Delivery Risk Dashboard\")\n",
    "st.markdown(\"Shows high-risk orders, predicted delay probabilities, and top risk drivers.\")\n",
    "\n",
    "# KPI cards\n",
    "total_orders = len(df)\n",
    "high_risk_orders = (df['Risk_Category'] == \"High Risk\").sum()\n",
    "high_risk_rate = round((high_risk_orders / total_orders) * 100, 2)\n",
    "avg_delay_prob = round(df['Late_Delivery_Prob'].mean(), 3)\n",
    "\n",
    "col1, col2, col3, col4 = st.columns(4)\n",
    "col1.metric(\"Total Orders\", total_orders)\n",
    "col2.metric(\"High-Risk Orders\", high_risk_orders)\n",
    "col3.metric(\"High-Risk Rate (%)\", high_risk_rate)\n",
    "col4.metric(\"Avg Delay Probability\", avg_delay_prob)\n",
    "\n",
    "# Risk Category Distribution\n",
    "st.subheader(\"Risk Category Distribution\")\n",
    "risk_counts = df['Risk_Category'].value_counts()\n",
    "fig, ax = plt.subplots()\n",
    "sns.barplot(x=risk_counts.index, y=risk_counts.values, palette=[\"green\",\"yellow\",\"red\"], ax=ax)\n",
    "ax.set_ylabel(\"Number of Orders\")\n",
    "st.pyplot(fig)\n",
    "\n",
    "# High-Risk Orders Table\n",
    "st.subheader(\"⚠ High-Risk Orders\")\n",
    "high_risk_df = df[df['Risk_Category'] == \"High Risk\"]\n",
    "st.dataframe(high_risk_df.sort_values(by='Late_Delivery_Prob', ascending=False))\n",
    "\n",
    "# Risk by Region\n",
    "st.subheader(\"🌍 Average Late Delivery Probability by Region\")\n",
    "region_risk = df.groupby('Order Region')['Late_Delivery_Prob'].mean().sort_values(ascending=False)\n",
    "st.bar_chart(region_risk)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e12c146f-8e81-43e1-aa35-98228aacef00",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
