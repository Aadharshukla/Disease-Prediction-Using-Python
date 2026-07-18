1. Clone the Repository
git clone https://github.com/<your-username>/Disease-Prediction-Using-Python.git
cd Disease-Prediction-Using-Python
2. Install Python
Download and install Python 3.12 or later from:
https://www.python.org/downloads/⁠�
Verify the installation:
python --version
3. Install Ollama
Download and install Ollama from:
https://ollama.com/download⁠�
Verify the installation:
ollama --version
4. Download the AI Model
Open a terminal and run:
ollama pull llama3.2
This downloads the local Llama 3.2 model used by the application.
5. Install Required Python Packages
Navigate to the project folder and run:
pip install -r requirements.txt
If requirements.txt is unavailable, install manually:
pip install flet ollama
6. Start the Ollama Service
Ensure the Ollama application/service is running in the background.
7. Run the Application
Execute:
python main.py
The Disease Prediction System window will open.
8. Using the Application
Enter symptoms or a health-related question.
Click Send.
The application processes the request using the local AI model.
Non-medical questions are politely rejected.
Troubleshooting
pip not found: Reinstall Python and ensure Add Python to PATH is enabled.
Model not found: Run ollama pull llama3.2.
Connection error: Make sure Ollama is running.
Module not found: Run pip install -r requirements.txt.
