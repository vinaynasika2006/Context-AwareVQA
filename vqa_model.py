from transformers import BlipProcessor, BlipForQuestionAnswering
import torch

class VQAModel:
    def __init__(self):
        self.processor = BlipProcessor.from_pretrained("Salesforce/blip-vqa-base")
        self.model = BlipForQuestionAnswering.from_pretrained("Salesforce/blip-vqa-base")

    def predict(self, image, question):
        inputs = self.processor(image, question, return_tensors="pt")
        with torch.no_grad():
            output = self.model.generate(**inputs)
        return self.processor.decode(output[0], skip_special_tokens=True)
