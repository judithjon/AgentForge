# test_agentforge.py
"""
Tests for AgentForge module.
"""

import unittest
from agentforge import AgentForge

class TestAgentForge(unittest.TestCase):
    """Test cases for AgentForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AgentForge()
        self.assertIsInstance(instance, AgentForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AgentForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
