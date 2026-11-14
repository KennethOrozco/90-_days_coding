def gini_impurity(labels: list[int]) -> float:
    if not labels:
        return 0.0
    proportion_one = sum(labels) / len(labels)
    proportion_zero = labels.count(0) / len(labels)
    return 1 - (proportion_zero**2) - (proportion_one**2)

def weighted_gini(left: list[int], right: list[int]) -> float:
    if not left and not right:
        return 0.0
    left_gini_impurity = gini_impurity(left)
    right_gini_impurity = gini_impurity(right)
    total = len(left) + len(right)
    return (len(left)/total) * left_gini_impurity + (len(right)/ total) * right_gini_impurity

parent = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0]

split_a_left = [1, 1, 1, 1, 1]
split_a_right = [1, 0, 0, 0, 0]

split_b_left = [1, 1, 1, 0, 0]
split_b_right = [1, 1, 1, 0, 0]

parent_gini = gini_impurity(parent)
weighted_gini_a = weighted_gini(split_a_left, split_a_right)
weighted_gini_b = weighted_gini(split_b_left, split_b_right)
print(parent_gini)
if weighted_gini_a < weighted_gini_b:
    print("Split A is better because it is lower!")
else:
    print("Split B is better because it is lower!")

dictionary = {
    "split_a": {
        "left_split": split_a_left,
        "right_split": split_a_right,
        "weighted_gini": weighted_gini_a,
        "left_gini_impurity": gini_impurity(split_a_left),
        "right_gini_impurity": gini_impurity(split_a_right),
        "gini_reduction": parent_gini - weighted_gini_a
    },
    "split_b": {
        "left_split": split_b_left,
        "right_split": split_b_right,
        "weighted_gini": weighted_gini_b,
        "left_gini_impurity": gini_impurity(split_b_left),
        "right_gini_impurity": gini_impurity(split_b_right),
        "gini_reduction": parent_gini - weighted_gini_b
    }
}

min_val = min(dictionary[split]["weighted_gini"] for split in dictionary)
best_weighted_gini = [split for split in dictionary if dictionary[split]["weighted_gini"] == min_val]
print(best_weighted_gini)

print(dictionary["split_a"])
print(dictionary["split_b"])








    