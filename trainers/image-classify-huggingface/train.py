from transformers import (
    AutoImageProcessor,
    AutoModelForImageClassification,
    Trainer,
    TrainingArguments,
)
from datasets import load_dataset

# replace the path with the location of your image folder
dataset = load_dataset("imagefolder", data_dir="./hotdog_nothotdog/")

labels = dataset["train"].features["label"].names
id2label = {i: label for i, label in enumerate(labels)}
label2id = {label: i for i, label in enumerate(labels)}

# change this if you want!
model_name = "google/vit-base-patch16-224"

processor = AutoImageProcessor.from_pretrained(model_name)

model = AutoModelForImageClassification.from_pretrained(
    model_name,
    num_labels=len(labels),
    id2label=id2label,
    label2id=label2id,
    ignore_mismatched_sizes=True,
)


def preprocess(batch):
    batch["pixel_values"] = processor(batch["image"], return_tensors="pt").pixel_values
    return batch


dataset = dataset.map(preprocess, batched=True, remove_columns=["image"])

training_args = TrainingArguments(
    output_dir="./results3",
    num_train_epochs=3,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    eval_strategy="epoch",
    save_strategy="epoch",
    logging_steps=10,
    remove_unused_columns=False,
    load_best_model_at_end=True,
)

# Train
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"],
    eval_dataset=dataset["validation"],
    processing_class=processor,
)

trainer.train()

# processor.save_pretrained("ok")
