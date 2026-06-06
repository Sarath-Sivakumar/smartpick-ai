import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

with open("data/phones.json", "r") as f:
    phones = json.load(f)

phone_texts = []

for phone in phones:
    text = f"""
    {phone['name']}
    Camera: {phone['camera']}
    Battery: {phone['battery']}
    Gaming: {phone['gaming']}
    Display: {phone['display']}
    Processor: {phone['processor']}
    Price: {phone['price']}
    """
    phone_texts.append(text)

phone_embeddings = model.encode(
    phone_texts
)


def retrieve(query, top_k=3):

    query_embedding = model.encode(
        [query]
    )

    scores = cosine_similarity(
        query_embedding,
        phone_embeddings
    )[0]

    ranked = sorted(
        zip(scores, phones),
        reverse=True,
        key=lambda x: x[0]
    )

    return ranked[:top_k]