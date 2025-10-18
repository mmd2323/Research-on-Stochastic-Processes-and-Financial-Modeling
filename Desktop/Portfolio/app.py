import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="Mamadou Mbengue | Portfolio",
    layout="wide"
)

# --- Header Section ---
st.title("Mamadou Mbengue")
st.subheader("Financial Mathematics and Economics Student | Aspiring Data Analyst")

st.write(
    """
    Welcome to my personal website.  
    I am a **Financial Mathematics and Economics** student at the **University of Ottawa**, 
    passionate about **quantitative finance**, **machine learning**, and **stochastic modeling**.
    """
)

# --- Quick Links ---
st.markdown(
    """
    **Contact Information**  
    Ottawa, Ontario  
    [momodouserign00@gmail.com](mailto:momodouserign00@gmail.com)  
    [LinkedIn](https://linkedin.com/in/mamadou-mbengue-29968122a)  
    [GitHub](https://github.com/mmd2323)
    """
)

st.divider()

# --- About Me ---
st.header("About Me")
st.write(
    """
    I am currently a **fourth-year Financial Mathematics and Economics student** at the University of Ottawa.  
    My studies combine economics, statistics, and programming, and my interests include **data science**, 
    **financial modeling**, and **stochastic processes**.  
    I have developed strong technical skills in R, Python, and econometric analysis, and I enjoy applying 
    quantitative methods to real-world financial problems.
    """
)

st.divider()

# --- Projects Section ---
st.header("Projects")

col1, col2 = st.columns(2, gap="large")

# --- Project 1 ---
with col1:
    st.subheader("Research on Stochastic Processes and Financial Modeling")
    st.write(
        """
        Conducted a comprehensive research project on **stochastic calculus** and its applications 
        in finance as part of my **Research Assistant position**.  
        Topics included **martingales**, **Brownian motion**, **Ito’s lemma**, and **stochastic differential equations**.  
        Implemented **Python simulations** to demonstrate the **Black–Scholes model**, **Greeks**, 
        and **jump-diffusion processes**.
        """
    )
    st.link_button(
        "View Research Repository",
        "https://github.com/mmd2323/Research-on-Stochastic-Processes-and-Financial-Modeling"
    )

# --- Project 2 ---
with col2:
    st.subheader("MAT4372 – Machine Learning Portfolio Optimization")
    st.write(
        """
        Designed and implemented a **Random Forest regression model** to estimate **Sharpe ratios** 
        and construct the **efficient frontier** of a two-asset ETF portfolio (**VFV.TO** and **VCN.TO**).  
        The project integrates **quantitative finance**, **machine learning**, and **portfolio theory** 
        to evaluate risk–return trade-offs.  
        Results were visualized using **ggplot2** in R.
        """
    )
    st.link_button(
        "View Project Repository",
        "https://github.com/mmd2323/MAT4372-Machine-Learning-Portfolio-Optimization"
    )

st.divider()

# --- Resume Download Section ---
st.header("Download My Resume")
with open("Mamadou_Mbengue_Resume_ENG.pdf", "rb") as file:
    st.download_button(
        label="Download Resume (PDF)",
        data=file,
        file_name="Mamadou_Mbengue_Resume.pdf",
        mime="application/pdf"
    )

# --- Footer ---
st.divider()
st.caption("© 2025 Mamadou Mbengue | University of Ottawa | Financial Mathematics and Economics")
