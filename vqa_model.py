import torch

from transformers import (
    BlipProcessor,
    BlipForQuestionAnswering
)


class VQAModel:

    def __init__(self):

        self.device = torch.device(
            "cuda"
            if torch.cuda.is_available()
            else "cpu"
        )

        self.processor = BlipProcessor.from_pretrained(
            "Salesforce/blip-vqa-base"
        )

        self.model = BlipForQuestionAnswering.from_pretrained(
            "Salesforce/blip-vqa-base"
        )

        self.model = self.model.to(
            self.device
        )

        self.model.eval()


    def predict(
        self,
        image,
        question
    ):

        inputs = self.processor(
            images=image,
            text=question,
            return_tensors="pt"
        )

        inputs = {
            key: value.to(self.device)
            for key, value in inputs.items()
        }

        with torch.no_grad():

            output = self.model.generate(
                **inputs,
                max_new_tokens=20
            )

        answer = self.processor.decode(
            output[0],
            skip_special_tokens=True
        )

        return answer
