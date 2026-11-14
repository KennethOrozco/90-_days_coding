scores = [45, 72, 88, 59, 61, 30, 95]
labels = [int(score >= 60) for score in scores]

for score, label in zip(scores, labels):
    passed = "Passed" if label  else "Failed"
    print(f"Score: {score} -- Class: {passed}")