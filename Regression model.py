import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.impute import SimpleImputer  # For handling missing values
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression  # Example model - replace with your choice
from sklearn.metrics import mean_squared_error

# Load data
df = pd.read_csv("your_data.csv")

# Handle missing values (replace with your strategy)
imputer = SimpleImputer(strategy="mean")  # Impute numerical features with mean
categorical_features = ['sex', 'smoker', 'region']
transformer = ColumnTransformer(transformers=[
    ("imputer", imputer, df.select_dtypes(include=[np.number])),  # Impute numerical features
    ("label", LabelEncoder(), categorical_features)  # Encode categorical features
])
df_transformed = pd.DataFrame(transformer.fit_transform(df))
df = pd.concat([df.drop(categorical_features, axis=1), df_transformed], axis=1)

# Target variable
target_variable = "charges"

# Feature selection (optional)
features = list(df.columns)  # Use all features initially (replace with chosen features)
features.remove(target_variable)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(df[features], df[target_variable], test_size=0.2, random_state=42)

# One-hot encode region feature (optional, consider if needed for your model)
# onehot_encoder = OneHotEncoder(sparse=False)
# region_encoded = onehot_encoder.fit_transform(X_train[:, features.index('region')].reshape(-1, 1))
# X_train[:, features.index('region')] = region_encoded
# Similar steps for X_test

# Model selection and training (replace with your chosen model)
model = LinearRegression()
model.fit(X_train, y_train)

# Model evaluation
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Prediction on new data (replace with your new data)
new_data = {"age": 35, "sex": "male", "bmi": 25, "children": 2, "smoker": "no", "region": "northeast"}
new_data_transformed = transformer.transform(pd.DataFrame([new_data]))
new_features = pd.DataFrame(new_data_transformed, columns=transformer.get_feature_names_out())
predicted_cost = model.predict(new_features)[0]
print("Predicted medical insurance cost:", predicted_cost)
