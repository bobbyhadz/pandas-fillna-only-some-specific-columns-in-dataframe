# Panda: Using fillna() with a specific column in a DataFrame

import pandas as pd

df = pd.DataFrame({
    'ID': [1, 1, None, 2, 2, None],
    'Animal': ['Cat', 'Cat', None, 'Dog', 'Dog', None],
    'Max Speed': [25, 35, None, 55, 65, None]
})

print(df)

print('-' * 50)

df['Animal'] = df['Animal'].fillna(value='Anonymous')

print(df)