import openai


def load_prompt_template(filepath="prompts/test_scenarios.txt"):
    with open(filepath, "r") as f:
        return f.read()

def generate_test_scenarios(feature_text):
    template = load_prompt_template()
    prompt = template.replace("{{feature_text}}", feature_text)

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=1000,
    )

    return response.choices[0].message['content']
