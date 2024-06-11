def top_three(scores):
    scores = scores
    top_scores = []
    
    # Solution
    scores.sort()
    list_size = len(scores)
    top_scores = [scores[list_size-1], scores[list_size-2], scores[list_size-3]]
    
    
    
    # Leave this line alone
    return top_scoresgit