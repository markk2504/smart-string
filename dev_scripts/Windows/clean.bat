title Clean

del *.pyc /s /f /q

rd .pytest_cache /s /q
rd smart_str\tests\__pycache__ /s /q

del build\* /s /f /q
for /d %%x in (build\*) do @rd "%%x" /s /q

del /s /f /q dist\*
for /d %%x in (dist\*) do @rd "%%x" /s /q

del /s /f /q smart_string.egg-info\*
for /d %%x in (smart_string.egg-info\*) do @rd "%%x" /s /q
