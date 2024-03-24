import pandas as pd
import random
import numpy as np
import os

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

CHAT_MODEL_PATH = "model_components/forgex_model"
EMBEDDINGS_PATH = "model_components/question_embeddings.npy"
SIMILARITY_THRESHOLD = 0.5


CONFUSED_REPONSES = (
    [
        "I'm sorry, I'm still under development for general conversation topics. But I'm great at science! Ask me "
        "anything science-related.",
        "That's an interesting question, but it's beyond my current expertise. Let's focus on science today. What "
        "do you want to know?",
        "Intriguing! However, my specialty is science. How can I help you explore that fascinating world?",
    ],
)


def create_model_essential():
    df = pd.read_csv("model_components/final_data.csv")
    model = SentenceTransformer("paraphrase-distilroberta-base-v1")
    question_embeddings = model.encode(df["question"].tolist())
    model.save(CHAT_MODEL_PATH)
    np.save(EMBEDDINGS_PATH, question_embeddings)


def get_answer(user_input):
    df = pd.read_csv("model_components/final_data.csv")
    if not os.path.exists(CHAT_MODEL_PATH) or not os.path.exists(EMBEDDINGS_PATH):
        create_model_essential()
    model = SentenceTransformer(CHAT_MODEL_PATH)
    question_embeddings = np.load(EMBEDDINGS_PATH)
    user_input_embedding = model.encode([user_input])
    similarities = cosine_similarity(user_input_embedding, question_embeddings)[0]
    most_similar_index = similarities.argmax()
    if similarities[most_similar_index] > SIMILARITY_THRESHOLD:
        return df.iloc[most_similar_index]["support"]
    else:
        return random.choice(CONFUSED_REPONSES[0])
