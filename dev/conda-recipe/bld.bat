xcopy /e "%RECIPE_DIR%\..\.." "%SRC_DIR%"
"%PYTHON%" setup.py install --with-cython
if errorlevel 1 exit 1