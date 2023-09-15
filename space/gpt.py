import openai

openai.api_key = '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'

def generate_response(prompt):
    try:
        # Make a request to the GPT-3 API
        response = openai.Completion.create(
            engine="text-davinci-002",  # You can change the engine as needed
            prompt=prompt,
            max_tokens=50,  # Adjust max tokens as needed
            n=1,  # Number of responses to generate
            stop=None,  # You can provide a stopping condition if needed
        )

        # Extract and return the generated text from the API response
        return response.choices[0].text.strip()

    except Exception as e:
        # Handle exceptions here, e.g., log errors or return a default response
        return str(e)


