import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from joblib import dump


# Load the data
df = pd.read_csv('./ML/data.csv')

# Check the first few rows of the DataFrame
print(df.head())

# Separate the features and the target variable
X = df[['views', 'likes']]
y = df['dislikes']

# Split the data into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f'Test MSE: {mse}')

# Save the model
dump(model, 'yt_dislike_model.joblib') 
