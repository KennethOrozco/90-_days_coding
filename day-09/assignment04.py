def rank_developers(developers):
    return sorted(developers, key=lambda developer:(-developer['score'], developer['projects']))

developers = [
    {"name": "Alex", "score": 92, "projects": 4},
    {"name": "Jordan", "score": 88, "projects": 6},
    {"name": "Taylor", "score": 92, "projects": 3},
    {"name": "Morgan", "score": 79, "projects": 7}
]

print(rank_developers(developers))