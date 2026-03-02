from statistics import median

from sentence_transformers import SentenceTransformer, util

# Load a domain-specific sentence embedding model (SciBERT with SBERT)
model = SentenceTransformer('allenai-specter',
                            device='cpu')  # Good for AI/ML text. Alternative: 'allenai/scibert_scivocab_uncased'


def calculate_similarity(sentence1: str, sentence2: str) -> float:
    embedding1 = model.encode(sentence1, convert_to_tensor=True)
    embedding2 = model.encode(sentence2, convert_to_tensor=True)

    cosine_similarity = util.pytorch_cos_sim(embedding1, embedding2)

    return cosine_similarity.item()


def print_similarity_stats(similarity_scores: list[float]):
    average_similarity_score = sum(similarity_scores) / len(similarity_scores)
    print('avg: ', average_similarity_score)

    median_similarity_score = median(similarity_scores)
    print('med: ', median_similarity_score)

    min_similarity_score = min(similarity_scores)
    print('min: ', min_similarity_score)

    max_similarity_score = max(similarity_scores)
    print('max: ', max_similarity_score)

    return average_similarity_score, median_similarity_score, min_similarity_score, max_similarity_score