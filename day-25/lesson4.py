
probabilities = [0.15, 0.35, 0.49, 0.50, 0.62, 0.78, 0.93]

thresholds = [.5, .3, .7]

results = {}

for threshold in thresholds:
    predictions = [1 if probability >= threshold else 0 for probability in probabilities]
    results[threshold] = predictions
    print("Threshold: ", threshold)
    print("Class: ", predictions)
    print("Count Passed", sum(predictions))

at_five = results[0.5]
at_seven = results[0.7]

for index, (five , seven) in enumerate(zip(at_five, at_seven)):
    letter = chr(65 + index)
    if five != seven:
        print(f"Student {letter}'s classification has changed!")







