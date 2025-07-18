import streamlit as st
import json

# Load your data once
with open("emotions_dua.json.ini", "r", encoding="utf-8") as f:
    data = json.load(f)



# Extract unique emotions
emotions = sorted(set(item["emotion"] for item in data))

# Streamlit page config
st.set_page_config(page_title="Dua Recommender", page_icon="🌙")
st.title("🌙 RECITE DUA ACCORDING TO YOUR EMOTIONS ")
st.markdown("Select how you feel to receive a comforting Dua.")

# Emotion Dropdown
selected_emotion = st.selectbox("How are you feeling?", ["-- Select Emotion --"] + emotions)

# Only show when an emotion is selected
if selected_emotion != "-- Select Emotion --":
    # Filter unique duas
    filtered = []
    seen = set()

    for item in data:
        if item["emotion"] == selected_emotion:
            key = (item["title"], item["arabic"], item["transliteration"], item["translation"])
            if key not in seen:
                seen.add(key)
                filtered.append(item)

    # Show message if no duas found
    if not filtered:
        st.warning("No Duas found for this emotion.")
    else:
        for dua in filtered:
            st.markdown(
                f"""
                <div style='
                    background-color: #f9f9f9;
                    border: 1px solid #ddd;
                    padding: 20px;
                    border-radius: 12px;
                    margin-bottom: 20px;
                    color: #222;
                '>
                    <h4 style='color: #2c3e50;'>{dua['title']}</h4>
                    <p style='font-size: 24px; direction: rtl; font-family: "Amiri", serif; color: #1a1a1a;'>{dua['arabic']}</p>
                    <p><strong>Transliteration:</strong> {dua['transliteration']}</p>
                    <p><strong>Translation:</strong> {dua['translation']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
else:
    st.info("Please select an emotion from the dropdown above to see a relevant Dua 🌿.")
