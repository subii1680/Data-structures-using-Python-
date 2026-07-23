class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


front = None
rear = None


def enqueue(value):
    global front, rear

    newNode = Node(value)

    # If queue is empty
    if rear is None:
        front = newNode
        rear = newNode
    else:
        rear.next = newNode
        rear = newNode

    print("Element inserted successfully")


def dequeue():
    global front, rear

    # Check whether queue is empty
    if front is None:
        print("Queue is Empty")
    else:
        temp = front
        print("Deleted element:", temp.data)

        front = front.next

        # If queue becomes empty
        if front is None:
            rear = None


def display():
    if front is None:
        print("Queue is Empty!!!")
    else:
        temp = front

        print("Queue elements:")
        while temp is not None:
            print(temp.data, end=" --> ")
            temp = temp.next

        print("NULL")


# Main Program
while True:
    print("\n--- LINKED LIST IMPLEMENTATION OF QUEUE ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter the value: "))
        enqueue(value)

    elif choice == 2:
        dequeue()

    elif choice == 3:
        display()

    elif choice == 4:
        print("Program terminated")
        break

    else:
        print("Invalid choice")
