# README

## Pre-commit Hook Installation

Before pushing any changes to the repository, it's necessary to install the pre-commit hook. This hook ensures that certain checks are performed automatically before committing changes, helping to maintain code quality and consistency.

To install the pre-commit hook, follow these steps:

1. Ensure you have the necessary permissions to install hooks in the repository.

2. Navigate to the root directory of the repository in your terminal.

3. Run the following command to install the pre-commit hook:

    ```bash
    pre-commit install
    ```

4. Once installed, the pre-commit hook will run automatically before each commit. If any issues are detected during the checks, you will need to address them before proceeding with the commit.

By enforcing these checks before commits are made, we aim to keep our codebase clean, consistent, and free of common issues.

For more information about pre-commit hooks, visit: [pre-commit.com](https://pre-commit.com/)
