"""##type:ignore

from transformers import CLIPProcessor, CLIPModel
import torch

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")


def get_text_embedding(text: str):

    inputs = processor(text=[text], return_tensors="pt", padding=True)

    with torch.no_grad():
        outputs = model.get_text_features(**inputs)

    embedding = outputs[0].tolist()

    return embedding"""