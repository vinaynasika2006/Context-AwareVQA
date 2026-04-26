from transformers import BlipProcessor, BlipForConditionalGeneration
import torch

class ContextExtractor:
    def __init__(self):
        self.processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        self.model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    def get_context(self, image):
        inputs = self.processor(image, return_tensors="pt")
        with torch.no_grad():
            output = self.model.generate(**inputs)
        return self.processor.decode(output[0], skip_special_tokens=True)
