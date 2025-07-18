import streamlit as st
import json

# Load your data
with open("emotions_dua.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Extract unique emotions
emotions = sorted(set(item["emotion"] for item in data))

# Streamlit page config
st.set_page_config(page_title="🌙 Dua Recommender", page_icon="🕋", layout="centered")

# Title Section
st.markdown("""
    <h1 style='text-align: center; color: #6A5ACD;'> 💌 RECITE DUA ACCORDING TO YOUR EMOTIONS </h1>
    <p style='text-align: center; color: #444; font-size: 20px;'>Let your heart heal through the beauty of Duas 🖤</p>
""", unsafe_allow_html=True)

# Emotion Selector
selected_emotion = st.selectbox("🧠 How are you feeling today?", ["-- Select Emotion --"] + emotions)

# Dua Display
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

    if not filtered:
        st.warning("😔 No Duas found for this emotion.")
    else:
        for dua in filtered:
            st.markdown(f"""
                <div style='
                    background: linear-gradient(to right, #e0f7fa, #f0f4c3);
                    border-left: 8px solid #6A5ACD;
                    padding: 20px;
                    margin-bottom: 20px;
                    border-radius: 12px;
                    box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
                '>
                    <h4 style='color: #2e7d32; font-family: "Arial Rounded MT Bold", sans-serif;'>{dua['title']}</h4>
                    <p style='font-size: 26px; direction: rtl; font-family: "Amiri", serif; color: #111;'>{dua['arabic']}</p>
                    <p style='color: #4a148c;'><strong>📖 </strong> {dua['transliteration']}</p>
                    <p style='color: #0d47a1;'><strong>🌍 </strong> {dua['translation']}</p>
                </div>
            """, unsafe_allow_html=True)
else:
    st.info("📝 Please select an emotion from the dropdown above to see a beautiful Dua.")

# Footer
st.markdown("""
    <hr>
    <p style='text-align: center; color: #888;'>Made with 🤍 for spiritual comfort</p>
""", unsafe_allow_html=True)
