from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in rides_management/__init__.py
from rides_management import __version__ as version

setup(
	name="rides_management",
	version=version,
	description="Managing Rides",
	author="Hussain",
	author_email="hussain@frappe.io",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
