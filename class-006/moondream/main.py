from transformers import AutoModelForCausalLM
from PIL import Image
import torch

# Load the model
model = AutoModelForCausalLM.from_pretrained(
    "vikhyatk/moondream2",
    trust_remote_code=True,
    dtype=torch.bfloat16,
    device_map="mps",
)

# Load your image
image = Image.open("./sample.jpg")

# Optional sampling settings
settings = {"max_objects": 50}

# Run Moondream
result = model.detect(image, "police", settings=settings)
print(result)

print("Short caption:")
print(model.caption(image, length="short")["caption"])

print(model.query(image, "How many people are in the image?")["answer"])
