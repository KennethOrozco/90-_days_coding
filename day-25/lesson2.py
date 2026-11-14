import math

study_hours = [1, 3, 5, 7, 9]

z = []

for sample in study_hours:
    raw_score = 0.8 * sample - 4
    z.append(raw_score)

sigmoids = []
for raw_score in z:
    sigmoid = 1 / (1 + math.exp(-raw_score))
    sigmoids.append(sigmoid)

classes = [1 if sigmoid >= 0.5 else 0 for sigmoid in sigmoids]

for index, hours in enumerate(study_hours):
    print(f"Study hours: {hours}")
    print(f"Raw Score: {z[index]:.3f}")
    print(f"Probability: {sigmoids[index]:.3f}")
    print(f"Predicted Class: {classes[index]}")

probabilites = []
for hours, sigmoid in zip(study_hours, sigmoids):
    a = abs(sigmoid - 0.5)
    dictionary = {
        "study_hours": hours,
        "distance_from_half": a
    }
    probabilites.append(dictionary)

closest = min(probabilites, key=lambda probability: probability["distance_from_half"])

print("Study hours: ", closest["study_hours"])



