import unittest
from contact import Contact
from hash_map import HashMap
from merge_sort import merge_sort

class TestContactsApp(unittest.TestCase):

    def test_add_and_get_contact(self):
        hm = HashMap()
        c = Contact("Alice", "123")
        hm.put("alice", c)
        self.assertEqual(hm.get("alice"), c)

    def test_delete_contact(self):
        hm = HashMap()
        c = Contact("Bob", "456")
        hm.put("bob", c)
        hm.remove("bob")
        self.assertIsNone(hm.get("bob"))

    def test_search_empty_map(self):
        hm = HashMap()
        self.assertIsNone(hm.get("not_here"))

    def test_collision_handling(self):
        hm = HashMap(size=1)  # force collision
        c1 = Contact("A", "111")
        c2 = Contact("B", "222")
        hm.put("a", c1)
        hm.put("b", c2)
        self.assertEqual(hm.get("a"), c1)
        self.assertEqual(hm.get("b"), c2)

    def test_merge_sort(self):
        c1 = Contact("Charlie", "333")
        c2 = Contact("Alice", "111")
        c3 = Contact("Bob", "222")
        sorted_list = merge_sort([c1, c2, c3])
        self.assertEqual([c.name for c in sorted_list], ["Alice", "Bob", "Charlie"])

if __name__ == "__main__":
    unittest.main()
