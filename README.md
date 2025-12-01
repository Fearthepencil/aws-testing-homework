# Amazon Website Testing - QA Homework

## Overview
Automated and manual test suite for Amazon's product search functionality, completed as part of a QA Engineer take-home assignment for SAP Fioneer.

**Author:** Pavle Stefanovic  
**Date:** December 2025

---

## 📋 Project Structure

```
amazon-qa-homework/
├── docs/                      # HTML documentation deliverables
│   ├── index.html            # Main landing page
│   ├── test-plan.html        # Test strategy and approach (ISTQB)
│   ├── test-cases.html       # 17 test cases (BDD format)
│   ├── bug-report.html       # 3 defects with screenshots
│   ├── test-execution-report.html  # Test results summary
│   ├── test-data.html        # Test data documentation
│   └── exploratory-sessions.html   # Exploratory testing notes
├── tests/                     # Automated test suite (9 tests)
│   ├── conftest.py           # Pytest fixtures
│   ├── test_search.py        # TC-001, TC-002
│   ├── test_pagination.py    # TC-005, TC-006
│   ├── test_product_cards.py # TC-007
│   ├── test_product_detail_page.py  # TC-008
│   ├── test_price.py         # TC-009 (Pages 1-3)
│   └── test_sorting.py       # TC-010, TC-011
├── pages/                     # Page Object Model
│   ├── base_page.py
│   ├── home_page.py
│   ├── search_results_page.py
│   └── product_detail_page.py
├── utils/                     # Utilities
│   ├── price_parser.py       # Price parsing logic
│   └── logger.py             # Loguru configuration
├── test_data/                 # Test data files
│   └── search_terms.json
├── screenshots/               # Bug evidence screenshots
├── requirements.txt           # Python dependencies
├── pytest.ini                # Pytest configuration
└── README.md                 # This file
```

---

## 🚀 Setup Instructions

### Prerequisites
- Python 3.9+
- pip (Python package manager)

### Installation

1. **Navigate to project directory**
   ```bash
   cd aws-testing-homework
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Playwright browsers**
   ```bash
   playwright install chromium
   ```

---

## 🧪 Running Tests

### Run All Automated Tests
```bash
pytest tests/ -v
```

### Run Specific Test Files
```bash
pytest tests/test_search.py -v
pytest tests/test_pagination.py -v
pytest tests/test_price.py -v -s    # -s shows console output
pytest tests/test_sorting.py -v
```

### Price Calculation Output
The price calculation test (TC-009) logs average prices for pages 1-3:
```bash
pytest tests/test_price.py -v -s
```

**Sample Output:**
```
PAGE 1 - Products: 18, Average: $19.02
PAGE 2 - Products: 10, Average: $18.11
PAGE 3 - Products: 12, Average: $28.66
```

---

## 📊 Test Coverage

### Test Summary
- **Total Test Cases:** 17
- **Automated:** 9 tests (53%)
- **Manual:** 8 tests (47%)
- **Pass Rate:** 82% (14 passed, 3 failed)
- **Defects Found:** 3 bugs

### Automated Tests (9)
- ✅ TC-001: Valid product search
- ✅ TC-002: Search with multiple keywords
- ✅ TC-005: Pagination - Page 2
- ✅ TC-006: Pagination - Page 3
- ✅ TC-007: Product card information
- ✅ TC-008: Product detail page navigation
- ✅ TC-009: Calculate average price (Pages 1-3)
- ❌ TC-010: Sort by price - Low to High (BUG-001)
- ❌ TC-011: Sort by price - High to Low (BUG-001)

### Manual Tests (8)
- ✅ TC-003: Search with special characters
- ✅ TC-004: Empty search validation
- ❌ TC-012: Handle price ranges (BUG-003)
- ✅ TC-013: Results relevance check
- ✅ TC-014: Search suggestions/autocomplete
- ✅ TC-015: Very long search string
- ✅ TC-016: Search with only numbers
- ✅ TC-017: Page load performance

### Defects Found
- **BUG-001:** Price sorting not in strict order (Medium)
- **BUG-002:** Special characters return unrelated results (Low)
- **BUG-003:** Price filter shows products outside range (Medium)

---

## 📚 Documentation

Open `docs/index.html` in your browser to access all deliverables:
- Test Plan (ISTQB format)
- Test Cases (BDD Given-When-Then)
- Bug Reports (with screenshots)
- Test Execution Report
- Test Data
- Exploratory Testing Sessions

---

## 🏗️ Architecture

### Page Object Model (POM)
- **BasePage:** Common functionality (navigation, screenshots)
- **HomePage:** Search functionality
- **SearchResultsPage:** Product cards, pagination, sorting
- **ProductDetailPage:** Product details validation

### Test Organization
- **Fixtures:** Browser and page setup in `conftest.py`
- **Test Data:** Centralized in `test_data/search_terms.json`
- **Logging:** Loguru for structured logging

---

## 🔧 Troubleshooting

### Playwright browser not found
```bash
playwright install chromium
```

### Tests timeout
- Check internet connection
- Amazon may have rate limiting - tests include waits

### Locator issues
- Amazon's HTML structure may change
- Update selectors in `pages/` directory

---

## 📝 Notes

- Tests run against live Amazon.com
- Some tests may be flaky due to dynamic content
- Screenshots saved to `screenshots/` directory
- Logs saved to `test_execution.log`

---

## 📧 Contact

**Pavle Stefanovic**  
QA Engineer Candidate

---

## 📄 License

Created for educational and assessment purposes only.
