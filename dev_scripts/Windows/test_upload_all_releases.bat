title Upload all Releases to Test PYPI

twine upload --repository-url https://test.pypi.org/legacy/ dist/*

rem To install smart-string from the test PYPI:
rem pip install -U --index-url https://test.pypi.org/simple/ smart-string

rem To install smart-string from the test PYPI, and the dependencies from the production PYPI:
rem pip install -U --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple smart-string
