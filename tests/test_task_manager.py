import unittest
import task_manager as tm


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        tm.tasks.clear()
        tm.next_id = 1

    def test_add_task(self):
        task = tm.add_task("Write report")
        self.assertEqual(task["title"], "Write report")
        self.assertEqual(len(tm.tasks), 1)

    def test_complete_task(self):
        tm.add_task("Write report")
        self.assertTrue(tm.complete_task(1))
        self.assertTrue(tm.tasks[0]["completed"])

    def test_delete_task(self):
        tm.add_task("Write report")
        self.assertTrue(tm.delete_task(1))
        self.assertEqual(len(tm.tasks), 0)

    def test_empty_title_rejected(self):
        with self.assertRaises(ValueError):
            tm.add_task("   ")

