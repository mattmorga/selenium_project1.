# README.md
# Selenium Testing Project

This is a simple Selenium testing project for practicing automation testing using Python and Selenium WebDriver. The tests interact with the SauceDemo website to validate basic features like login, add to cart, and checkout.

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
