
```markdown
# Naivas E-Commerce Automation Test

An automated end-to-end (E2E) testing suite for the Naivas demo e-commerce platform. This project implements the **Page Object Model (POM)** pattern using **Python** and **Playwright**.

## Features
- **Purchase Journey:** Automates adding items (Hoodie, Shoes) to the cart and proceeding to checkout.
- **Page Object Model:** Separates UI locators from test logic for easy maintenance.
- **Automated Reporting:** Generates screenshots and Playwright traces on failure.
- **Cross-Browser:** Configured to run on Chromium (Chrome/Edge), Firefox, and WebKit (Safari).

## Tech Stack
- **Language:** Python 3.12+
- **Framework:** Pytest
- **Automation Tool:** Playwright
- **Pattern:** Page Object Model (POM)

## Installation

**Clone the repo:**
   ```bash
   git clone [https://github.com/yourusername/naivas_demo_test.git](https://github.com/yourusername/naivas_demo_test.git)
   cd naivas_demo_test
   ```

**Set up a Virtual Environment:**
   ```bash
   python3 -m venv naivas_env
   source naivas_env/bin/activate
   ```

**Install Dependencies:**
   ```bash
   pip install pytest-playwright
   playwright install chromium
   ```

## Running Tests

### Run in Headed Mode (Watch the browser)
```bash
python -m pytest --headed --slowmo 1000
```

### Generate a Trace on Failure
```bash
python -m pytest --tracing retain-on-failure
```

### View Results & Screenshots
Screenshots are saved in the `/test-results` directory upon successful completion or failure.

```
