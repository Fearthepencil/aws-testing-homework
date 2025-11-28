Homework task QA: Amazon Website Testing

DELIVERABLES
1. Test Plan including scope, objectives, and strategy for Amazon search flow.
2. Test Cases covering search, pagination, product detail verification, and usability checks.
3. Bug Report template with any identified defects.
4. Test Data with sample search terms, filters, and edge inputs.
5. Automated Playwright suite that searches, validates product cards, and logs average prices for first three pages.

TEST SCOPE
- Product search functionality and result accuracy.
- Search result page consistency across the first three pagination pages.

TEST OBJECTIVES
- Validate successful searches and accurate product information display.
- Identify usability issues, data discrepancies, and risk areas.
- Compute and log average product price per results page for pages 1–3.

TEST STRATEGY
- Functional testing of the search workflow and pagination.
- Usability checks for clarity of CTAs and product data presentation.
- Exploratory testing to catch edge-case behaviors, with Chrome as the primary browser.

AUTOMATION
- Use Playwright with Chrome to implement the scripted scenarios (scrape prices, assert key elements, navigate pages).
- Calculate per-page averages from the first three pages and write them to the console.

SUBMISSION
- Zip the plan, cases, bug report, test data, and Playwright project.
- Email to Valentina, Kristina, and Andjelka with subject “<Your Name> - QA Homework Task.”