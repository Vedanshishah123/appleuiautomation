# Apple UI Automation Framework

A beginner-friendly, real-world UI automation framework for guest user journeys on [apple.com](https://www.apple.com).

## Tech Stack

- Python
- Playwright
- PyTest
- Page Object Model
- python-dotenv
- Allure Reports

## Project Structure

```
apple_ui_framework/
├── .env
├── conftest.py
├── pytest.ini
├── requirements.txt
├── config/
│   └── settings.py
├── pages/
│   ├── base_page.py
│   ├── home_page.py
│   ├── iphone_page.py
│   ├── mac_page.py
│   ├── search_page.py
│   └── store_page.py
└── tests/
    └── test_guest_user_journeys.py
```

## Setup

```bash
git clone https://github.com/vik175-m/appleuiautomation.git
cd appleuiautomation/apple_ui_framework

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
playwright install
```

## Configuration

Create a `.env` file in `apple_ui_framework/`:

```env
BASE_URL=https://www.apple.com/in
BROWSER=chromium
HEADLESS=false
SLOW_MO=500
DEFAULT_TIMEOUT=15000
```

## Run Tests

```bash
pytest
```

Run with Allure report:

```bash
pytest --alluredir=allure-results
allure serve allure-results
```

## Test Coverage (11 tests)

| Test | Description |
|---|---|
| `test_homepage_validation` | Validates homepage loads with title and logo |
| `test_navigation_menu_has_multiple_links` | Counts nav links |
| `test_hover_over_mac_navigation` | Hover behavior on Mac nav |
| `test_store_page_navigation_and_dropdown_style_links` | Store page shopping links |
| `test_search_functionality_for_iphone` | Search with keyboard Enter |
| `test_keyboard_actions_clear_search_field` | Meta+A and Backspace shortcuts |
| `test_scroll_to_footer_and_validate_footer` | Scroll and footer visibility |
| `test_open_support_link_in_new_tab` | New tab/popup handling |
| `test_mac_and_iphone_buy_button_validation` | Buy button on product pages |
| `test_mobile_menu_validation` | Responsive viewport test |
| `test_negative_search_does_not_break_page` | Graceful invalid search handling |
