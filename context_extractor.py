import torch

from transformers import (
    BlipProcessor,
    BlipForConditionalGeneration
)


class ContextExtractor:

    def __init__(self):

        self.device = torch.device(
            "cuda"
            if torch.cuda.is_available()
            else "cpu"
        )

        self.processor = BlipProcessor.from_pretrained(
            "Salesforce/blip-image-captioning-base"
        )

        self.model = BlipForConditionalGeneration.from_pretrained(
            "Salesforce/blip-image-captioning-base"
        )

        self.model = self.model.to(
            self.device
        )

        self.model.eval()


    def get_context(self, image):

        inputs = self.processor(
            images=image,
            return_tensors="pt"
        )

        inputs = {
            key: value.to(self.device)
            for key, value in inputs.items()
        }

        with torch.no_grad():

            output = self.model.generate(
                **inputs,
                max_new_tokens=30
            )

        context = self.processor.decode(
            output[0],
            skip_special_tokens=True
        )

        return context
