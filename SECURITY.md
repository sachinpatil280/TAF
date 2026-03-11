# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| Latest  | :white_check_mark: |

## Reporting a Vulnerability

We take security seriously. If you discover a security vulnerability, please follow these steps:

1. **Do NOT** open a public issue
2. Email the maintainers directly at [sachin.patil280@gmail.com] with:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

3. Allow up to 48 hours for an initial response
4. We will work with you to understand and address the issue

## Security Best Practices

When using this framework:
- Keep dependencies updated: `pip install -r resources/requirements.txt --upgrade`
- Use environment variables for sensitive data (API keys, credentials)
- Never commit credentials or sensitive data to the repository
- Enable SSL verification in API tests when testing production systems
- Use the latest Python version compatible with the framework

Thank you for helping keep TAF secure! 🔒
