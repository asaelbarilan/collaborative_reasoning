# evaluator.py

def simple_evaluator(response: str) -> float:
    """
    Evaluates the response based on keyword presence and length.
    Adjust this function based on specific evaluation criteria.
    """
    score = 0
    keywords = ["should", "because", "however", "therefore"]
    for keyword in keywords:
        if keyword in response.lower():
            score += 1
    score += len(response) / 100  # Length contributes to score
    return score
