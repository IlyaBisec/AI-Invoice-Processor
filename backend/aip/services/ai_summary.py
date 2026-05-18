# AI summarization service.
# Uses OpenAI API to generate invoice summaries
# 18.05.2026 (c) ilya_bisec

from openai import OpenAI

from aip.core.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def generate_summary(invoice_text: str):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "Summarize invoices in one short business sentence."
            },
            {
                "role": "user",
                "content": invoice_text
            }
        ]
    )

    return response.choices[0].message.content