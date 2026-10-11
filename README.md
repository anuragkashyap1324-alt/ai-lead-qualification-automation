# AI Lead Qualification & Sales Automation

## Project Overview
A Python-based demonstration that validates customer lead data, checks AI-generated analysis, applies business rules to determine the next action, and handles simulated CRM failures.

## Problem
Businesses can waste time manually reviewing customer leads and deciding which prospects need immediate attention. Incorrect or incomplete data can also disrupt follow-up workflows.

## Features
- Validates required lead fields and input values.
- Uses JSON to store structured lead data.
- Validates AI-analysis fields, including priority and confidence score.
- Applies business rules to recommend sales follow-up actions.
- Simulates CRM retries when an operation fails.
- Stores failed records for later review.

## Technology Stack
- Python
- JSON
- Python functions and exception handling
- AI workflow design and structured-response validation

## Project Files
- `main.py` — Lead validation, response validation, decision rules, and simulated failure handling.
- `fields.json` — Sample customer lead input.

## How to Run
1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

   ```bash
   python main.py
   ```

## Current Limitations
This is a learning and portfolio demonstration. AI responses and CRM behavior are simulated; a live AI API, production CRM integration, and deployed webhook are not included in this version.

## Future Improvements
- Integrate a real AI API with secure environment-variable handling.
- Connect to a CRM through an API.
- Add automated tests.
- Implement a webhook endpoint for incoming leads.

## Author
Anurag Kashyap