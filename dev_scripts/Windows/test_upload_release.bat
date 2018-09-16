title Upload Release to Test PYPI

twine upload --repository-url https://test.pypi.org/legacy/ %1

rem To install smart-string from the test PYPI:
rem pip install -U --index-url https://test.pypi.org/simple/ smart-string

rem To install smart-string from the test PYPI, and the dependencies from the production PYPI:
rem pip install -U --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple smart-string
