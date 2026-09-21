import pandas as pd
print(pd.__version__)
scores=pd.Series([88,99,100,40],
        index=['ali','ahmed','khaled','nadeem'],
        name="exam_score"
        )
print(scores)
print(scores['ali'])
print(scores.mean())
print(scores.max())