from transformers import CLIPProcessor, CLIPModel
import torch


class ModelService:

    _clip_model = None
    _clip_processor = None

    @classmethod
    def get_clip_model(cls):

        if cls._clip_model is None:

            print("Loading CLIP model...")

            cls._clip_model = CLIPModel.from_pretrained(
                "openai/clip-vit-base-patch32"
            )

            cls._clip_processor = CLIPProcessor.from_pretrained(
                "openai/clip-vit-base-patch32"
            )

        return cls._clip_model, cls._clip_processor



        #Now CLIP loads only once.