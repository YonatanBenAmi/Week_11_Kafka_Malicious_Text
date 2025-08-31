#נצרך להסיר סחמני פיסוק
import re
import string
#נצרך לקבל קשימה של כל המילות חיבור
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
#דברים שהצטרך בשביל המציאת שורשים
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
import nltk




class Cleaner:
    def __init__(self):
        # self.data=data
        # self.clean_data=""
        pass


    #פונקציה שמנקה את הטקסט מסימני פיסוק
    def Removing_punctuation_marks(self,text):
        #פונקציה מובנת בפייתון שמנקה טקסטים מסימני פיסוק
        translator = str.maketrans('', '', string.punctuation)
        return text.translate(translator)

    # פונקציה להסרת סימני פיסוק ותווים מיוחדים
    def Remove_special_characters(self,text):
        cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
        return cleaned_text

    #מסירים רווחים מיותרים
    def Removing_unnecessary_whitespace_characters(self,text):
        clean_text = " ".join(text.split())
        return clean_text


    #ממירים את כל האותיות לאותיות קטנות
    def Converting_text_to_lowercase(self,text):
        clean_text = text.lower()
        return clean_text

    #מסיר את כל המילות חיבור
    def Removing_stop_words(self, text):
        words = text.split()
        filtered = [w for w in words if w.lower() not in ENGLISH_STOP_WORDS]
        return " ".join(filtered)


    def Lemtization(self,text):

        lemmatizer = WordNetLemmatizer()

        tokens = word_tokenize(text)

        tagged_tokens = pos_tag(tokens)

        def get_wordnet_pos(tag):
            if tag.startswith('J'):
                return 'a'
            elif tag.startswith('V'):
                return 'v'
            elif tag.startswith('N'):
                return 'n'
            elif tag.startswith('R'):
                return 'r'
            else:
                return 'n'

        lemmatized_sentence = []

        for word, tag in tagged_tokens:
            if word.lower() == 'are' or word.lower() in ['is', 'am']:
                lemmatized_sentence.append(word)
            else:
                lemmatized_sentence.append(lemmatizer.lemmatize(word, get_wordnet_pos(tag)))
        return ' '.join(lemmatized_sentence)




