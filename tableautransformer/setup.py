import setuptools

with open("README.md", "r") as fh:
	description = fh.read()

setuptools.setup(
	name="tableautransformer",
	version="0.0.30",
	author="Josh Teixeira",
	author_email="jteixeira@cppib.com",
	packages=["tableautransformer"],
	description="ETL tooling for tableau seed data",
	long_description=description,
	long_description_content_type="text/markdown",
	url="https://pypi.org/project/tableautransformer",
	license='MIT',
	python_requires='>=3.6',
	install_requires=[]
)

