import unittest

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class PatientHealthRecord:
    @staticmethod
    def isHealthRecordSymmetric(head):
        if not head or not head.next:
            return True  # Empty or single-node list is always symmetric

        # Step 1: Find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the list
        prev, current = None, slow
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        # Step 3: Compare the two halves
        left, right = head, prev
        while right:
            if left.value != right.value:
                return False  # Not symmetrical
            left = left.next
            right = right.next

        return True  # Symmetrical list

# Unit test class
class TestPatientHealthRecord(unittest.TestCase):
    def test_symmetric_list(self):
        head = ListNode(70, ListNode(85, ListNode(90, ListNode(85, ListNode(70, None)))))
        self.assertTrue(PatientHealthRecord.isHealthRecordSymmetric(head))

    def test_non_symmetric_list(self):
        head = ListNode(80, ListNode(85, ListNode(90, ListNode(92, ListNode(85, ListNode(70, None))))))
        self.assertFalse(PatientHealthRecord.isHealthRecordSymmetric(head))

    def test_single_node(self):
        head = ListNode(100)
        self.assertTrue(PatientHealthRecord.isHealthRecordSymmetric(head))

    def test_empty_list(self):
        head = None
        self.assertTrue(PatientHealthRecord.isHealthRecordSymmetric(head))

if __name__ == "__main__":
    unittest.main()
