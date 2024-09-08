from django.conf import settings
from openai import OpenAI
import json

CLIENT = OpenAI(api_key=settings.OPENAI_API_KEY)

def product_help_bot(request):
    system_instructions = """
    너는 지금 부터 "한국어로 온라인 쇼핑몰 상품의 제목과 내용을 자동으로 작성해 주는 도우미"야. 
    사용자가 제공한 제품 정보를 분석하여 적절한 제목과 상세한 설명을 작성해. 
    상품의 특성을 잘 반영하고, 매력적인 문구로 작성해야 해. 
    상품의 카테고리나 타겟 소비자에 맞게 자연스럽고 설득력 있는 한국어로 작성해 줘.
    해시태그 같은 경우에는 "#"이 아닌 ","로 구분해서 보여줘야 해.
    그리고 제목은 제목이라고 앞에 명시해주고 내용또는 상세내용은 앞에 내용으로 통일해서 명시해줘야 해.
    """
    data = request.body
    data = data.decode('utf-8')
    data = json.loads(data)
    message = data['text']
    history = data['history']
    if history != '':
        completion = CLIENT.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content":system_instructions,
                },
                {
                    "role": "user",
                    "content": message,
                },
                {
                    "role": "assistant", 
                    "content": history,
                },
            ],
        )
    else:
        completion = CLIENT.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content":system_instructions,
                },
                {
                    "role": "user",
                    "content": message,
                },
            ],
        )
    return completion.choices[0].message