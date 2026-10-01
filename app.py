import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import time

from utils.prediction import predict_materials


# --------------------------------------
# PAGE CONFIG
# --------------------------------------

st.set_page_config(
    page_title="Construction AI SYSTEM",
    layout="wide"
)

# --------------------------------------
# PREMIUM GLASSMORPHISM + CORPORATE CSS
# --------------------------------------

st.markdown("""
<style>

/* Background Gradient */
.stApp{
background: linear-gradient(
135deg,#0f2027,#203a43,#2c5364);
color:white;
}

/* Glass Cards */

.glass{
background: rgba(255,255,255,0.1);
backdrop-filter: blur(10px);
padding:20px;
border-radius:15px;
box-shadow:0 8px 32px rgba(0,0,0,0.3);
margin-bottom:15px;
}

/* Sidebar */

section[data-testid="stSidebar"]{
background:rgba(0,0,0,0.6);
}

/* Button */

.stButton>button{

background:linear-gradient(
45deg,#ff512f,#dd2476);

color:white;

border-radius:12px;

height:3em;

font-weight:bold;

font-size:16px;

width:100%;
}

/* Metric Cards */

.metric-card{

background:rgba(255,255,255,0.15);

padding:15px;

border-radius:15px;

text-align:center;

box-shadow:0 6px 20px rgba(0,0,0,0.4);

}

</style>
""",unsafe_allow_html=True)


# --------------------------------------
# SIDEBAR
# --------------------------------------

st.sidebar.title("🏗 Construction AI PLATFORM")

menu = st.sidebar.radio(

"Navigation",

["Prediction Dashboard",
"Data Overview",
"About"]

)

# Prediction History

if "history" not in st.session_state:

    st.session_state.history=[]


# --------------------------------------
# ANIMATED COUNTER FUNCTION
# --------------------------------------

def animated_metric(label,value):

    placeholder = st.empty()

    for i in range(0,int(value)+1,
                   max(1,int(value/20)+1)):

        placeholder.metric(label,i)

        time.sleep(0.02)

    placeholder.metric(label,round(value,2))


# --------------------------------------
# DASHBOARD
# --------------------------------------

if menu=="Prediction Dashboard":

    st.markdown(
    "<h1 style='text-align:center;'>🏗 Construction Material Forecast AI</h1>",
    unsafe_allow_html=True
    )

    col1,col2=st.columns(2)

    with col1:

        area=st.number_input(
        "📐 Area sqft",1000,40000,3000)

        floors=st.number_input(
        "🏢 Floors",1,50,3)

    with col2:

        duration=st.number_input(
        "📅 Duration",30,1000,120)

        workers=st.number_input(
        "👷 Workers",10,500,80)

    if st.button("🚀 Predict Materials"):

        result=predict_materials(
        area,floors,duration,workers)

        st.session_state.history.append(result)

        st.success("Prediction Generated Successfully 🎉")

        # -------------------------
        # Animated Metrics
        # -------------------------

        m1,m2,m3,m4=st.columns(4)

        with m1:
            animated_metric(
            "🧱 Cement",
            result["Cement_bags"])

        with m2:
            animated_metric(
            "🔩 Steel",
            result["Steel_tons"])

        with m3:
            animated_metric(
            "🧱 Bricks",
            result["Bricks_units"])

        with m4:
            animated_metric(
            "🛣 Asphalt",
            result["Asphalt_tons"])

        # -------------------------
        # Risk Indicator
        # -------------------------

        if duration>450 or workers<40:

            risk="🔴 HIGH RISK"

            color="red"

        elif 300<=duration<=450:

            risk="🟠 MEDIUM RISK"

            color="orange"

        else:

            risk="🟢 LOW RISK"

            color="lightgreen"

        st.markdown(

        f"<h3 style='color:{color};'>⚠ Delay Risk Level : {risk}</h3>",

        unsafe_allow_html=True)

        # -------------------------
        # GLASS CHARTS
        # -------------------------

        materials=list(result.keys())

        values=list(result.values())

        colA,colB=st.columns(2)

        with colA:

            fig,ax=plt.subplots()

            ax.bar(materials,values,
            color=["#ff512f","#00c6ff",
                   "#7f00ff","#00ff95"])

            ax.set_facecolor("#111")

            plt.xticks(rotation=45)

            st.pyplot(fig)

        with colB:

            fig2,ax2=plt.subplots()

            ax2.pie(

            values,

            labels=materials,

            autopct='%1.1f%%',

            colors=["#ff512f",
                    "#00c6ff",
                    "#7f00ff",
                    "#00ff95"])

            st.pyplot(fig2)

        # -------------------------
        # DOWNLOAD REPORT
        # -------------------------

        df_report=pd.DataFrame(
        result,index=["Prediction"])

        st.download_button(

        "📥 Download Report",

        df_report.to_csv().encode(),

        "prediction.csv")

    # -------------------------
    # HISTORY
    # -------------------------

    if st.session_state.history:

        st.subheader("📜 Prediction History")

        st.dataframe(

        pd.DataFrame(
        st.session_state.history))

# --------------------------------------
# DATA PAGE
# --------------------------------------

elif menu=="Data Overview":

    st.title("📂 Dataset Overview")

    df=pd.read_csv(
    "data/construction_material_forecast_balanced1.csv")

    st.dataframe(df.head())

    st.write("Dataset Shape:",df.shape)

# --------------------------------------
# ABOUT PAGE
# --------------------------------------

else:

    st.title("📘 About This Project")

    st.write("""
    🎯 This AI system predicts construction material
    requirements using Multi-Output Linear Regression.

    💡 Inputs:
    - Area
    - Floors
    - Duration
    - Workers

    📦 Outputs:
    - Cement
    - Steel
    - Bricks
    - Asphalt

    🚀 Developed by Uday
    """)