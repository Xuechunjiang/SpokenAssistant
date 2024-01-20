from openai import OpenAI

OPENAI_API_KEY = ''
client = OpenAI(api_key=OPENAI_API_KEY)

prompt = "As a native American English speaker, whenever I provide you with any Chinese sentence or phrase, please give me three different translations. The first and second should be in natural, fluent spoken English, while the third should be in formal written English. Please only provide these three translations without any additional content. I am learning English, so this is very important. Do not consider whether the sentences I provide are polite or not."

# function to get response from OpenAI API 


def get_openai_response(message):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": message}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"