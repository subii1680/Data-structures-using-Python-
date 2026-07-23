SIZE = 5

queue = [0] * SIZE
front = -1
rear = -1


def enqueue(value):
    global front, rear

    if rear == SIZE - 1:
        print("Queue is FULL!!! Insertion is not possible!!!")
    else:
        rear += 1
        queue[rear] = value

        if front == -1:
            front = 0

        print("Element inserted successfully")


def dequeue():
    global front, rear

    if front == -1 or front > rear:
        print("Queue is EMPTY!!!")
    else:
        print("Deleted element:", queue[front])
        front += 1

        if front > rear:
            front = -1
            rear = -1


def isEmpty():
    if front == -1:
        return True
    else:
        return False


def size():
    if isEmpty():
        return 0
    else:
        return rear - front + 1


def show():
    if isEmpty():
        print("Queue is EMPTY!!!")
    else:
        print("Queue elements are:")
        for i in range(front, rear + 1):
            print(queue[i], end=" ")
        print()


# Main program
while True:
    print("\n--- ARRAY IMPLEMENTATION OF QUEUE ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. IsEmpty")
    print("4. Size")
    print("5. Show")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter the value: "))
        enqueue(value)

    elif choice == 2:
        dequeue()

    elif choice == 3:
        if isEmpty():
            print("Queue is EMPTY")
        else:
            print("Queue is NOT EMPTY")

    elif choice == 4:
        print("Size of queue:", size())

    elif choice == 5:
        show()

    elif choice == 6:
        print("Program terminated")
        break

    else:
        print("Invalid choice")
