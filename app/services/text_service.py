from transformers import pipeline
import openai
import nltk
import os

openai.api_key = os.getenv('OPENAI_API_KEY')
openai.api_base = os.getenv('OPENAI_API_BASE')

nltk.download('punkt', quiet=True)

text_generator = pipeline('text-generation', model='gpt2')

def generate_text(prompt):
    """
    使用 GPT-2模型生成文本。
    """
    try:
        response = openai.Completion.create(
            engine='o4-mini',
            prompt=prompt
        )
        return response.choices[0].text.strip()
    except:
        result = text_generator(prompt)
        return result[0]['generated_text'].strip()