Features Tested:
Login: Validates user login functionality with correct and incorrect credentials.
Add to Cart: Verifies that items can be added to the shopping cart successfully.
Checkout: Ensures that the checkout process works smoothly and displays the confirmation message after purchase.
Technologies Used:

Python

Selenium WebDriver

Pytest (for test execution)

Git (for version control)

Setup Instructions:

 this repository:

git clone https://github.com/your-username/selenium-testing-project.git

Navigate to the project directory:
cd selenium-testing-project

Install required dependencies:
pip install -r requirements.txt

How to Run the Tests:
After setting up, run the tests with the following command: pytest
Project Structure:
tests/: Contains all the test files.
requirements.txt: Lists all the dependencies required for the project.
README.md: Project documentation.
## Prerequisites

- Python 3.x
- pip (Python package installer)
- Chrome WebDriver (Make sure it's in your PATH)

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/selenium-project.git
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running Tests

1. You can run the tests with `pytest`:
    ```bash
    pytest tests/ -v
    ```

2. For CI integration, tests will automatically run on **push** or **pull request** via **GitHub Actions**.

## Contributing

Feel free to contribute to this project by creating pull requests.

## License

This project is licensed under the MIT License.
