def bayesian_update(prior_probs, likelihoods, evidence):
    # Multiply prior by likelihood for the given evidence
    numerators = [prior * likelihood for prior, likelihood in zip(prior_probs, likelihoods[evidence])]

    # Calculate the total probability of the evidence
    total_evidence_prob = sum(numerators)

    # Bayes' Rule: Divide each (prior * likelihood) by total evidence probability
    posterior_probs = [num / total_evidence_prob for num in numerators]

    return posterior_probs


def coin_flip_sequence(sequence, coin_probs):
    # Initial probabilities for each coin being selected
    prior_probs = [1 / len(coin_probs) for _ in coin_probs]

    # Likelihood of flipping H or T for each coin
    likelihoods = {
        'H': coin_probs,
        'T': [1 - p for p in coin_probs]
    }

    # For each flip in the sequence, update the probabilities
    for flip in sequence:
        prior_probs = bayesian_update(prior_probs, likelihoods, flip)
        print(
            f"After flip {flip}, probability of H next: {sum(p * l for p, l in zip(prior_probs, likelihoods['H'])):.2f}")

    return prior_probs


# Given coin head probabilities
coin_probs = [0.1, 0.2, 0.4, 0.8, 0.9]
# Given sequence
sequence = ['H', 'H', 'H', 'T', 'H', 'T', 'H', 'H']

coin_flip_sequence(sequence, coin_probs)