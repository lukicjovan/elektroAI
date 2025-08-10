from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import torch

# === Inicijalizuj model i procesor (samo jednom pri pokretanju) ===
processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-handwritten")
model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-handwritten")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

def ocr_sa_trocr_lokalno(putanja_slike):
    try:
        slika = Image.open(putanja_slike).convert("RGB")
        inputs = processor(images=slika, return_tensors="pt").to(device)

        with torch.no_grad():
            output_ids = model.generate(inputs.pixel_values)
        tekst = processor.batch_decode(output_ids, skip_special_tokens=True)[0]

        if tekst and len(tekst.strip()) >= 2:
            print(f"[TrOCR LOCAL] Prepoznato: '{tekst.strip()}'")
            return tekst.strip(), False  # uspešan OCR, bez fallback
        else:
            raise Exception("Prazan rezultat iz lokalnog TrOCR modela.")
    except Exception as e:
        print(f"[TrOCR LOCAL ERROR] {putanja_slike} → {e}")
        return "", True  # fallback aktiviran, možeš pozvati EasyOCR ako želiš