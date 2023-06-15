import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from joblib import dump



df = pd.read_csv('data.csv')


print(df.head())

# Get the summary statistics of the DataFrame
print(df.describe())

# Check for missing values
print(df.isnull().sum())


df.dropna(inplace=True)

df = df[(df[['views', 'likes', 'dislikes']] >= 0).all(axis=1)]

# Remove outliers based on Z-score
z_scores = stats.zscore(df)
abs_z_scores = np.abs(z_scores)
filtered_entries = (abs_z_scores < 3).all(axis=1)
df = df[filtered_entries]


sns.histplot(df['dislikes'], kde=True)
plt.show()


sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()

# Separate the features and the target variable
X = df[['views', 'likes']]
y = df['dislikes']


scaler = StandardScaler()
X = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)


mse = mean_squared_error(y_test, y_pred)
print(f'Test MSE: {mse}')

dump(scaler, 'scaler.joblib')
dump(model, 'yt_dislike_model.joblib')
