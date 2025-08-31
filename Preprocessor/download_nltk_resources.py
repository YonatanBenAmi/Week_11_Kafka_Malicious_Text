# download_nltk_resources.py
import nltk

# רשימת המשאבים שאנחנו רוצים להוריד
resources = [
    'punkt',                       # tokenizer
    'averaged_perceptron_tagger',  # POS tagging
    'wordnet',                      # מילון לממטיזציה
    'omw-1.4',                      # מילון תרגום ללמטיזציה
]

# הורדה
for resource in resources:
    print(f"Downloading {resource}...")
    nltk.download(resource)

print("All NLTK resources downloaded successfully!")
