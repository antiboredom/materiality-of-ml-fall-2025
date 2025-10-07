from transformers import pipeline

clf = pipeline(
    "image-classification",
    model="./results3/checkpoint-39",
)

results = clf("./Hot_dog_with_mustard.png")
print(results)
results = clf("/Users/sam/Downloads/newschoolcard.jpg")
print(results)
results = clf("./hotdog_nothotdog/val/hotdog/13355622.jpg")
print(results)

results = clf(
    "https://kagi.com/proxy/__opt__aboutcom__coeus__resources__content_migration__serious_eats__seriouseats.com__recipes__images__2014__02__20140128-hot-dogs-4505-meats-ryan-farr-63-5e3b8dd4f9e34a488e2c0ccb40e9ce51.jpg?c=L388tWaRgztlhTUL7vPk5M1PGep7WsHCU3-5u0SUyl11_GsRwVEsdJauNphLt7ZY7plGXIBZV2143_6hOhTbU1F1ddOr2HARK2Gsmx1RZHP1cWDXbfX4_ptEg9jxhL3n8EBAyZSzqf5aCZ3R3II5fZBQtnOU1mquhVtNlPeNS8b7-a1eB_15SwPm6XAvisNZIbSrNq7hj_oS2J-LjDQ4FX7D3IeUeUUJsPYf-6Ma9seunsX0oZwXWVNUxZW5Z1EiParfcB_CbFw1wLMvU2agSR4pylE-ZXfwQFSObnHvi3_dUcwEkGevtNL3v6raYZT6QguhniVGu8Mcnj9ZX9et9q_6ta3VppgrAHaI-Bqy-yzzxZZg5I4KPN7tEf4QALlgBeTEBxXycTUoHeAIWWrtpwqJ5ajKAol0GQwDtjZK1nEczWksXVrFEjYeayKu4biQ"
)

print(results)

results = clf("./500px-Joe_Biden_presidential_portrait.jpg")
print(results)
