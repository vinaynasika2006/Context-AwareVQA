from vqa_model import VQAModel
from context_extractor import ContextExtractor
from bias import mitigate_bias

class VQASystem:
    def __init__(self):
        self.vqa = VQAModel()
        self.context = ContextExtractor()

    def answer_question(self, image, question):
        context_text = self.context.get_context(image)
        enhanced_question = f"Context: {context_text}. Question: {question}"
        answer = self.vqa.predict(image, enhanced_question)
        final_answer = mitigate_bias(answer)
        return final_answer, context_text
