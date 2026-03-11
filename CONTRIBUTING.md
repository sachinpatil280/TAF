# Contributing to Test Automation Framework

Thank you for considering contributing to TAF! 🎉

## How to Contribute

### Reporting Bugs
- Use the GitHub Issues tab
- Describe the bug clearly with steps to reproduce
- Include your environment (OS, Python version, browser version)
- Add relevant logs or screenshots

### Suggesting Features
- Open an issue with the "enhancement" label
- Explain the use case and expected behavior
- Provide examples if possible

### Submitting Code Changes

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**
   - Follow existing code style
   - Add tests for new features
   - Update documentation if needed
4. **Test your changes**
   ```bash
   cd test_cases
   python -m pytest -v
   ```
5. **Commit with clear messages**
   ```bash
   git commit -m "Add: feature description"
   ```
6. **Push and create a Pull Request**
   ```bash
   git push origin feature/your-feature-name
   ```

## Code Style Guidelines
- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings to classes and methods
- Keep functions focused and testable

## Testing Requirements
- All new features must include tests
- Ensure all existing tests pass
- Run both UI and API test suites

## Questions?
Open an issue or reach out to the maintainers.

Thank you for contributing! 🚀
