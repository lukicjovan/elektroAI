
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import torch

_processor = None
_model = None

def _ucitaj_model():
    global _processor, _model
    if _processor is None or _model is None:
        _processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-handwritten")
        _model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-handwritten")
        _model.eval()
        _model.to("cpu")

def izvuci_tekst_iz_slike(image):
    _ucitaj_model()
    pixel_values = _processor(images=image, return_tensors="pt").pixel_values
    with torch.no_grad():
        generated_ids = _model.generate(pixel_values)
    generated_text = _processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return generated_text
