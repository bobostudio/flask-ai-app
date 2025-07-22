from transformers import pipeline
import openai
import nltk
import os

openai.api_key = os.getenv('OPENAI_API_KEY')
openai.api_base = os.getenv('OPENAI_API_BASE')

nltk.download('punkt', quiet=True)

text_generator = pipeline('text-generation', model='gpt2')
sentiment_analyzer = pipeline('sentiment-analysis')
summarizer = pipeline('summarization')
translator = pipeline('translation', model='Helsinki-NLP/opus-mt-en-zh')
qa_model = pipeline('question-answering')

def generate_text(prompt):
    """
    使用 GPT-2模型生成文本。
    """
    result = text_generator(prompt,max_new_tokens=256, num_return_sequences=1,
                             output_scores=True, return_dict_in_generate=True)
    return result[0]['generated_text'].strip()
    try:
        response = openai.Completion.create(
            engine='o4-mini',
            prompt=prompt
        )
        return response.choices[0].text.strip()
    except:
        result = text_generator(prompt)
        return result[0]['generated_text'].strip()

def analyze_sentiment(text):
    result = sentiment_analyzer(text)
    return result[0]['label'], result[0]['score']


def summarization(text):
    result = summarizer(text, max_length=150, min_length=30, do_sample=False)
    return result[0]['summary_text'].strip()    


def translate_text(text):
    result = translator(text, max_length=400)
    return result[0]['translation_text'].strip()

def answer_question(question, context):
    result = qa_model(question=question, context=context)
    return result['answer'].strip()