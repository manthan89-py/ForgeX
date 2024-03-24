import os
import pandas as pd


def create_question_answer_intent_from_dataset(db_path, merged_df):
    for f in os.listdir(db_path):
        if f.endswith(".csv"):
            df = pd.read_csv(os.path.join(dataset_path, f), encoding="utf-8")
            df = df[["question", "support"]]
            merged_df = pd.concat([merged_df, df], ignore_index=True)
    return merged_df


def create_greeting_intent(merged_df):
    intents = {
        "question": [
            "hello",
            "hi",
            "hey",
            "good day",
            "Hey buddy",
            "what's up?",
            "How is it going?",
            "How are you?",
            "Hola.",
            "Hey there",
        ],
        "support": [
            "Hi there! How can I help you explore science today?",
            "Hello! What science questions do you have for me?",
            "Greetings! I'm ready to answer your scientific inquiries.",
            "Hey! Let's delve into the fascinating world of science!",
            "Good morning/afternoon/evening! What scientific wonders can I help you understand?",
            "Welcome! I'm your friendly science companion. Ask away!",
            "Excited to be your guide on this scientific journey! What do you want to know?",
            "Fascinated by science? Let's explore it together. What are you curious about?",
            "Feeling curious? I'm here to quench your scientific thirst. Ask me anything!",
            "Ready to unlock the secrets of science? Let's begin your exploration!",
        ],
    }
    return pd.concat([merged_df, pd.DataFrame(intents)], ignore_index=True)


def create_bye_intent(merged_df):
    intents = {
        "question": ["bye", "goodbye", "thanks"],
        "support": [
            "Have a fantastic day! Reach out if you have more science questions.",
            "See you next time! Keep exploring the wonders of science.",
            "It was a pleasure assisting you. Until next time!",
        ],
    }
    return pd.concat([merged_df, pd.DataFrame(intents)], ignore_index=True)


def create_about_me_intent(merged_df):
    intents = {
        "question": [
            "who are you",
            "who created you",
            "who developed you",
            "tell me about yourself",
        ],
        "support": [
            "I'm a science chatbot ForgeX! Designed to answer your scientific questions! I'm still under development, "
            "but I'm learning more every day.",
            "I'm a friendly AI companion ForgeX! Created to help you explore the wonders of science. Ask me anything!",
            "Chatbots are conversational AI programs that can simulate human interaction. I'm a specific type focused "
            "on scientific inquiries.",
            "I was created by programmer name Manthan who are passionate about science communication and AI technology.",
        ],
    }
    return pd.concat([merged_df, pd.DataFrame(intents)], ignore_index=True)


def create_confused_intent(merged_df):
    intents = {
        "question": [
            "I don't understand",
            "What do you mean by that?",
            "Can you rephrase that?",
            "Sorry, I'm not sure.",
        ],
        "support": [
            "Hmm, I see what you're asking, but I need more information. Can you rephrase your question?",
            "That's an interesting question! I'm still learning, but I can try to find some info for you. What were "
            "you curious about?",
            "Science can be tricky sometimes. Maybe we can break it down a bit.  Can you tell me more about what "
            "you're interested in?",
            "Let's see if I can find something related to that. Can you give me a keyword or specific topic?",
        ],
    }
    return pd.concat([merged_df, pd.DataFrame(intents)], ignore_index=True)


if __name__ == "__main__":
    merged_df = pd.DataFrame()
    dataset_path = "Datasets/"
    destination_file_path = "Corpus/intents.json"

    merged_df = create_question_answer_intent_from_dataset(dataset_path, merged_df)
    merged_df = create_greeting_intent(merged_df)
    merged_df = create_bye_intent(merged_df)
    merged_df = create_about_me_intent(merged_df)
    merged_df = create_confused_intent(merged_df)
    print(merged_df)
    merged_df.to_csv("final_data.csv")
