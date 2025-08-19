# HSBC Argentina Bank Statement Converter

A simple and efficient web application that converts HSBC Argentina bank statement PDFs to CSV format for easier data analysis and processing.

## 🔍 Overview

This Streamlit-based web application allows users to upload their HSBC Argentina bank statement PDFs and automatically converts them to CSV format. The tool extracts transaction details including dates, references, amounts, and descriptions, making it easy to analyze your banking data in spreadsheet applications.

## ✨ Features

- **PDF Upload**: Simple drag-and-drop interface for uploading bank statement PDFs
- **Automatic Parsing**: Intelligent extraction of transaction data from HSBC Argentina statements
- **CSV Export**: Downloads processed data in CSV format with semicolon separators
- **Web Interface**: User-friendly Streamlit web application
- **Real-time Processing**: Instant conversion and download

## 📋 Prerequisites

Before setting up the project, ensure you have the following installed:

- **Python 3.8 or higher** (tested with Python 3.12.3)
- **pip** (Python package installer)
- **Git** (for cloning the repository)

## 🚀 Local Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/cavallofederico/statement.git
cd statement
```

### 2. Create a Virtual Environment (Recommended)

Creating a virtual environment helps isolate project dependencies:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

You have two options for installing dependencies:

#### Option A: Full Dependencies (Recommended)
Install all dependencies as specified in the original requirements:

```bash
pip install -r requirements.txt
```

#### Option B: Minimal Dependencies
If you prefer a lighter installation with only essential packages:

```bash
pip install -r requirements-minimal.txt
```

> **Note**: The minimal installation includes only the core dependencies (Streamlit, PyMuPDF, Pandas) needed for basic functionality.

### 4. Run the Application

Start the Streamlit development server:

```bash
streamlit run app.py
```

The application will open automatically in your default web browser at `http://localhost:8501`.

> **Tip**: If port 8501 is already in use, Streamlit will automatically find the next available port.

### 5. Using the Application

1. **Upload PDF**: Click on "Elegir Archivo PDF" (Choose PDF File) and select your HSBC Argentina bank statement PDF
2. **Process**: The application will automatically process the PDF and extract transaction data
3. **Download**: Click "Descargar CSV" (Download CSV) to download the converted file

## 📁 Project Structure

```
statement/
├── app.py                    # Main Streamlit application
├── transformstatement.py    # Core PDF processing and CSV conversion logic
├── requirements.txt         # Full Python dependencies
├── requirements-minimal.txt # Minimal Python dependencies (core only)
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

### File Descriptions

- **`app.py`**: Contains the Streamlit web interface, file upload handling, and user interaction logic
- **`transformstatement.py`**: Core module that processes PDF documents and extracts banking transaction data
- **`requirements.txt`**: Lists all Python package dependencies (full installation)
- **`requirements-minimal.txt`**: Lists only core dependencies for minimal installation

## 🔧 Development

### Code Structure

The application follows a simple modular structure:

1. **Frontend** (`app.py`): Streamlit interface for user interactions
2. **Backend** (`transformstatement.py`): PDF processing and data extraction logic

### Key Functions

- `transform_statement(document)`: Main function that processes PDF documents and returns CSV data
- `main()`: Streamlit application entry point with UI components

### Data Extraction

The application extracts the following fields from HSBC bank statements:

- **FECHA** (Date): Transaction date
- **REFERENCIA** (Reference): Transaction reference number
- **NRO** (Number): Transaction number
- **DEBITO** (Debit): Debit amounts
- **CREDITO** (Credit): Credit amounts
- **SALDO** (Balance): Account balance
- **DETALLE** (Details): Transaction description/details

## 🌐 Deployment

### Local Development

For local development, simply follow the setup instructions above and run:

```bash
streamlit run app.py
```

### Production Deployment

For production deployment, consider using:

- **Streamlit Cloud**: Free hosting for Streamlit apps
- **Heroku**: Platform-as-a-Service with Python support
- **Docker**: Containerized deployment

#### Example Dockerfile

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

## 🔒 Privacy & Security

- **No Data Storage**: The application does not store any uploaded files or processed data
- **Local Processing**: All PDF processing happens locally in memory
- **Secure Upload**: Files are processed temporarily and not saved to disk

## ⚠️ Important Notes

- This application is specifically designed for **HSBC Argentina** bank statements
- The PDF parsing logic is tailored to the specific format used by HSBC Argentina
- Different bank statement formats from other banks or regions may not work correctly
- Always verify the accuracy of converted data against your original statements

## 🐛 Troubleshooting

### Common Issues

1. **Import Errors**: Ensure all dependencies are installed correctly
   ```bash
   pip install -r requirements.txt
   ```

2. **PDF Not Processing**: Verify the PDF is from HSBC Argentina and not password-protected

3. **Virtual Environment Issues**: Make sure you've activated your virtual environment before installing dependencies
   ```bash
   # Activate your virtual environment first
   source venv/bin/activate  # macOS/Linux
   # OR
   venv\Scripts\activate     # Windows
   ```

4. **Port Already in Use**: If port 8501 is busy, Streamlit will automatically use the next available port

5. **Network/Installation Issues**: If you encounter timeout errors during installation, try:
   ```bash
   pip install --upgrade pip
   pip install -r requirements-minimal.txt  # Try minimal installation first
   ```

### Getting Help

If you encounter issues:

1. Check that your Python version is 3.8 or higher
2. Ensure all dependencies are properly installed
3. Verify the PDF format matches HSBC Argentina statements
4. Check the browser console for any JavaScript errors

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues or pull requests to improve the application.

## 📄 License

This project is open source. Please check the repository for license information.

## 💰 Support

If you find this tool useful, consider supporting the developer:

[![Invitame un café en cafecito.app](https://cdn.cafecito.app/imgs/buttons/button_1.png)](https://cafecito.app/cavallofederico)

---

**Created by Federico Cavallo** - Converting HSBC Argentina bank statements made easy! 🏦✨