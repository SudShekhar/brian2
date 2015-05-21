#!/bin/bash
cp -r $RECIPE_DIR/../../brian2 $SRC_DIR
cp $RECIPE_DIR/../../setup.py $SRC_DIR
$PYTHON setup.py install --with-cython --fail-on-error
