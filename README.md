# 🧠 Context-Aware Visual Question Answering System

A Visual Question Answering (VQA) system that extracts image context using pretrained BLIP and combines it with user questions to generate answers.

## 🚀 Features

- Image-based question answering
- Context extraction using BLIP
- Context-enhanced VQA
- Rule-based answer post-processing
- Interactive Streamlit interface
- CPU/GPU support

## 🏗️ Architecture

```text
Image
 ↓
BLIP Image Captioning
 ↓
Context Extraction
 ↓
Context + Question
 ↓
BLIP VQA
 ↓
Post-Processing
 ↓
Final Answer
📁 Project Structure
Context-AwareVQA/
├── app.py
├── main.py
├── vqa_model.py
├── context_extractor.py
├── bias.py
├── requirements.txt
└── README.md
⚙️ Installation
git clone https://github.com/vinaynasika2006/Context-AwareVQA.git
cd Context-AwareVQA
pip install -r requirements.txt
▶️ Run
streamlit run app.py

Open:

http://localhost:8501
🧪 Usage
Upload an image.
Enter a question.
Click Analyze Image.
The system extracts context and generates an answer.

Example:

Context: cricket game

Question: What is the person doing?

Answer: hitting ball

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
Rule-based post-processing is limited to predefined terms.
No formal accuracy or fairness benchmark has been performed.
🔮 Future Improvements
Fine-tuning on VQA datasets
Standard benchmark evaluation
Better context-question fusion
Advanced bias mitigation
Confidence estimation
BLIP-2/LLaVA integration
Explainable AI
