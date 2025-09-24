# Terraform-File-Generator-Application

## Overview
This web application allows users to input resource specifications (like VMs, Storage, Networks) and view the corresponding Terraform configuration code generated from predefined templates. Users can view and copy the generated code, ensuring that the syntax is correct.

## Features
- Simple HTML form to collect resource specifications (resource type, CPU, RAM, disk size, etc.)
- JavaScript frontend to handle form submission and display results
- Flask backend with `/generate` endpoint to process user input and return generated Terraform code
- Predefined Terraform templates for VM, Storage, and Network
- Template generation logic using Python string formatting
- Display of generated Terraform code in a code block with syntax highlighting (Prism.js)
- Copy-to-clipboard feature for easy code copying

## Setup Instructions

### Backend
1. Navigate to the `backend` directory:
	```bash
	cd backend
	```
2. Install dependencies:
	```bash
	pip install -r requirements.txt
	```
3. Run the Flask server:
	```bash
	python app.py
	```

### Frontend
No build step is required. The Flask backend serves the frontend files automatically.

## Usage
1. Open your browser and go to `http://localhost:5000`.
2. Fill out the form with your desired resource specifications (resource type, CPU, RAM, disk size).
3. Click "Generate Terraform Code".
4. The generated Terraform configuration will be displayed in a code block with syntax highlighting.
5. Click "Copy to Clipboard" to copy the code for use.

## Project Structure
```
backend/
  app.py
  requirements.txt
  static/
  templates/
frontend/
  index.html
  app.js
```

## Technologies Used
- Python 3, Flask, Jinja2
- HTML, CSS, JavaScript
- Prism.js for syntax highlighting

## Next Steps
- Add downloadable .tf file option
- Add more resource templates and validation

