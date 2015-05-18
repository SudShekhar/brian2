#!/bin/bash
cp -r $RECIPE_DIR/.. $SRC_DIR
$PYTHON setup.py install --with-cython

