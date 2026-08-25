import streamlit as st
from PIL import Image

from main import VQASystem


st.set_page_config(
    page_title="Context-Aware VQA",
    page_icon="🧠",
    layout="centered"
)


st.title("🧠 Context-Aware VQA")

st.write(
    "Ask questions about an image using "
    "context extraction and visual question answering."
)


@st.cache_resource
def load_system():
    return VQASystem()


st.header("📷 Upload Image")

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)


if uploaded_file is not None:

    image = Image.open(
        uploaded_file
    ).convert("RGB")

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    st.header("❓ Ask a Question")

    question = st.text_input(
        "Enter your question",
        placeholder="Example: What is the person doing?"
    )

    if st.button(
        "🚀 Analyze Image",
        type="primary"
    ):

        if not question.strip():

            st.warning(
                "Please enter a question."
            )

        else:

            system = load_system()

            with st.spinner(
                "Processing image..."
            ):

                answer, context = system.answer_question(
                    image,
                    question
                )

            st.success(
                "Analysis completed successfully!"
            )

            st.header("📊 Results")

            st.subheader("🧠 Extracted Context")

            st.info(context)

            st.subheader("❓ Question")

            st.write(question)

            st.subheader("💡 Final Answer")

            st.success(answer)

            with st.expander(
                "🔍 View Processing Details"
            ):

                st.write(
                    "**Context:**"
                )

                st.write(context)

                st.write(
                    "**Question:**"
                )

                st.write(question)

                st.write(
                    "**Answer:**"
                )

                st.write(answer)

else:

    st.info(
        "Upload an image above to start."
    )


st.divider()

st.caption(
    "Context-Aware VQA | BLIP | Streamlit"
)
