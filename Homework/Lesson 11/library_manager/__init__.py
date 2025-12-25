# package_name/__init__.py
__all__ = ["catalog", "report"]

from .catalog import Library
from .report import generate_report

print("Main package initialized")
