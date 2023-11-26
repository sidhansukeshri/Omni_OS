# memory_allocator.py
import sys

class MemoryAllocator:
    def __init__(self, total_memory):
        self.total_memory = total_memory
        self.allocated_memory = 0

    def allocate_memory(self, size):
        if self.allocated_memory + size <= self.total_memory:
            self.allocated_memory += size
            return f"Allocated {size} bytes of memory."
        else:
            return "Memory allocation failed. Not enough free memory."

    def deallocate_memory(self, size):
        if self.allocated_memory >= size:
            self.allocated_memory -= size
            return f"Deallocated {size} bytes of memory."
        else:
            return "Memory deallocation failed. Requested size exceeds allocated memory."

def update_memory_allocation(allocator):
    allocated_blocks = int((allocator.allocated_memory / allocator.total_memory) * 20)
    free_blocks = 20 - allocated_blocks
    percentage_filled = (allocator.allocated_memory / allocator.total_memory) * 100

    # If allocated_memory equals total_memory, set percentage_filled to 100
    if allocator.allocated_memory == allocator.total_memory:
        percentage_filled = 100

    # Move the cursor to the beginning of the line
    sys.stdout.write("\r")
    sys.stdout.write("Memory Allocation Status: [")
    sys.stdout.write("#" * allocated_blocks)
    sys.stdout.write(" " * free_blocks)
    sys.stdout.write("] ")
    sys.stdout.write(f"{percentage_filled:.2f}%   \n")  # Add spaces to clear any previous characters

    sys.stdout.write(f"Allocated Memory: {allocator.allocated_memory} bytes\n")
    sys.stdout.write(f"Free Memory: {allocator.total_memory - allocator.allocated_memory} bytes\n")

def run_memory_allocator():
    total_memory = int(input("Enter the total memory size: "))
    allocator = MemoryAllocator(total_memory)

    while True:
        print("\n Menu for Memory Allocator")
        print("1. Allocate memory")
        print("2. Deallocate memory")
        print("3. View memory allocation")
        print("4. Return to the menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            size = int(input("Enter the size to allocate: "))
            print(allocator.allocate_memory(size))
            update_memory_allocation(allocator)
        elif choice == '2':
            size = int(input("Enter the size to deallocate: "))
            print(allocator.deallocate_memory(size))
            update_memory_allocation(allocator)
        elif choice == '3':
            update_memory_allocation(allocator)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    run_memory_allocator()
