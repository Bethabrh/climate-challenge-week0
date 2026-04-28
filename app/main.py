import streamlit as st
import pandas as pd

def load_data(file_path):
    """Load dataset safely"""
    try:
        df = pd.read_csv(file_path)
        print(f"Loaded data successfully from {file_path}")
        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"Error loading file: {e}")
        return None


def clean_data(df):
    """Basic cleaning pipeline"""
    if df is None:
        return None

    df = df.drop_duplicates()
    df = df.fillna(method="ffill")

    return df
kenya = clean_data(load_data("data/kenya.csv"))
sudan = clean_data(load_data("data/sudan.csv"))
tanzania = clean_data(load_data("data/tanzania.csv"))
nigeria = clean_data(load_data("data/nigeria.csv"))
ethiopia = clean_data(load_data("data/ethiopia.csv"))
st.title("🌍 Climate Change Dashboard")

st.header("About Climate Change")
st.write("""
Climate change refers to long-term shifts in temperature and weather patterns.
These changes may be natural, but human activities have been the main driver since the 1800s.
""")
if kenya is None or sudan is None or tanzania is None:
    st.error("One or more datasets failed to load.")
else:
    st.success("All datasets loaded successfully!")

st.header("Key Issues")
st.write("- Rising global temperatures")
st.write("- Melting ice caps")
st.write("- Sea level rise")
st.write("- Extreme weather events")

st.success("This is my first climate app using Streamlit 🚀")



st.subheader("🇰🇪 Kenya EDA")

if kenya is not None:
    st.write("### Dataset Preview")
    st.dataframe(kenya.head())

    st.write("### Summary Statistics")
    st.write(kenya.describe())


st.subheader("🇸🇩 Sudan EDA")

if sudan is not None:
    st.write("### Dataset Preview")
    st.dataframe(sudan.head())

    st.write("### Summary Statistics")
    st.write(sudan.describe())

st.subheader("🇹🇿 Tanzania EDA")

if tanzania is not None:
    st.write("### Dataset Preview")
    st.dataframe(tanzania.head())

    st.write("### Summary Statistics")
    st.write(tanzania.describe())
   
   st.subheader("🇪🇹 Ethiopia EDA")

if ethiopia is not None:
    st.write("### Dataset Preview")
    st.dataframe(ethiopia.head())

    st.write("### Summary Statistics")
    st.write(ethiopia.describe())





st.subheader("🇳🇬 Nigeria EDA")

if nigeria is not None:
    st.write("### Dataset Preview")
    st.dataframe(nigeria.head())

    st.write("### Summary Statistics")
    st.write(nigeria.describe())    

