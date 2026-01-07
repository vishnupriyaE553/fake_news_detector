# 🛠️ Step-by-Step Procedure (Implementation Using VS Code)
```
Step 1: Install Required Software

1.Installed Python (3.9+) on the system
2.Installed Visual Studio Code (VS Code)
3.Added the following VS Code extensions : Python

Step 2: Create Project Folder

1.Opened VS Code
2.Selected File → Open Folder
3.Created and opened a new folder: fake_news_detector

Step 3: Create Virtual Environment

1.In the VS Code terminal: python -m venv venv
2.Activated the environment:

   -Windows : venv\Scripts\activate

   -macOS/Linux : source venv/bin/activate

Step 4: Install Required Libraries

1.Created a file named requirements.txt and added:

  -streamlit
  -google-generativeai
  -python-dotenv

2.Installed dependencies: pip install -r requirements.txt

Step 5: Obtain Gemini API Key

1.Visited Google AI Studio
2.Generated a Gemini API Key
3.Created a .env file in the project root: GEMINI_API_KEY=your_api_key_here
4.The .env file was added to .gitignore to prevent exposing the API key.

Step 6: Design Application Logic (app.py)

1.Created app.py in VS Code
2.Imported required libraries:
  -streamlit
  -google.generativeai
  -os
3.Loaded the API key using environment variables
4.Configured the Gemini model

Step 7: Implement Fake News Detection Logic

1.Took user input using Streamlit text area
2.Sent the news text to Gemini API
3.Received Gemini’s response
4.Parsed the output to determine classification
5.Displayed: Fake News ❌ or Real News ✅

Step 8: Build User Interface with Streamlit

1.Added:

  -App title
  -Text input area
  -Analyze button

2.Applied basic UI styling using: style.css
3.Ensured the UI is responsive and user-friendly

Step 9: Run the Application Locally

1.Executed the following command in VS Code terminal: streamlit run app.py
```
