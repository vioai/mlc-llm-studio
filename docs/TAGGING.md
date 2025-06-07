# Release Tagging Guidelines

This project uses Git tags to mark stable releases of the Docker image and Python package.

- Tags follow the format `v<major>.<minor>.<patch>`.
- Create a new tag whenever you publish a release build.
- Push tags to GitHub so that CI can build and upload artifacts.

Example:

```bash
git tag v1.2.0
git push origin v1.2.0
```

