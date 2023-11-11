import panel as pn
from sklearn.metrics import accuracy_score, classification_report
from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from dataloader import df  
from xgbb import xgboost_pipeline
from xgbb import random_forest_pipeline
from xgbb import adaboost_pipeline

# Load your logo image (replace 'path/to/your/logo.png' with the actual path to your logo file)
logo_path = 'C:/Users/harou/Desktop/Projetdata/spotifylogo.png'




n_trees = pn.widgets.IntSlider(start=2, end=100, name="Number of trees")
max_depth = pn.widgets.IntSlider(start=1, end=50, value=2, name="Maximum Depth") 
booster = pn.widgets.Select(options=['gbtree', 'gblinear', 'dart'], name="Booster")

n_estimators = pn.widgets.IntSlider(start=2, end=100, name="Number of Estimators")
max_depth_rf = pn.widgets.IntSlider(start=1, end=50, value=2, name="Maximum Depth")

n_estimators_ab = pn.widgets.IntSlider(start=2, end=100, name="Number of Estimators")
learning_rate_ab = pn.widgets.FloatSlider(start=0.01, end=2.0, step=0.01, value=1.0, name="Learning Rate")

# Create a layout
tabs_layout = pn.Column(
    "<h2>Machine Learning Dashboard/h2>",  # Add your title here
    pn.Tabs(
        ("XGBoost", pn.Column(n_trees, max_depth, booster, xgboost_pipeline)),
        ("Random Forest", pn.Column(n_estimators, max_depth_rf, random_forest_pipeline)),
        ("AdaBoost", pn.Column(n_estimators_ab, learning_rate_ab, adaboost_pipeline)),
    ),
)

# Serve the app
tabs_layout.servable()