import streamlit as st
import pandas as pd
import time
import os

# --- file paths ---
tips_path = "./tips.csv"
image_path = "./media/image.jpg"
video_path = "./media/waterfalls.mp4"
audio_path = "./media/audio.mp3"

# --- Sidebar ---
side_bar = st.sidebar
side_bar.header("Sidebar — st.sidebar")
side_bar.caption("Elements added in the sidebar are pinned to the left")

# --- load tips.csv safely ---
if os.path.exists(tips_path):
    df = pd.read_csv(tips_path)
else:
    st.error(f"Could not find '{tips_path}'. Please place tips.csv in the app folder.")
    st.stop()

columns = tuple(df.columns)
st.write("Columns in dataset:", columns)

# selectbox for column selection
select_column = side_bar.selectbox(
    "Select the column you want to display",
    columns
)
side_bar.write(f"You selected the column_name = {select_column}")

# --- Layout Columns (middle wider) ---
st.header("Columns Layout Example")
col1, col2, col3 = st.columns([1, 4, 1])

with col1:
    st.write("Column 1")
    if os.path.exists(image_path):
        st.image(image_path, caption="Beautiful City", use_container_width=True)
    else:
        st.warning(f"Image not found: {image_path}")

with col2:
    st.write("Column 2 — Video")
    if os.path.exists(video_path):
        st.video(video_path)
    else:
        st.warning(f"Video not found: {video_path}")

with col3:
    st.write("Column 3") # Selected Column
    st.dataframe(df[[select_column]], use_container_width=True)

# ⭐⭐⭐ NEW SECTION: FULL DATAFRAME BELOW COLUMNS ⭐⭐⭐
st.header("Full DataFrame (Below Columns)")
st.dataframe(df, use_container_width=True)


# --- Expander ---
st.header("Expander: st.expander")
with st.expander("Some explanation"):
    st.write(
        """
        Insert a multi-element container that can be expanded/collapsed.
        Great for hiding long explanations or optional content.
        """
    )
    st.code(
        """
import streamlit as st
st.expander('message')
        """,
        language="python"
    )

# --- container ---
st.header("Container Example")
with st.container():
    st.write("You are inside a container block")

# --- Empty (placeholder) ---
st.header("Empty: st.empty")

placeholder = st.empty()
total_seconds = 10
for i in range(total_seconds):
    remaining = total_seconds - i
    placeholder.write(f"This message will disappear in {remaining} seconds")
    time.sleep(1)
placeholder.empty()

# --- Media demo ---
st.header("Media demo (Image + Audio)")

if os.path.exists(image_path):
    st.subheader("Extra Image")
    st.image(image_path, width=400)

if os.path.exists(audio_path):
    st.subheader("Audio")
    st.audio(audio_path)
