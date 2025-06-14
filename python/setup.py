# python/setup.py
from setuptools import setup, find_packages

setup(
    name="mlc-llm",
    version="0.1.0",
    description="Python package for MLC LLM runtime",
    packages=find_packages(include=["mlc_llm", "mlc_llm.*"]),
    package_data={"mlc_llm": ["frontend/*"]},
    include_package_data=True,
    install_requires=[
        "fastapi",
        "uvicorn[standard]",
        "pytest",
        "requests",
        "httpx<0.26",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "mlc_llm=mlc_llm.cli:main",
        ],
    },
)
