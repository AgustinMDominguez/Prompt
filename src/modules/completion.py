import openai

def complete_prompt(input: str) -> str:
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=input,
        temperature=0.1,
        max_tokens=50,
        echo=True
    )
    print(f"Token used in total: {response.usage.total_tokens}")
    return response.choices[0].text
