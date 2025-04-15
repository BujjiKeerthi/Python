import numpy as np
from django.http import JsonResponse
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

speed = np.array([10, 20, 30, 40, 45]).reshape(-1, 1)
steering_angle = np.array([0.1, 0.2, 0.15, 0.3, 0.25])

# Train Polynomial Regression Model
poly = PolynomialFeatures(degree=5)
speed_poly = poly.fit_transform(speed)
model = LinearRegression()
model.fit(speed_poly, steering_angle)

def predict_steering(request):
    try:
        speeds = request.GET.getlist("speed")  
        if not speeds:
            return JsonResponse({"error": "No speed values provided"}, status=400)

        results = []
        for speed_value in speeds:
            try:
                speed_value = float(speed_value)
                speed_value_poly = poly.transform([[speed_value]])  
                predicted_angle = model.predict(speed_value_poly)[0]

                results.append({"speed": speed_value, "predicted_steering_angle": round(predicted_angle, 3)})

            except ValueError:
                results.append({"speed": speed_value, "error": "Invalid speed value"})

        return JsonResponse({"predictions": results})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
