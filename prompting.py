def build_prompt(context, question):

    prompt = f"""
You are an expert agriculture assistant.

Answer the question using the provided context.

Context:
{context}

Question:
{question}

Answer in simple language.
"""

    return prompt