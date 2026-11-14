import numpy as np

study_hours = np.array([1, 3, 5, 7, 9])

attendance = np.array([50, 65, 75, 85, 95])

passed = np.array([0, 0, 1, 1, 1])


X= np.column_stack((study_hours, attendance))

y = passed

print(X)
print(X.shape)
print(y)
print(y.shape)

