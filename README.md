# Amazon Website Testing - QA Homework

## Overview
This project contains automated and manual test cases for Amazon's product search functionality, completed as part of a QA Engineer take-home assignment.

## Author
**Candidate**: [Your Name]  
**Position**: QA Engineer - SAP Fioneer  
**Date**: November 2024

---

## 📋 Project Structure

```
amazon-qa-homework/
├── docs/                      # HTML documentation deliverables
│   ├── index.html            # Main landing page
│   ├── test-plan.html        # Test strategy and approach
│   ├── test-cases.html       # Detailed test cases (BDD format)
│   ├── bug-report.html       # Defects found during testing
│   ├── test-data.html        # Test data documentation
│   └── exploratory-sessions.html
├── tests/                     # Automated test suite
│   ├── test_search.py        # Search functionality tests
│   ├── test_pagination.py    # Pagination tests
│   └── test_price_calculation.py  # Price averaging tests
├── pages/                     # Page Object Model
│   ├── base_page.py
│   ├── home_page.py
│   ├── search_results_page.py
│   └── product_detail_page.py
├── utils/                     # Utilities
│   ├── price_calculator.py   # Price calculation logic
│   └── logger.py             # Logging configuration
├── test_data/                 # Test data files
│   └── search_terms.json
├── screenshots/               # Test execution screenshots
├── requirements.txt           # Python dependencies
├── pytest.ini                # Pytest configuration
└── README.md                 # This file
```

---

## 🚀 Setup Instructions

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)
- Chrome browser (latest version)

### Installation

1. **Clone or extract the project**
   ```bash
   cd amazon-qa-homework
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers**
   ```bash
   playwright install chromium
   ```

---

## 🧪 Running Tests

### Run All Automated Tests
```bash
pytest tests/ -v
```

### Run Specific Test Categories

**Search functionality tests:**
```bash
pytest tests/test_search.py -v
```

**Pagination tests:**
```bash
pytest tests/test_pagination.py -v
```

**Price calculation tests (with console output):**
```bash
pytest tests/test_price_calculation.py -v -s
```

### Run Tests by Marker

**Smoke tests only:**
```bash
pytest -m smoke -v
```

**Price calculation tests:**
```bash
pytest -m price_calculation -v -s
```

### Generate HTML Report
```bash
pytest tests/ -v --html=test-report.html --self-contained-html
```

---

## 📊 Test Coverage

### Automated Tests (10 tests)
- ✅ TC-001: Valid product search returns results
- ✅ TC-002: Search with multiple keywords
- ✅ TC-005: Navigate to page 2
- ✅ TC-006: Navigate to page 3
- ✅ TC-007: Product card displays required information
- ✅ TC-008: Click product opens detail page
- ✅ TC-009: Calculate average price - Page 1
- ✅ TC-010: Calculate average price - Page 2
- ✅ TC-011: Calculate average price - Page 3
- ✅ TC-012: Combined average across all pages

### Manual Tests (8 tests)
- 🔍 TC-003: Search with special characters
- 🔍 TC-004: Empty search validation
- 🔍 TC-013: Handle price ranges visually
- 🔍 TC-014: Results relevance check
- 🔍 TC-018: Search suggestions/autocomplete
- 🔍 TC-019: Very long search string
- 🔍 TC-020: Search with only numbers
- 🔍 TC-021: Page load performance

### Exploratory Testing Sessions
- 📝 Session 01: Search behavior exploration (60 min)
- 📝 Session 02: Results page deep dive (45 min)
- 📝 Session 03: Price display variations (30 min)

---

## 📈 Price Calculation Feature

The automated tests calculate and log average product prices for the first 3 pages of search results, as required by the homework task.

**To see price calculations in console:**
```bash
pytest tests/test_price_calculation.py::test_calculate_all_three_pages_combined -v -s
```

**Sample Output:**
```
============================================================
COMBINED PRICE SUMMARY - ALL 3 PAGES
============================================================
Search term: 'wireless mouse'
Total products analyzed: 48

Page 1 - Products: 16, Avg: $24.99
Page 2 - Products: 16, Avg: $26.50
Page 3 - Products: 16, Avg: $25.75

OVERALL AVERAGE PRICE: $25.75
Lowest price found: $9.99
Highest price found: $89.99
============================================================
```

---

## 📚 Documentation

All deliverables are available in the `docs/` folder:

- **index.html** - Main landing page with links to all documents
- **test-plan.html** - Comprehensive test plan following ISTQB standards
- **test-cases.html** - All test cases in BDD Given-When-Then format
- **bug-report.html** - Defects discovered during testing
- **test-data.html** - Test data used for testing
- **exploratory-sessions.html** - Notes from exploratory testing

**To view documentation:**
1. Open `docs/index.html` in your browser
2. Navigate through linked documents

---

## 🏗️ Architecture

### Page Object Model (POM)
The project uses the Page Object Model pattern for maintainability:
- Each page has its own class with locators and methods
- Base page provides common functionality
- Tests interact with pages, not raw selectors

### Test Organization
- **Fixtures**: Defined in `tests/conftest.py`
- **Utilities**: Shared logic in `utils/`
- **Test Data**: Centralized in `test_data/`

### Logging
- Console logs: INFO level
- File logs: DEBUG level (`test_execution.log`)
- Price calculations: Logged to console as required

---

## 🐛 Known Issues

See `docs/bug-report.html` for detailed bug reports discovered during testing.

---

## 🔧 Troubleshooting

### Tests fail with timeout errors
- Increase timeout in `tests/conftest.py`
- Check internet connection
- Amazon may have rate limiting - add delays between tests

### Playwright browser not found
```bash
playwright install chromium
```

### Price extraction fails
- Amazon's HTML structure may change
- Check locators in `pages/search_results_page.py`
- Some products may not have prices displayed

---

## 📝 Notes

- Tests are designed to run against the live Amazon.com website
- Amazon's layout may change, requiring locator updates
- Some tests may be flaky due to dynamic content and ads
- Price calculations exclude sponsored products when possible

---

## 📧 Contact

For questions about this project, please contact:
- **Email**: [your.email@example.com]
- **LinkedIn**: [Your LinkedIn Profile]

---

## 📄 License

This project is created for educational and assessment purposes only.

