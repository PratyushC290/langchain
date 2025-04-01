import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title and Introduction
st.title("Streamlit Basics - Notes")
st.write("This file covers the basics of Streamlit, including UI elements, user input, charts, caching, and deployment.")

# Section 1: Displaying Text
st.header("1. Displaying Text")
st.text("This is a simple text message.")
st.write("This is a general-purpose write function.")
st.markdown("### Markdown is also supported.")
st.subheader("This is a subheader example.")

# Section 2: Displaying Data
st.header("2. Displaying Data")
df = pd.DataFrame(np.random.randn(10, 5), columns=["A", "B", "C", "D", "E"])
st.dataframe(df)  # Interactive table
st.table(df.head())  # Static table

# Section 3: User Input
st.header("3. Taking User Input")
name = st.text_input("Enter your name")
st.write("Hello, ", name)

age = st.number_input("Enter your age", min_value=1, max_value=100, step=1)
st.write("Your age is:", age)

if st.button("Click Me"):
    st.write("Button clicked!")

# Section 4: File Upload
st.header("4. File Upload")
uploaded_file = st.file_uploader("Upload a file")
if uploaded_file is not None:
    st.write("Filename:", uploaded_file.name)

# Section 5: Layout and Sidebar
st.header("5. Layout and Sidebar")
st.sidebar.title("Sidebar Example")
option = st.sidebar.selectbox("Select an option", ["A", "B", "C"])
st.write("You selected:", option)

col1, col2 = st.columns(2)
col1.write("Column 1 Content")
col2.write("Column 2 Content")

with st.expander("Click to Expand"):
    st.write("Here is some additional information.")

# Section 6: Charts and Visualization
st.header("6. Adding Charts")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])
st.line_chart(chart_data)

fig, ax = plt.subplots()
ax.hist(np.random.randn(100), bins=20)
st.pyplot(fig)

# Section 7: Caching for Performance
st.header("7. Caching for Performance")

@st.cache_data
def load_data():
    return pd.DataFrame(np.random.randn(10, 5), columns=["A", "B", "C", "D", "E"])

df_cached = load_data()
st.dataframe(df_cached)

# Section 8: Interactive Widgets
st.header("8. Interactive Widgets")
selected_number = st.selectbox("Choose a number:", [1, 2, 3, 4, 5])
st.write("You selected:", selected_number)

slider_value = st.slider("Select a value", 0, 100, 50)
st.write("Slider value:", slider_value)

# Section 9: Deployment Notes
st.header("9. Deployment Notes")
st.markdown("""
### Deploying with Streamlit Cloud:
1. Push your code to **GitHub**.
2. Go to [Streamlit Cloud](https://share.streamlit.io/).
3. Connect your GitHub repo and deploy.

### Deploying with Heroku:
1. Create a `requirements.txt`:
2. Create a `Procfile`:
3. Deploy using Heroku CLI.
""")

st.success("End of Notes. You can use this file as a reference for Streamlit development!")