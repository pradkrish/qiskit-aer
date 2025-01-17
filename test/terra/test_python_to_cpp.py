# This code is part of Qiskit.
#
# (C) Copyright IBM 2018, 2019.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

import unittest
import numpy as np
from qiskit_aer.pulse.controllers.test_python_to_cpp import \
    test_py_list_to_cpp_vec, test_py_list_of_lists_to_cpp_vector_of_vectors,\
    test_py_dict_string_numeric_to_cpp_map_string_numeric,\
    test_py_dict_string_list_of_list_of_doubles_to_cpp_map_string_vec_of_vecs_of_doubles,\
    test_np_array_of_doubles, test_np_2D_array_of_doubles, test_evaluate_hamiltonians,\
    test_py_ordered_map

from .common import QiskitAerTestCase


class TestPythonToCpp(QiskitAerTestCase):
    """ Test Pyhton C API wrappers we have for dealing with Python data structures
        in C++ code. """
    def test_py_list_to_cpp_vec(self):
        arg = [1., 2., 3.]
        self.assertTrue(test_py_list_to_cpp_vec(arg))

    def test_py_list_of_lists_to_cpp_vector_of_vectors(self):
        arg = [[1., 2., 3.]]
        self.assertTrue(test_py_list_of_lists_to_cpp_vector_of_vectors(arg))

    def test_py_dict_string_numeric_to_cpp_map_string_numeric(self):
        arg = {"key": 1}
        self.assertTrue(test_py_dict_string_numeric_to_cpp_map_string_numeric(arg))

    def test_py_dict_string_list_of_list_of_doubles_to_cpp_map_string_vec_of_vecs_of_doubles(self):
        arg = {"key": [[1., 2., 3.]]}
        self.assertTrue(test_py_dict_string_list_of_list_of_doubles_to_cpp_map_string_vec_of_vecs_of_doubles(arg))

    def test_np_array_of_doubles(self):
        arg = np.array([0., 1., 2., 3.])
        self.assertTrue(test_np_array_of_doubles(arg))

    def test_np_2D_array_of_doubles(self):
        arg = np.array([[0., 1., 2., 3.], [10., 20., 30., 40.]])
        self.assertTrue(test_np_2D_array_of_doubles(arg))

    def test_evaluate_hamiltonians(self):
        """ TODO: Evaluate different hamiltoninan expressions?"""
        self.assertEqual(True, True)

    def test_py_ordered_map(self):
        # Since Python 3.6 dict insertion order is guaranted
        arg = {"D0": 1, "U0": 2, "D1": 3, "U1": 4}
        self.assertTrue(test_py_ordered_map(arg))
