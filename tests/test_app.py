import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict_endpoint():
    # Example of input matching your model's features
    sample_input = [-1.99658302, -0.69424232, -0.04407492, 1.6727735, 0.97336551,
                     -0.24511658, 0.34706795, 0.19367894, 0.08263728, 0.33112778,
                     0.08338555, -0.54040704, -0.61829572, -0.99609892, -0.32461019,
                     1.60401384, -0.53683287, 0.24486345, 0.03076993, 0.49628203,
                     0.32611802, -0.02492336, 0.38285444, -0.17691133, 0.11050692,
                     0.24658544, -0.39217043, 0.33089162, -0.06378115, 0.24496426]

    response = client.post("/predict", json={"features": sample_input})
    assert response.status_code == 200
    assert "prediction" in response.json()