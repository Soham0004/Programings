import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression  # Example model - replace with your choice
from sklearn.metrics import mean_squared_error
import numpy as np  # Needed for imputer

# Load data
df = pd.read_csv("your_data.csv")

# Handle missing values (replace with your strategy)
imputer = SimpleImputer(strategy="mean")  # Impute numerical features with mean
categorical_features = ['room_type', 'neighbourhood_group']
transformer = ColumnTransformer(transformers=[
    ("imputer", imputer, df.select_dtypes(include=[np.number])),  # Impute numerical features
    ("label", LabelEncoder(), categorical_features),  # Encode categorical features
    ("onehot", OneHotEncoder(sparse=False), categorical_features)  # One-hot encode categories
])
df_transformed = pd.DataFrame(transformer.fit_transform(df))
df = pd.concat([df.drop(categorical_features, axis=1), df_transformed], axis=1)

# Feature engineering (optional)
df['year'] = pd.to_datetime(df['last_review']).dt.year  # Extract year from last_review

# Target variable
target_variable = "price"

# Feature selection (optional)
features = list(df.columns)  # Use all features initially (replace with chosen features)
features.remove(target_variable)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(df[features], df[target_variable], test_size=0.2, random_state=42)

# Feature scaling (optional but recommended)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Model selection and training (replace with your chosen model)
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# Model evaluation
y_pred = model.predict(X_test_scaled)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Prediction on new data (replace with your new data)
new_listing_data = {"room_type": "Entire home/apt", "neighbourhood_group": "Downtown", 
                    # Add other features here with their corresponding values
                    "minimum_nights": 3,  # Example features
                    "number_of_reviews": 10}
new_listing_transformed = transformer.transform(pd.DataFrame([new_listing_data]))
new_listing_features = pd.DataFrame(new_listing_transformed, columns=transformer.get_feature_names_out())
predicted_price = model.predict(scaler.transform(new_listing_features))[0]
print("Predicted price for new listing:", predicted_price)
