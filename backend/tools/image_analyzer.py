##type:ignore

"""from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import torch
print("IMAGE ANALYZER LOADED")

device = "cuda" if torch.cuda.is_available() else "cpu"

# load model once
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(device)
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")


def get_image_embedding(image_path: str):

    image = Image.open(image_path).convert("RGB")

    inputs = processor(images=image, return_tensors="pt")

    inputs = {k: v.to(device) for k, v in inputs.items()}

    with torch.no_grad():
        image_features = model.get_image_features(**inputs)

    embedding = image_features[0].cpu().numpy()

    return embedding
"""
"""from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import torch

print("IMAGE ANALYZER LOADED")

device = "cuda" if torch.cuda.is_available() else "cpu"

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(device)
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")


def get_image_embedding(image_path: str):

    image = Image.open(image_path).convert("RGB")

    inputs = processor(images=image, return_tensors="pt")
    inputs = {k: v.to(device) for k, v in inputs.items()}

    with torch.no_grad():
        image_features = model.get_image_features(pixel_values=inputs["pixel_values"])

    # Extract tensor if transformers wraps it
    if hasattr(image_features, "image_embeds"):
        image_features = image_features.image_embeds

    embedding = image_features[0].detach().cpu().numpy().flatten().tolist()

    return embedding"""


# backend/tools/image_analyzer.py

"""from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import torch

print("IMAGE ANALYZER LOADED")

device = "cuda" if torch.cuda.is_available() else "cpu"

# Load model once
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(device)
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")


def get_image_embedding(image_path: str):

    image = Image.open(image_path).convert("RGB")

    inputs = processor(images=image, return_tensors="pt")
    inputs = {k: v.to(device) for k, v in inputs.items()}

    with torch.no_grad():

        outputs = model.get_image_features(**inputs)

    # outputs shape: (1, 512)
    embedding = outputs[0].detach().cpu().numpy().flatten().tolist()

    print("CLIP image embedding size:", len(embedding))

    return embedding"""