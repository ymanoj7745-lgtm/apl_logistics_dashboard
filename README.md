# 📦 APL Logistics Risk Dashboard

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Logistics](https://img.shields.io/badge/Domain-Logistics-0078D4?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

**An interactive delivery delay risk dashboard — predicting late delivery risk, categorizing orders by risk level, and providing actionable logistics insights in real time.**

</div>

---

## 📋 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Risk Categories](#-risk-categories)
- [Project Structure](#-project-structure)
- [How It Works](#-how-it-works)
- [Getting Started](#-getting-started)
- [Running the Dashboard](#-running-the-dashboard)
- [Screenshots](#-screenshots)

---

## 🔍 Overview

Late deliveries cost logistics companies millions every year. This dashboard uses a machine learning model to give operations teams **early visibility** into at-risk orders — before delays happen.

Built for logistics managers and operations teams who need to:
- Spot high-risk shipments before they become complaints
- Understand which regions and shipping modes drive delays
- Prioritize interventions on critical orders in real time

---

## 🧰 Features

| Feature | Description |
|---------|-------------|
| 🎯 **Risk Scoring** | ML-powered late delivery probability per order |
| 🚨 **Risk Categorization** | Automatic Low / Medium / High risk classification |
| 📊 **Risk Distribution** | Visual breakdown of order risk across the fleet |
| 🗺️ **Region Analysis** | Risk heatmap by geography |
| 🚢 **Shipping Mode Analysis** | Risk comparison across delivery methods |
| ⚡ **High-Risk Action Panel** | Focused view of orders needing immediate attention |
| 🎨 **Corporate UI** | Clean, interactive controls built for operations use |

---

## 🚨 Risk Categories

```
Risk Score 0% ──────────────────────────────────── 100%
               │                  │                  │
            🟢 LOW            🟡 MEDIUM           🔴 HIGH
           (< 33%)           (33% – 66%)          (> 66%)
        Monitor normally    Review & plan       Immediate action
```

---

## 📁 Project Structure

```
apl_logistics_dashboard/
│
├── 📄 app.py                      # Streamlit dashboard — main entry point
├── 📄 train_model.py              # Model training script (if applicable)
│
├── models/
│   └── risk_model.pkl             # Trained late delivery risk model
│
├── data/
│   └── logistics_data.csv         # ⚠️ Local only — not committed (size)
│
├── screenshots/
│   ├── overview.png               # Dashboard overview screenshot
│   └── order_details.png          # Order detail view screenshot
│
├── requirements.txt               # Python dependencies
└── README.md
```

---

## ⚙️ How It Works

```
Logistics Orders Data
        │
        ▼
┌─────────────────────────────┐
│  Feature Engineering        │  Order value, region, shipping mode,
│                             │  delivery window, distance, etc.
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  ML Risk Model              │  Predicts late delivery probability
│  (scikit-learn pipeline)    │  per order (0% – 100%)
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Risk Categorization        │  Low / Medium / High
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────────────────────────────┐
│  Streamlit Dashboard                                │
│  ┌───────────────┐  ┌────────────┐  ┌───────────┐  │
│  │ Risk Overview │  │  Region    │  │ High-Risk │  │
│  │ Distribution  │  │  Analysis  │  │  Actions  │  │
│  └───────────────┘  └────────────┘  └───────────┘  │
└─────────────────────────────────────────────────────┘
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Logistics dataset (CSV) placed in the `data/` folder

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/ymanoj7745-lgtm/apl_logistics_dashboard.git
cd apl_logistics_dashboard

# 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt
```

---

## 🖥️ Running the Dashboard

```bash
streamlit run app.py
```

Open the URL shown in your terminal. The dashboard provides:

- 📊 **Risk Distribution** — fleet-wide view of Low / Medium / High risk orders
- 🗺️ **Region & Shipping Mode Charts** — identify which segments drive delays
- ⚡ **High-Risk Order Panel** — actionable list of orders needing immediate attention
- 🔍 **Individual Order Scoring** — enter order details and get an instant risk score

---

## 🖼️ Screenshots

**Dashboard Overview**
![Dashboard Overview](./screenshots/overview.png)

**Order Detail & Risk Score**
![Order Details](./screenshots/order_details.png)

---

## 🛠️ Tech Stack

| Library | Purpose |
|---------|---------|
| `streamlit` | Interactive web dashboard |
| `scikit-learn` | ML model training & inference |
| `pandas` | Data manipulation |
| `numpy` | Numerical computing |
| `matplotlib` / `seaborn` / `plotly` | Visualizations |
| `joblib` | Model serialization |

---

## 📄 License

This project is licensed under the MIT License.

---

<div align="center">
Spot the risk. Ship with confidence. 🚚
</div>
