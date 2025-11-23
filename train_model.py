# Simple training script (synthetic data)
import numpy as np, pandas as pd, joblib
from sklearn.ensemble import RandomForestRegressor
from pathlib import Path
models = Path('models'); models.mkdir(exist_ok=True)
rng = np.random.RandomState(42)
n=300
difficulty = rng.randint(1,6,n)
priority = rng.randint(1,6,n)
actual_time = difficulty * (1.0 + rng.rand(n)) + (6-priority)*0.25 + rng.normal(scale=0.4, size=n)
X = pd.DataFrame({'difficulty':difficulty, 'priority':priority})
y = actual_time
model = RandomForestRegressor(n_estimators=100, random_state=1)
model.fit(X, y)
joblib.dump(model, models/'time_predictor.joblib')
print('Saved model to models/time_predictor.joblib')
