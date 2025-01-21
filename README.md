# Wseiz University Application System

Welcome to the **Wseiz University Application System**! This application allows prospective students to submit their university applications for different departments. The system provides a simple graphical user interface (GUI) to enter personal details and select the department. After submission, it processes the application and simulates whether the application is accepted or rejected.

## Features

- **User Interface**: A clean and simple GUI using the **Tkinter** library in Python, allowing easy interaction with the application system.
- **Application Submission**: Applicants can fill in their full name, email, date of birth, and select a department for application submission.
- **Validation**: The system validates input fields to ensure data integrity, such as checking the name length, valid email format, and age requirement (18+).
- **Processing**: Once submitted, the system simulates processing by sending the application to the university, which can either accept or reject the application.
- **Feedback**: The system provides feedback to users on their application's status (Accepted or Rejected).

## How it Works

### Step 1: Submit Your Application
- **Full Name**: The user enters their full name.
- **Email**: The user provides their email address (ensured to be valid).
- **Date of Birth**: The system requires the user to enter their birthdate in the format `YYYY-MM-DD`. The applicant must be at least 18 years old to apply.
- **Department**: Choose the department for your application. Departments include **Computer Science**, **Business Administration**, **Psychology**, **Management**, and **Engineering**.

Once all fields are filled out correctly, the applicant can click the "Submit Application" button to send their details for processing.

### Step 2: Application Processing
Once the application is submitted, the system simulates the processing delay (to mimic real-world application handling) and randomly determines whether the application will be accepted or rejected.

### Step 3: Receive Feedback
After processing, the system outputs the result (Accepted or Rejected) in the text area. It shows the status of the application along with the university's response.

## Getting Started

To get started with the application, follow these steps:

1. **Clone the Repository**: Download or clone this repository to your local machine.
2. **Install Dependencies**:
   - Make sure you have Python 3.x installed.
   - The application uses the `tkinter` library for the GUI, which is usually included with Python. If not, you can install it using the following command:
     ```bash
     pip install tk
     ```
3. **Run the Application**:
   - Open a terminal or command prompt.
   - Navigate to the directory where the Python file is located.
   - Run the application by executing the following command:
     ```bash
     python application_system.py
     ```

4. **Start Using the System**:
   - Fill in the application form.
   - Submit your application and wait for the result!

## Code Structure

Here’s a brief explanation of the key parts of the code:

### 1. **Event Classes**
   - These represent different application events:
     - `ApplicationSentEvent`: This event is triggered when the applicant submits their application.
     - `ApplicationRejectedEvent`: This event is triggered if the university rejects the application.
     - `ApplicationAcceptedEvent`: This event is triggered if the university accepts the application.

### 2. **University Class**
   - This class simulates a university that processes applications.
   - It receives an `ApplicationSentEvent` and handles it by either accepting or rejecting the application randomly.

### 3. **Application System UI**
   - This class builds the user interface using Tkinter.
   - It validates the inputs (name, email, date of birth) and ensures the correct data is provided before submission.
   - Once the user submits the form, it triggers the application processing logic and provides feedback on whether the application was accepted or rejected.

## Contribution

We welcome contributions! If you want to improve the application or fix any issues, feel free to fork the repository, make your changes, and create a pull request. 

Here are some ways you can help:
- Improving the user interface
- Adding more departments or features
- Enhancing the application feedback logic

## License

This project is open-source and is available under the MIT License. You can freely use, modify, and distribute the code as you wish.

---

We hope you enjoy using the **Wseiz University Application System**. It’s designed to simulate the real-world application process with a little fun and randomness added to the experience. If you have any questions, feel free to reach out to the project maintainers.

Happy applying! 🎓


Also if you want to read my new blog about "Unlocking the Power of Event-Driven Programming: Revolutionizing Modern Software Development" 
You can find in this link; https://medium.com/@cankoksal0506/unlocking-the-power-of-event-driven-programming-revolutionizing-modern-software-development-68ba5229464a
