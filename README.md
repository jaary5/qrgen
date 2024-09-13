# qrgen

## Interface

![Interface-1 Screenshot](static/images/qrgen_interface.png)


## Overview

"qrgen" is a QR Code Generator Web App which is a simple yet powerful tool that allows users to generate and download QR codes for any URL they input. Built using Flask, a lightweight Python web framework.


## Technologies Used

- **HTML**: Provides the structure of the web pages.
- **CSS**: Styles the appearance of the application.
- **Python**: Serves as the primary programming language for backend development.
- **Flask**: A Python framework used to build the web application.
- **Jinja**: A templating engine used to generate dynamic HTML content.


## Features

- **QR Code Generation**: Allows users to generate a QR code for any URL they input.
- **Download Option**: Provides the ability to download the generated QR code image.


## File Descriptions

### `app.py`

This file contains the core logic of the Flask application. It defines the application's routes and handles user requests. Key functions include:

- **`index()`**: Manages both `GET` and `POST` requests at the root URL (`/`). It processes the user input to generate a QR code and renders the appropriate HTML templates.
- **`download()`**: Allows users to download the generated QR code image by serving it as an attachment.

This file also ensures that the necessary directory for storing QR codes exists and initializes the Flask application.

### `templates/index.html`

This HTML file serves as the main page where users input the URL for QR code generation. It includes:

- **Form**: An input field for the URL and a submit button. The form uses the `POST` method to send data to the server.
- **Styling Link**: Links to the external CSS file for page styling.

### `templates/result.html`

This HTML file displays the generated QR code and includes options for further actions. It contains:

- **QR Code Image**: Shows the generated QR code image using an `<img>` tag.
- **Download Link**: A link to download the QR code image.
- **Generate Another QR Code Link**: A link to return to the main page to generate a new QR code.

### `static/styles.css`

This CSS file provides the styling for the web application. It includes:

- **Container Styling**: Centers content and adds padding, background color, and box shadow to enhance the visual appeal.
- **Form Elements**: Styles the text input and buttons for a better user experience.


## Design Choices

### QR Code Generation

The `qrcode` Python library was selected for generating QR codes due to its ease of use and efficiency. It provides a simple interface for creating QR codes and integrates seamlessly with Flask.

### File Organization

The project is structured to maintain clarity and manageability:

- **`app.py`**: Contains application logic.
- **`templates/`**: Holds HTML templates for rendering views.
- **`static/`**: Stores static assets such as CSS files.

This MVC(Model-View-Controller) implementation ensures that the application is easy to develop and maintain.

### User Interface Design

The UI is designed to be simple and responsive:

- **Simple Form**: Provides a straightforward method for users to input URLs.
- **Responsive Layout**: Ensures the application is accessible and usable on various devices.


## Requirements

- Python 3.x
- Flask
- qrcode
- Pillow (PIL Fork)


## Installation

1. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Navigate to the project root directory**:
   ```bash
   cd ..
   ```

2. **Run the Flask application**:
   ```bash
   python app.py
   ```

3. **Open your web browser and go to http://127.0.0.1:5000/ to use the QR code generator**.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
