# coding: utf-8
"""
https://leetcode.com/problems/linked-list-cycle/
"""


class ListNode:  # pragma: no cover
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        visted_ids = set()

        node = head
        while node:
            node_id = id(node)
            if node_id in visted_ids:
                return True
            else:
                visted_ids.add(node_id)

            node = node.next

        return False


class Solution2:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
