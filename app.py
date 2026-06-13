"""
app.py

Purpose
-------
Flask application for Car Price Prediction.

Responsibilities
----------------
1. Display HTML form
2. Collect user input
3. Send data to prediction pipeline
4. Display prediction result
"""

# ==================================================
# Flask Imports
# ==================================================

from flask import (
    Flask,
    request,
    render_template
)

# ==================================================
# Project Imports
# ==================================================

from src.pipeline.prediction_pipeline import (
    PredictPipeline,
    CustomData
)

# ==================================================
# Create Flask Application
# ==================================================

app = Flask(__name__)

# ==================================================
# Home Route
# ==================================================

@app.route("/")
def index():
    """
    Home Page

    URL:
        http://localhost:5000/
    """

    return render_template(
        "home.html"
    )


# ==================================================
# Prediction Route
# ==================================================

@app.route(
    "/predict",
    methods=["GET", "POST"]
)
def predict_data():
    """
    Prediction Endpoint

    GET:
        Show Form

    POST:
        Make Prediction
    """

    try:

        # ======================================
        # Show Form
        # ======================================

        if request.method == "GET":

            return render_template(
                "home.html"
            )

        # ======================================
        # Handle Prediction Request
        # ======================================

        else:

            # ----------------------------------
            # Collect User Inputs
            # ----------------------------------

            year = int(
                request.form.get("Year")
            )

            present_price = float(
                request.form.get(
                    "Present_Price"
                )
            )

            kms_driven = float(
                request.form.get(
                    "Kms_Driven"
                )
            )

            fuel_type = (
                request.form.get(
                    "Fuel_Type"
                )
            )

            seller_type = (
                request.form.get(
                    "Seller_Type"
                )
            )

            transmission = (
                request.form.get(
                    "Transmission"
                )
            )

            owner = int(
                request.form.get(
                    "Owner"
                )
            )

            # ----------------------------------
            # Create CustomData Object
            # ----------------------------------

            data = CustomData(

                Year=year,

                Present_Price=
                present_price,

                Kms_Driven=
                kms_driven,

                Fuel_Type=
                fuel_type,

                Seller_Type=
                seller_type,

                Transmission=
                transmission,

                Owner=owner
            )

            # ----------------------------------
            # Convert To DataFrame
            # ----------------------------------

            pred_df = (
                data.get_data_as_dataframe()
            )

            # ----------------------------------
            # Prediction Pipeline
            # ----------------------------------

            predict_pipeline = (
                PredictPipeline()
            )

            prediction = (
                predict_pipeline.predict(
                    pred_df
                )
            )

            # ----------------------------------
            # Display Result
            # ----------------------------------

            result = round(
                prediction[0],
                2
            )

            return render_template(

                "home.html",

                prediction_text=
                f"Predicted Car Price: "
                f"{result} Lakhs"

            )

    except Exception as e:

        return render_template(

            "home.html",

            prediction_text=
            f"Error: {str(e)}"
        )


# ==================================================
# Run Flask Server
# ==================================================

if __name__ == "__main__":

    app.run(

        host="0.0.0.0",

        port=5000,

        debug=True

    )