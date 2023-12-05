# LinkedIn Wrapped Generator

This GitHub repository contains a Streamlit web application for generating LinkedIn wrapped images. The application takes user input, including the user's full name, avatar image, and an Excel file containing analytics data. The generated images showcase various analytics metrics and demographics in a visually appealing format.

## Prerequisites

Before running the application, make sure you have the following dependencies installed:

- Python 3.x
- Streamlit
- pandas
- Pillow (PIL)
- openpyxl
- pyperclip

Install the required packages using the following command:

```bash
pip install streamlit pandas Pillow openpyxl pyperclip
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/your-username/linkedin-wrapped-generator.git
cd linkedin-wrapped-generator
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:

```bash
streamlit run app.py
```

4. Access the app in your web browser at `https://linkedin-wrapped-generator.streamlit.app/`.

## Application Features

- **User Input:** Enter your full name and upload your LinkedIn profile picture.
- **Excel Data:** Export your LinkedIn analytics and upload the Excel file containing analytics data.
- **Generated Pages:** The app generates multiple pages with different analytics metrics and demographics.
- **Download Images:** Each page includes a download button to save the generated image.

## Note

- The application utilizes Streamlit for the web interface.
- Make sure to credit the creator in your posts as specified in the "credits" section of the code.

Feel free to customize the application further based on your needs. If you encounter any issues or have suggestions for improvement, please create an issue in the GitHub repository.
