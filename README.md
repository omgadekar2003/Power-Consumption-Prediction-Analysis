# Power Consumption Prediction Web App

This repository contains a web application built using **Streamlit** for predicting power consumption in three zones based on environmental and time-based factors. The app utilizes a **machine learning model** (saved as a `.joblib` file) that predicts power consumption based on inputs such as temperature, humidity, wind speed, and more(also see this:[https://github.com/omgadekar2003/Power_Consumption_Analysis]).

### Table of Contents
- [About](#about)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [App Deployment](#app-deployment)
- [Model Explanation](#model-explanation)
- [Contributing](#contributing)
- [License](#license)

---

## About

This web application uses machine learning models to predict power consumption for three zones. The app accepts user inputs such as temperature, humidity, wind speed, diffuse flows, and other factors. Based on this data, the app predicts the power consumption for **Zone 1**, **Zone 2**, and **Zone 3**.

The model has been trained and saved as a `.joblib` file, which is used to make predictions within the app. The app is built with **Streamlit** and deployed to Streamlit Cloud for easy access.

---

## Features

- Predict power consumption for **Zone 1**, **Zone 2**, and **Zone 3** based on multiple environmental parameters.
- Interactive web interface with input fields for each parameter.
- Predicts power consumption in real-time based on user inputs.
- Model loading is handled efficiently using `joblib`.
- Simple and user-friendly design for easy interaction.

---

## Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **Modeling**: Scikit-learn (for building and training the model)
- **Model Serialization**: Joblib (to save and load the model)
- **Deployment**: Streamlit Cloud

---

## Installation

### Prerequisites

Make sure you have Python installed. You can download Python from [here](https://www.python.org/downloads/).

### Steps to Run Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/power-consumption-prediction.git
   cd power-consumption-prediction
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**:
   ```bash
   streamlit run app.py
   ```

   This will start the Streamlit app locally. You can open the app in your browser by visiting [http://localhost:8501](http://localhost:8501).

---

## Usage

Once the app is running, follow these steps:

1. Open the app in your browser.
2. Fill in the input fields with the relevant data:
   - **Temperature** (°C)
   - **Humidity** (%)
   - **Wind Speed** (m/s)
   - **General Diffuse Flows**
   - **Diffuse Flows**
   - **Day of the Year**
   - **Month**

3. Click the **"Predict"** button.
4. The app will display the predicted power consumption for:
   - **Zone 1**
   - **Zone 2**
   - **Zone 3**

---

## App Deployment

The app is deployed on **Streamlit Cloud**. You can access the live app [here](https://pow-consume-om.streamlit.app/).

To deploy the app to your own Streamlit Cloud account, follow these steps:

1. Go to [Streamlit Cloud](https://share.streamlit.io/).
2. Click **"New App"** and link it to your GitHub repository.
3. Streamlit will automatically install the required dependencies and run the app.

---

## Model Explanation

The machine learning model used in this app was trained using **Scikit-learn** and saved as a `.joblib` file. The model predicts power consumption based on the following input features:
- **Temperature**
- **Humidity**
- **Wind Speed**
- **General Diffuse Flows**
- **Diffuse Flows**
- **Day of the Year**
- **Month**

### Steps to Train the Model:
1. Preprocess the data (e.g., handling missing values, scaling features).
2. Train the model using an appropriate algorithm (e.g., linear regression, decision tree, etc.).
3. Save the trained model using `joblib`:
   ```python
   import joblib
   joblib.dump(model, 'model.joblib')
   ```

---

## Contributing

We welcome contributions to this project. If you would like to contribute, please follow these steps:

1. Fork this repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Contact

If you have any questions, feel free to reach out to me via [GitHub Issues](https://github.com/your-username/power-consumption-prediction/issues).

---

**Note:** Be sure to replace the placeholder `your-username` with your actual GitHub username in the link and relevant sections of the file.

Regards,
Om
