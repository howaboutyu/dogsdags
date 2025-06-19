from transformers import pipeline
from PIL import Image
import os

def classify_image(image_path):
    classifier = pipeline("image-classification")
    image = Image.open(image_path)
    results = classifier(image)
    return results

if __name__ == "__main__":
    assets_dir = "assets"
    image_file = "logo1.png"
    image_path = os.path.join(assets_dir, image_file)
    print(f"Classifying image: {image_path}")
    results = classify_image(image_path)
    print("Top classification results:")
    for res in results:
        print(f"- {res['label']} (score: {res['score']:.4f})")
