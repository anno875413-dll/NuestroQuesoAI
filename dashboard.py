import streamlit as st

from models.xgboost_forecast import (
    xgboost_forecast
)

from models.inventory_optimizer import (
    current_inventory
)

from models.production_planner import (
    production_needed
)

from models.spoilage_prediction import (
    find_high_risk_batches
)

from models.waste_reduction_engine import (
    waste_actions
)

from reports.sales_chart import (
    create_sales_chart
)

from reports.inventory_chart import (
    create_inventory_chart
)

from reports.savings_estimator import (
    estimated_savings
)

from reports.loss_estimator import (
    estimated_loss
)


# --------------------------------------------------
# PAGE SETTINGS
# --------------------------------------------------

st.set_page_config(
    page_title="Nuestro Queso AI Dashboard",
    layout="wide"
)
st.sidebar.title(
    "Nuestro Queso AI"
)

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Forecast",
        "Inventory",
        "Reports"
    ]
)
st.title("🧀 Nuestro Queso AI Dashboard")

st.markdown(
    """
Forecast demand, optimize production,
reduce spoilage, and improve profitability.
"""
)


# --------------------------------------------------
# DEMAND FORECASTS
# --------------------------------------------------

st.header("Demand Forecast")

queso_fresco_forecast = xgboost_forecast(
    "Queso Fresco"
)

queso_oaxaca_forecast = xgboost_forecast(
    "Queso Oaxaca"
)

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Queso Fresco 30-Day Demand",
        queso_fresco_forecast
    )

with col2:

    st.metric(
        "Queso Oaxaca 30-Day Demand",
        queso_oaxaca_forecast
    )


# --------------------------------------------------
# INVENTORY
# --------------------------------------------------

st.header("Current Inventory")

fresco_inventory = current_inventory(
    "Queso Fresco"
)

oaxaca_inventory = current_inventory(
    "Queso Oaxaca"
)

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Queso Fresco Inventory",
        fresco_inventory
    )

with col2:

    st.metric(
        "Queso Oaxaca Inventory",
        oaxaca_inventory
    )


# --------------------------------------------------
# PRODUCTION RECOMMENDATIONS
# --------------------------------------------------

st.header("Production Recommendations")

fresco_production = production_needed(
    "Queso Fresco"
)

oaxaca_production = production_needed(
    "Queso Oaxaca"
)

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Produce Queso Fresco",
        fresco_production
    )

with col2:

    st.metric(
        "Produce Queso Oaxaca",
        oaxaca_production
    )


# --------------------------------------------------
# HIGH RISK INVENTORY
# --------------------------------------------------

st.header("High Risk Batches")

high_risk = find_high_risk_batches()

if high_risk.empty:

    st.success(
        "No high-risk inventory found."
    )

else:

    st.dataframe(
        high_risk
    )


# --------------------------------------------------
# WASTE REDUCTION ACTIONS
# --------------------------------------------------

st.header("Waste Reduction Actions")

actions = waste_actions()

if len(actions) == 0:

    st.success(
        "No immediate actions required."
    )

else:

    for action in actions:

        st.warning(
            action
        )


# --------------------------------------------------
# FINANCIAL IMPACT
# --------------------------------------------------

st.header("Financial Impact")

potential_loss_avoided = estimated_savings(
    spoiled_units=500,
    cost_per_unit=4.50
)

inventory_value = estimated_loss()

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Potential Loss Avoided ($)",
        potential_loss_avoided
    )

with col2:

    st.metric(
        "Inventory Value ($)",
        inventory_value
    )


# --------------------------------------------------
# SALES CHART
# --------------------------------------------------

st.header("Historical Cheese Sales")

sales_chart = create_sales_chart()

st.plotly_chart(
    sales_chart,
    use_container_width=True
)


# --------------------------------------------------
# INVENTORY CHART
# --------------------------------------------------

st.header("Inventory Levels")

inventory_chart = create_inventory_chart()

st.plotly_chart(
    inventory_chart,
    use_container_width=True
)


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")

st.caption(
    "Nuestro Queso AI • Demand Forecasting • Inventory Optimization • Spoilage Prevention"
)
from models.ensemble_forecast import (
    ensemble_forecast
)

from models.profit_optimizer import (
    estimated_profit
)

from models.milk_purchase_optimizer import (
    milk_required
)

from models.production_scheduler import (
    weekly_schedule
)

from models.temperature_forecast import (
    temperature_risk
)

from reports.pdf_report_generator import (
    generate_pdf_data
)


# --------------------------------------------------
# ENSEMBLE FORECAST
# --------------------------------------------------

st.header(
    "Ensemble Forecast"
)

col1, col2 = st.columns(2)

with col1:

    st.metric(

        "Queso Fresco Forecast",

        ensemble_forecast(
            "Queso Fresco"
        )
    )

with col2:

    st.metric(

        "Queso Oaxaca Forecast",

        ensemble_forecast(
            "Queso Oaxaca"
        )
    )


 # --------------------------------------------------
# MILK REQUIREMENTS
# --------------------------------------------------

st.header(
    "Milk Requirements"
)

col1, col2 = st.columns(2)

with col1:

    st.metric(

        "Milk Needed for Queso Fresco (lbs)",

        milk_required(
            "Queso Fresco"
        )
    )

with col2:

    st.metric(

        "Milk Needed for Queso Oaxaca (lbs)",

        milk_required(
            "Queso Oaxaca"
        )
    )


    # --------------------------------------------------
# PROFIT ESTIMATOR
# --------------------------------------------------

st.header(
    "Estimated Profit"
)

profit = estimated_profit(

    revenue=100000,

    production_cost=55000,

    spoilage_loss=5000
)

st.metric(

    "Estimated Monthly Profit ($)",

    profit
)


# --------------------------------------------------
# WEEKLY PRODUCTION SCHEDULE
# --------------------------------------------------

st.header(
    "Weekly Production Schedule"
)

schedule = weekly_schedule()

st.table(
    schedule
)


# --------------------------------------------------
# STORAGE TEMPERATURE RISK
# --------------------------------------------------

st.header(
    "Storage Temperature Risk"
)

risk = temperature_risk(
    38
)

st.metric(

    "Current Risk",

    risk
)


# --------------------------------------------------
# DAILY REPORT
# --------------------------------------------------

st.header(
    "Daily Report"
)

st.write(

    generate_pdf_data()
)