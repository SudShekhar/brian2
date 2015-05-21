xcopy /e "%RECIPE_DIR%\..\..\brian2" "%SRC_DIR%"
xcopy "%RECIPE_DIR%\..\..\setup.py" "%SRC_DIR%"
"%PYTHON%" setup.py install --with-cython --fail-on-error
if errorlevel 1 exit 1