import unittest
from hello_world import hello_world
 
class TestGreeting(unittest.TestCase):
    
  def test_greeting(self):
    greeting = hello_world()
    self.assertEqual(greeting, "Hello World!")
 
  if __name__ =="__main__":
    unittest.main()