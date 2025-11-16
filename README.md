
### Key Features:
- **Playwright :** Fast, cross-browser automation (Chromium, WebKit, Firefox).
- **Behave (BDD):** Gherkin-based syntax for defining tests.
- **Page Object Model (POM):** Encapsulation of page-specific actions.
- **Base Page:** Shared methods like `select_dropdown`, and `select_radio_button`.
- **Screenshots:** Captured on every step (if enabled) and at the end of scenarios.
- **Multi-Environment Support:** Multiple environments defined in `behave.ini`.
- **CI/CD Integration:** GitHub Actions pipeline for automated execution.

## Framework Structure

```plaintext
project-root/
├── features/                # Feature files (BDD scenarios)
│   ├── pages/               # Page Object files (BasePage, LoginPage, etc.)
│   ├── steps/               # Step definition files
│   ├── environment.py       # Hooks for setup and teardown
│   └── *.feature            # Feature files with scenarios
├── screenshots/             # Screenshots captured during tests
├── traces/                  # Playwright trace sessions (zip files)
├── behave.ini               # Configurations for different environments
├── requirements.txt         # Dependencies
└── README.md                # Project documentation
```
```

## Setup and Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/manivannanpannerselvam/E-commerce-workflows.git
   cd playwright-python-framework
   ```

2. **Create and activate a Python virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   python -m playwright install  # Install Playwright browsers
   ```

## Configuration

- **behave.ini:** This file defines environment configurations such as base URLs, API URLs, and browser types for different environments (e.g., `sit`, `uat`). Update it with your environment-specific details.

Example `behave.ini`:

```ini
[behave:sit]
baseUrl = https://sit.example.com
apiUrl = https://api.sit.example.com
browserType = chrome

[behave:uat]
baseUrl = https://uat.example.com
apiUrl = https://api.uat.example.com
browserType = webkit
```

- **Environment Profiles:** Set the environment at runtime by passing the profile flag:
  ```bash
  behave -D profile=uat
  ```

## Running Tests

### **Run All Tests:**
```bash
behave
```

### **Run Tests for Specific Profile:**
```bash
behave -D profile=uat
```

### **Run Debug Tests:**
To run tests in debug mode, use the `--no-capture` option to view the output in real-time:
```bash
behave --no-capture
```

### **Run a Specific Feature File:**
To run tests from a specific feature file, provide the path to the file:
```bash
behave features/login.feature
```

### **Run Tests with Specific Tags:**
```bash
behave --tags @smoke
```

### **Run Tests for a Specific Scenario:**
```bash
behave --name "New User Registration"
```
### **Run Tests with Video Recording:**

To enable video recording for your tests, ensure the `record_video` option is set in your configuration

```bash
behave -D record_video=true
```

The recorded videos will be saved in the `videos/` directory for each scenario. These videos can be used for debugging and reviewing test execution.

### **Capture Screenshot on Every Step:**
To enable screenshots on every step, pass the `screenshot_on_step` option during test execution:

```bash
behave -D screenshot_on_step=true
```

The screenshots will be saved in the `screenshots/` directory for each step. These can be used for debugging and reporting purposes.
