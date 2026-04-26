import streamlit as st
from PIL import Image

st.set_page_config(page_title="VQA System", layout="centered")

st.title("🧠 Context-Aware Bias-Resilient VQA System")

# Debug / status
st.write("✅ App started")

# Safe import with error handling
try:
    from main import VQASystem
    st.write("✅ Model modules loaded")
except Exception as e:
    st.error(f"❌ Import Error: {e}")
    st.stop()

# Cache model (VERY IMPORTANT for performance)
@st.cache_resource
def load_system():
    return VQASystem()

# UI Inputs
uploaded_file = st.file_uploader("📷 Upload an image", type=["jpg", "png", "jpeg"])
question = st.text_input("❓ Ask a question about the image")

# Main logic
if uploaded_file:
    try:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Uploaded Image", use_column_width=True)
    except Exception as e:
        st.error(f"❌ Image Error: {e}")
        st.stop()

if uploaded_file and question:

    try:
        system = load_system()

        with st.spinner("🔄 Processing... First run may take time (model download)"):
            answer, context = system.answer_question(image, question)

        st.success("✅ Done!")

        st.subheader("🧠 Extracted Context")
        st.write(context)

        st.subheader("💡 Answer")
        st.write(answer)

    except Exception as e:
        st.error(f"❌ Runtime Error: {e}")

else:
    st.info("👉 Please upload an image and enter a question to proceed.")