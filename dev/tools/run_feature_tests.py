from brian2 import *
from brian2.tests.features import *
from brian2.tests.features.base import *

# Full testing
print run_feature_tests().tables_and_exceptions

# Quick testing
#print run_feature_tests(configurations=[DefaultConfiguration,
#                                    WeaveConfiguration]).tables_and_exceptions

# Specific testing
#from brian2.tests.features.synapses import SynapsesSTDP, SynapsesPost
#print run_feature_tests(feature_tests=[SynapsesPost]).tables_and_exceptions
#print run_feature_tests(feature_tests=[SynapsesPost],
#                        configurations=[DefaultConfiguration,
#                                        WeaveConfiguration]).exceptions
