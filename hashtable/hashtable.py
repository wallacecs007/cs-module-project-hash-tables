class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.size / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        # Prime number for base hash
        hash = 5381

        # Turning everything into UTF-8 numbers
        string_utf = key.encode()

        for char in string_utf:
            hash = hash * 33 + char
            hash &= 0xffffffff

        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        hash_index = self.hash_index(key)
        if not self.table[hash_index]:
            self.table[hash_index] = HashTableEntry(key, value)

        else:
            node = self.table[hash_index]

            # This checks to see if there is still a node in the list and if the key is unique
            while node.next and node.key != key:
                node = node.next

            # After getting the last node or finding a matching key logic begins
            # Updates the value if the key is already in the list
            if node.key == key:
                node.value = value
            # Adding new node to end of list
            else:
                node.next = HashTableEntry(key, value)
                self.size += 1

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        hash_index = self.hash_index(key)

        node = self.table[hash_index]
        # Checks to see if the key exists and if it doesn't, prints a warning
        if not node:
            print("There is no object with this key.")
        # Finding if this is the only node at this index
        elif not node.next:
            self.table[hash_index] = None
            self.size -= 1
        else:
            # Finding the node that has the associated key.
            prev_node = None
            while node.next and node.key != key:
                prev_node = node
                node = node.next
            if not prev_node:
                self.table[hash_index] = node.next
                self.size -= 1
            # Finding if this is the last node in the list.
            elif not node.next:
                prev_node.next = None
                self.size -= 1
            else:
                prev_node.next = node.next
                self.size -= 1

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here

        hash_index = self.hash_index(key)

        if self.table[hash_index]:
            node = self.table[hash_index]

            while node.next and node.key != key:
                node = node.next
            if node.key == key:
                return node.value

        else:
            return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here

        if new_capacity == 1024:
            print(new_capacity)

        hold_table = self.table
        self.capacity = new_capacity
        self.table = [None] * new_capacity

        for item in hold_table:
            if item:
                node = item
                while node:
                    self.put(node.key, node.value)
                    node = node.next


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
