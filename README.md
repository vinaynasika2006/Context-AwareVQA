# 🧠 Context-Aware Visual Question Answering System

A Visual Question Answering (VQA) system that extracts image context using pretrained BLIP and combines it with user questions to generate answers.

## 🚀 Features

- Image-based question answering
- Image context extraction
- Context-enhanced VQA
- Rule-based answer post-processing
- Streamlit web interface
- CPU/GPU support

## 🏗️ Project Structure

    Context-AwareVQA/
    ├── app.py
    ├── main.py
    ├── vqa_model.py
    ├── context_extractor.py
    ├── bias.py
    ├── requirements.txt
    └── README.md

## ⚙️ Installation

Install the required packages:

    pip install -r requirements.txt

The pretrained BLIP models are downloaded automatically on the first run.

## ▶️ Run

Start the application:

    streamlit run app.py

Open:

    http://localhost:8501

## 🧪 Usage

1. Upload an image.
2. Enter a question.
3. Click **Analyze Image**.
4. The system extracts image context.
5. The context is combined with the question.
6. BLIP generates an answer.
7. The processed answer is displayed.

## 🧠 Models

- `Salesforce/blip-image-captioning-base`
- `Salesforce/blip-vqa-base`

## 🛠️ Technologies

- Python
- PyTorch
- Hugging Face Transformers
- BLIP
- Streamlit
- Pillow

## ⚠️ Limitations

- Pretrained VQA models may produce incorrect answers.
- Generated context may not always be accurate.
- Answers may be short or ambiguous.
- Post-processing is limited to predefined rules.

## 🔮 Future Improvements

- Fine-tuning on VQA datasets
- Standard VQA evaluation
- Improved context-question fusion
- Advanced bias mitigation
- Confidence estimation
- BLIP-2 or LLaVA integration
- Explainable AI
