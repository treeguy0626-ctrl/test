from collections import deque
from typing import Optional, List
from datetime import datetime

RECENT_LIMIT = 5

class Item:
    def __init__(self, item_id: str, name: str, price: float, available: bool = True):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.available = available
        self.next = None


class Menu:
    def __init__(self):
        self.head: Optional[Item] = None

    def insert(self, node: Item):
        if not self.head:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def delete(self, item_id: str) -> bool:
        prev = None
        cur = self.head
        while cur:
            if cur.item_id == item_id:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                return True
            prev = cur
            cur = cur.next
        return False

    def find(self, item_id: str) -> Optional[Item]:
        cur = self.head
        while cur:
            if cur.item_id == item_id:
                return cur
            cur = cur.next
        return None

    def to_list(self) -> List[Item]:
        out = []
        cur = self.head
        while cur:
            out.append(cur)
            cur = cur.next
        return out


class Category:
    def __init__(self, name: str):
        self.name = name
        self.children = {}
        self.items_list = Menu()

    def add_child(self, child_name: str):
        normalized_name = child_name.lower()
        if normalized_name not in self.children:
            self.children[normalized_name] = Category(child_name)
        return self.children[normalized_name]

    def get_child(self, child_name: str) -> Optional['Category']:
        return self.children.get(child_name.lower())

    def traverse_preorder(self):
        stack = [(self, 0)]
        while stack:
            node, depth = stack.pop()
            yield node, depth
            for child_name in sorted(node.children.keys(), reverse=True):
                stack.append((node.children[child_name], depth + 1))


class RecentUpdates:
    def __init__(self, limit=RECENT_LIMIT):
        self.q = deque(maxlen=limit)

    def enqueue(self, text: str):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.q.append(f"[{timestamp}] {text}")

    def get(self):
        return list(self.q)


class Shop:
    def __init__(self, shop_id: str, name: str, password: str):
        self.shop_id = shop_id
        self.name = name
        self.password = password
        self.status = "Closed"
        self.menu_tree = Category(name)
        self.recent_updates = RecentUpdates()

    def add_category(self, category_name: str):
        self.menu_tree.add_child(category_name)
        self.recent_updates.enqueue(f"Category '{category_name}' added")

    def add_item(self, category_name: str, item_id: str, item_name: str, price: float):
        cat = self.menu_tree.get_child(category_name)
        if not cat:
            cat = self.menu_tree.add_child(category_name)
        node = Item(item_id, item_name, price, available=True)
        cat.items_list.insert(node)
        self.recent_updates.enqueue(f"Added item '{item_name}' to {category_name}")

    def remove_item(self, category_name: str, item_id: str):
        cat = self.menu_tree.get_child(category_name)
        if not cat:
            return False
        success = cat.items_list.delete(item_id)
        if success:
            self.recent_updates.enqueue(f"Removed item {item_id} from {category_name}")
        return success

    def find_item(self, item_id: str):
        for node, _ in self.menu_tree.traverse_preorder():
            found = node.items_list.find(item_id)
            if found:
                return node, found
        return None, None

    def toggle_availability(self, category_name: str, item_id: str, available: bool):
        cat = self.menu_tree.get_child(category_name)
        if not cat:
            return False
        found = cat.items_list.find(item_id)
        if not found:
            return False
        found.available = available
        state = "Available" if available else "Sold Out"
        self.recent_updates.enqueue(f"Item '{found.name}' marked {state}")
        return True
