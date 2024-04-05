# ML dependencies
import pickle
import pandas as pd
from tensorflow.keras.preprocessing import sequence
import numpy as np
from tensorflow.keras.models import model_from_json

class ChatbotService:
    
    def __init__(self):
        print("Initializing!!!!")
        # Load tokenizer from pickle file
        with open('files/abc.pickle', 'rb') as handle:
            self.tokenizer = pickle.load(handle)

    
    def load_model():
        # Load the model architecture from JSON file
        with open("files/model.json", "r") as json_file:
            loaded_model_json = json_file.read()

        # Load the model architecture
        loaded_model = model_from_json(loaded_model_json)

        # Load the model weights
        loaded_model.load_weights("files/model.h5")

        return loaded_model
    

    def get_sentiment(self, model, text):
        # Tokenize the text
        max_len = 160
        sent_to_id  = {"Jenkins-Maven":0, "Jenkins-Python":1,"Jenkins-iOS":2, "Jenkins-Generic": 3}
        twt = self.tokenizer.texts_to_sequences([text])
        twt = sequence.pad_sequences(twt, maxlen=max_len, dtype='int32')
        
        # Predict sentiment
        task = model.predict(twt, batch_size=1, verbose=2)
        
        # Round the sentiment percentages
        sent = np.round(np.dot(task, 100).tolist(), 0)[0]
        
        # Create a DataFrame with sentiment labels and percentages
        result = pd.DataFrame([sent_to_id.keys(), sent]).T
        result.columns = ["content", "percentage"]
        
        # Filter out entries with zero percentage
        result = result[result.percentage != 0]
        
        return result

    
    def chatbot_conversation(self, text):      
        try:
            print("chabot processing...")
            model = self.load_model()
            result = self.get_sentiment(model, text)
            return result, 200
        except Exception as ex:
            return f"Unable to process: {ex}", 500
        
   
