import numpy as np
import pandas as pd

# exericitul 1
print("Exercitiul 1")

matrix = np.full((7,7), 7, dtype=float)
np.fill_diagonal(matrix, [33, 33, 33, 77, 33, 33, 33])

for i in range(1,6):
    matrix[i, i-1] = 0
    matrix[i, i+1] = 0

print(matrix)

# exercitiul 2
print("Exercitiul 2")

matrix = np.full((7,7), np.nan)

matrix[:] = 5
matrix[1:-1, 1:-1] = 0

print(matrix)

# exercitiul 3
print("Exercitiul 3")
sub_matrix = matrix[1:-1, 1:-1]
print(sub_matrix)

# exercitiul 4
print("Exercitiul 4")
random_vector = np.random.uniform(0, 10, 100)
labels = [f'L_{i}' for i in range(1, 101)]
series = pd.Series(random_vector, index=labels)
print(series)

# exercitiul 5
print("Exercitiul 5")
random_array = np.random.uniform(0, 10, (11,5))

row_labels = [f'L_{i}' for i in range (1, 12)]
column_labels = [f'C_{i}' for i in range (1, 6)]
dataframe = pd.DataFrame(random_array, index=row_labels, columns=column_labels)
print(dataframe)

# exercitiul 6
print("Exercitiul 6")
students = {f'S_{i}': np.random.randint(1, 11, 7).tolist() for i in range(1,9)} # punem 1, 11, 7 pentru ca generam 7 note random intre 1 si 10 (11 e exlusiv, 1 e inclusiv)
df = pd.DataFrame(students)

print(df)

# exercitiul 7
print("Exercitiul 7")

students2 = {f'Stud{i}': np.random.randint(1, 11, 5).tolist() for i in range(1,8)}
labels2 = [f'Ex{i}' for i in range(1, 6)]
df2 = pd.DataFrame(students2, index=labels2)
print(df2)

# exercitiul 8
print("Exercitiul 8") # trebuie sa ai fisierele respective ca sa ruleze
series_1 = pd.read_csv('Series_1.csv')
series_2 = pd.read_csv('Series_2.csv')
data_dict = {
    'Col1': series_1,
    'Col2': series_2
}
df = pd.DataFrame(data_dict)
print(df)

# exercitiul 9
print("Exercitiul 9")
data = {
    f'An{i}': {
        f'Stud{j}': np.random.randint(1, 11, 5).tolist()  # 5 random grades for each student
        for j in range(1, 9)  # 'Stud1' to 'Stud8'
    }
    for i in range(1, 6)  # 'An1' to 'An5'
}
df = pd.DataFrame(data)
print(df)
