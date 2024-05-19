# MyTomorrows
## Disclaimer
This repo contains the code for the MyTomorrows assignment. The code is written in Python and Playwright + Pytest.
There is a single test case that tests the functionality of the MyTomorrows website. The test case is written in the file `test_sign_up.py` and is located in the `tests` directory. In `.github/workflows` there is a GitHub Actions workflow that runs the tests on every push to the repository, and publish Allure reports to GitHub Pages: https://maksimkravchuk.github.io/MyTomorrows/
## Installation
1. Clone the repository
2. Install the requirements
```bash
pip install -r requirements.txt
playwright install
```
3. Run the tests
```bash
pytest
```