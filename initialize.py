import os
from datetime import datetime
import json

# Create .gitignore file
gitignore_content = """
__pycache__/
*.pyc
*.pyo
*.pyd
*.env
"""

with open(".gitignore", "w") as gitignore_file:
    gitignore_file.write(gitignore_content)

# Create .env_template file
env_template_content = """
# Rename this file to .env and fill in the values

API_KEY=your_api_key_here
"""

with open(".env_template", "w") as env_template_file:
    env_template_file.write(env_template_content)

# Create config.py file
config_content = """
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
"""

with open("config.py", "w") as config_file:
    config_file.write(config_content)

# Update README.md file
readme_update = """
## Setup

1. Clone this repository.
2. Rename the `.env_template` file to `.env` and fill in the required values.
3. Install the dependencies: `pip install -r requirements.txt` (if you have a requirements file).
4. Run your project.

For more examples and use cases, visit our [blog](https://www.openagilesolutions.com/blog).
"""

if os.path.exists("README.md"):
    with open("README.md", "a") as readme_file:
        readme_file.write(readme_update)
else:
    with open("README.md", "w") as readme_file:
        readme_file.write(readme_update)

# Create MIT LICENSE file
current_year = datetime.now().year
license_content = f"""
MIT License

Copyright (c) {current_year} Open Agile Solutions

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

with open("LICENSE", "w") as license_file:
    license_file.write(license_content)

# Create CONTRIBUTING.md file
contributing_content = """
# Contributing Guidelines

Thank you for your interest in contributing to this project! All contributions are welcome, including bug reports, feature requests, and code contributions.

## Reporting Issues

- Please use the GitHub issue tracker to report any issues or bugs.
- Include as much detail as possible, including steps to reproduce the issue.

## Submitting Pull Requests

- Fork the repository and create a new branch for your changes.
- Ensure that your code follows the project's coding style and conventions.
- Include tests for any new features or bug fixes.
- Update the documentation
"""

with open("CONTRIBUTING.md", "w") as contributing_file:
    contributing_file.write(contributing_content)
