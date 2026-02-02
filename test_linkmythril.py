# test_linkmythril.py
"""
Tests for LinkMythril module.
"""

import unittest
from linkmythril import LinkMythril

class TestLinkMythril(unittest.TestCase):
    """Test cases for LinkMythril class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LinkMythril()
        self.assertIsInstance(instance, LinkMythril)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LinkMythril()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
