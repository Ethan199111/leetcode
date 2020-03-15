class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    @staticmethod
    def print(root):
        while root is not None:
            print(root.val, end="->")
            root = root.next
