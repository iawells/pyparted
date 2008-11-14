#!/usr/bin/python
# 
# Test cases for the methods in the _ped module itself - just the pyunit
# and pynatmath files.
#
# Copyright (C) 2008  Red Hat, Inc.
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions of
# the GNU General Public License v.2, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY expressed or implied, including the implied warranties of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.  You should have received a copy of the
# GNU General Public License along with this program; if not, write to the
# Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.  Any Red Hat trademarks that are incorporated in the
# source code or documentation are not subject to the GNU General Public
# License and may only be used or replicated with the express permission of
# Red Hat, Inc.
#
# Red Hat Author(s): Chris Lumens <clumens@redhat.com>
#
import _ped
import unittest

# One class per method, multiple tests per class.  For these simple methods,
# that seems like good organization.  More complicated methods may require
# multiple classes and their own test suite.
class GreatestCommonDivisorTestCase(unittest.TestCase):
    def runTest(self):
        # Can't test cases where we pass a negative to greatest_common_divisor
        # because libparted will assert() on those and we'll abort.
        self.assertEqual(_ped.greatest_common_divisor(40, 0), 40)
        self.assertEqual(_ped.greatest_common_divisor(0, 40), 40)
        self.assertEqual(_ped.greatest_common_divisor(40, 10), 10)
        self.assertEqual(_ped.greatest_common_divisor(47, 19), 1)

class DivRoundToNearestTestCase(unittest.TestCase):
    def runTest(self):
        self.assertEqual(_ped.div_round_to_nearest(0, 100), 0)
        self.assertEqual(_ped.div_round_to_nearest(100, 5), 20)
        self.assertEqual(_ped.div_round_to_nearest(100, 6), 17)
        self.assertRaises(ZeroDivisionError, _ped.div_round_to_nearest, 100, 0)

class DivRoundUpTestCase(unittest.TestCase):
    def runTest(self):
        self.assertEqual(_ped.div_round_up(0, 100), 0)
        self.assertEqual(_ped.div_round_to_nearest(100, 5), 20)
        self.assertEqual(_ped.div_round_to_nearest(100, 6), 17)
        self.assertRaises(ZeroDivisionError, _ped.div_round_up, 100, 0)

class RoundDownToTestCase(unittest.TestCase):
    def runTest(self):
        self.assertEqual(_ped.round_down_to(0, 100), 0)
        self.assertEqual(_ped.round_down_to(100, 17), 85)
        self.assertEqual(_ped.round_down_to(100, -17), 85)
        self.assertRaises(ZeroDivisionError, _ped.round_down_to, 100, 0)

class RoundToNearestTestCase(unittest.TestCase):
    def runTest(self):
        self.assertEqual(_ped.round_to_nearest(0, 100), 0)
        self.assertEqual(_ped.round_to_nearest(100, 17), 102)
        self.assertEqual(_ped.round_to_nearest(100, -17), 68)
        self.assertRaises(ZeroDivisionError, _ped.round_to_nearest, 100, 0)

class RoundUpToTestCase(unittest.TestCase):
    def runTest(self):
        self.assertEqual(_ped.round_to_nearest(0, 100), 0)
        self.assertEqual(_ped.round_up_to(100, 17), 102)
        self.assertEqual(_ped.round_up_to(100, -17), 68)
        self.assertRaises(ZeroDivisionError, _ped.round_up_to, 100, 0)

class UnitSetDefaultTestCase(unittest.TestCase):
    def setUp(self):
        self._initialDefault = _ped.unit_get_default()

    def tearDown(self):
        _ped.unit_set_default(self._initialDefault)

    def runTest(self):
        for v in [_ped.UNIT_BYTE, _ped.UNIT_CHS, _ped.UNIT_COMPACT,
                  _ped.UNIT_CYLINDER, _ped.UNIT_GIBIBYTE, _ped.UNIT_GIGABYTE,
                  _ped.UNIT_KIBIBYTE, _ped.UNIT_KILOBYTE, _ped.UNIT_MEBIBYTE,
                  _ped.UNIT_MEGABYTE, _ped.UNIT_PERCENT, _ped.UNIT_SECTOR,
                  _ped.UNIT_TEBIBYTE, _ped.UNIT_TERABYTE]:
            _ped.unit_set_default(v)
            self.assert_(_ped.unit_get_default() == v, "Could not set unit default to %s" % v)

        self.assertRaises(ValueError, _ped.unit_set_default, -1)
        self.assertRaises(ValueError, _ped.unit_set_default, 1000)

class UnitGetDefaultTestCase(unittest.TestCase):
    def runTest(self):
        self.assert_(_ped.unit_get_default() >= 0)

class UnitGetSizeTestCase(unittest.TestCase):
    # TODO
    def runTest(self):
        pass

class UnitGetNameTestCase(unittest.TestCase):
    def runTest(self):
        self.assert_(_ped.unit_get_name(_ped.UNIT_COMPACT) == "compact")
        self.assert_(_ped.unit_get_name(_ped.UNIT_MEGABYTE) == "MB")
        self.assertRaises(ValueError, _ped.unit_get_name, -1)
        self.assertRaises(ValueError, _ped.unit_get_name, 1000)

class UnitGetByNameTestCase(unittest.TestCase):
    def runTest(self):
        self.assert_(_ped.unit_get_by_name("cyl") == _ped.UNIT_CYLINDER)
        self.assert_(_ped.unit_get_by_name("TB") == _ped.UNIT_TERABYTE)
        self.assertRaises(_ped.UnknownTypeException, _ped.unit_get_by_name, "blargle")

class UnitFormatCustomByteTestCase(unittest.TestCase):
    # TODO
    def runTest(self):
        pass

class UnitFormatByteTestCase(unittest.TestCase):
    # TODO
    def runTest(self):
        pass

class UnitFormatCustomTestCase(unittest.TestCase):
    # TODO
    def runTest(self):
        pass

class UnitFormatTestCase(unittest.TestCase):
    # TODO
    def runTest(self):
        pass

class UnitParseTestCase(unittest.TestCase):
    # TODO
    def runTest(self):
        pass

class UnitParseCustomTestCase(unittest.TestCase):
    # TODO
    def runTest(self):
        pass

# And then a suite to hold all the test cases for this module.
def suite():
    suite = unittest.TestSuite()
    suite.addTest(GreatestCommonDivisorTestCase())
    suite.addTest(DivRoundToNearestTestCase())
    suite.addTest(DivRoundUpTestCase())
    suite.addTest(RoundDownToTestCase())
    suite.addTest(RoundToNearestTestCase())
    suite.addTest(RoundUpToTestCase())
    suite.addTest(UnitSetDefaultTestCase())
    suite.addTest(UnitGetDefaultTestCase())
    suite.addTest(UnitGetSizeTestCase())
    suite.addTest(UnitGetNameTestCase())
    suite.addTest(UnitGetByNameTestCase())
    suite.addTest(UnitFormatCustomByteTestCase())
    suite.addTest(UnitFormatByteTestCase())
    suite.addTest(UnitFormatCustomTestCase())
    suite.addTest(UnitFormatTestCase())
    suite.addTest(UnitParseTestCase())
    suite.addTest(UnitParseCustomTestCase())
    return suite

s = suite()
unittest.TextTestRunner(verbosity=2).run(s)