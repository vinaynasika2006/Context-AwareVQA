# 🧠 Context-Aware Visual Question Answering System

A Visual Question Answering (VQA) system that extracts image context using pretrained BLIP and combines it with user questions to generate answers.

## 🚀 Features

- Image-based question answering
- Image context extraction
- Context-enhanced VQA
- Rule-based answer post-processing
- Streamlit web interface
- CPU/GPU support

## 🏗️ Architecture

Image → BLIP Captioning → Context → Context + Question → BLIP VQA → Post-Processing → Answer

## 📁 Project Structure

```text
Context-AwareVQA/
├── app.py
├── main.py
├── vqa_model.py
├── context_extractor.py
├── bias.py
├── requirements.txt
└── README.md
⚙️ Installation
pip install -r requirements.txt

The required packages include PyTorch, Transformers, Pillow, and Streamlit.

The pretrained BLIP models are downloaded automatically on the first run.

▶️ Run
streamlit run app.py

Open:

http://localhost:8501
🧪 Usage
Upload an image.
Enter a question.
Click Analyze Image.
The system extracts image context.
The context is combined with the question.
BLIP generates an answer.
The processed answer is displayed.
🧠 Models
Salesforce/blip-image-captioning-base
Salesforce/blip-vqa-base
🛠️ Technologies
Python
PyTorch
Hugging Face Transformers
BLIP
Streamlit
Pillow
⚠️ Limitations
Pretrained VQA models may produce incorrect answers.
Generated context may not always be accurate.
Answers may be short or ambiguous.
Post-processing is limited to predefined rules.
🔮 Future Improvements
Fine-tuning on VQA datasets
Standard VQA evaluation
Improved context-question fusion
Advanced bias mitigation
Confidence estimation
BLIP-2 or LLaVA integration
Explainable AI
