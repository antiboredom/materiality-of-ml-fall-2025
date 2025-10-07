from transformers import pipeline

classifier = pipeline("text-classification", model="./my_awesome_model/checkpoint-20/")

results = classifier("This is great!")
print(results)

results = classifier("This is so awful")
print(results)
