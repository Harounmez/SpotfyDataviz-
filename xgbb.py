import panel as pn
from sklearn.metrics import accuracy_score, classification_report
from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from dataloader import df  # Make sure to adjust the import statement based on your project structure
from sklearn.ensemble import AdaBoostClassifier
from sklearn.cluster import KMeans
from sklearn.cluster import MiniBatchKMeans


# Assuming 'track_genre' is the target column
X = df.drop('track_genre', axis=1)
y = df['track_genre']

# Encode labels
encoder = LabelEncoder()
y = encoder.fit_transform(y)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# XGBoost Section



n_trees = pn.widgets.IntSlider(start=2, end=100, name="Number of trees")
max_depth = pn.widgets.IntSlider(start=1, end=50, value=2, name="Maximum Depth") 
booster = pn.widgets.Select(options=['gbtree', 'gblinear', 'dart'], name="Booster")

@pn.depends(n_trees.param.value, max_depth.param.value, booster.param.value)
def xgboost_pipeline(n_trees, max_depth, booster):
    model = XGBClassifier(max_depth=max_depth, n_estimators=n_trees, booster=booster)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = round(accuracy_score(y_test, y_pred) * 100, 1)
    
    classreport = classification_report(y_test, y_pred, target_names=encoder.classes_, zero_division=1)
    return pn.Column(
        pn.indicators.Number(
            name=f"Test score",
            value=accuracy,
            format="{value}%",
            colors=[(97.5, "red"), (99.0, "orange"), (100, "green")],
            align='center'
        ),
        pn.pane.Str(classreport, height_policy="min", sizing_mode="stretch_width"),
        align='center'
    )

# Random Forest Section


n_estimators = pn.widgets.IntSlider(start=2, end=100, name="Number of Estimators")
max_depth_rf = pn.widgets.IntSlider(start=1, end=50, value=2, name="Maximum Depth")

@pn.depends(n_estimators.param.value, max_depth_rf.param.value)
def random_forest_pipeline(n_estimators, max_depth_rf):
    model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth_rf)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = round(accuracy_score(y_test, y_pred) * 100, 1)
    classreport = classification_report(y_test, y_pred, target_names=encoder.classes_, zero_division=1)
    return pn.Column(
        pn.indicators.Number(
            name=f"Test score",
            value=accuracy,
            format="{value}%",
            colors=[(97.5, "red"), (99.0, "orange"), (100, "green")],
            align='center'
        ),
        pn.pane.Str(classreport, height_policy="min", sizing_mode="stretch_width"),
        align='center'
    )



n_estimators_ab = pn.widgets.IntSlider(start=2, end=100, name="Number of Estimators")
learning_rate_ab = pn.widgets.FloatSlider(start=0.01, end=2.0, step=0.01, value=1.0, name="Learning Rate")

@pn.depends(n_estimators_ab.param.value, learning_rate_ab.param.value)
def adaboost_pipeline(n_estimators, learning_rate):
    model = AdaBoostClassifier(n_estimators=n_estimators, learning_rate=learning_rate)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = round(accuracy_score(y_test, y_pred) * 100, 1)
    classreport = classification_report(y_test, y_pred, target_names=encoder.classes_, zero_division=1)
    return pn.Column(
        pn.indicators.Number(
            name=f"Test score",
            value=accuracy,
            format="{value}%",
            colors=[(97.5, "red"), (99.0, "orange"), (100, "green")],
            align='center',
        ),
        pn.pane.Str(classreport, height_policy="min", sizing_mode="stretch_width"),
        align='center',
    )
