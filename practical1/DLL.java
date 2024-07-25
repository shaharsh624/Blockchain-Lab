import java.util.Scanner;

public class DLL {

    static Node head;

    static class Block {
        int rollNo;
        String name;
        String branch;

        Block(int roll, String nameIn, String branchIn) {
            rollNo = roll;
            name = nameIn;
            branch = branchIn;
        }
    }

    static class Node {
        Node prev;
        Block data;
        Node next;

        Node(Block std) {
            prev = null;
            data = std;
            next = null;
        }
    }

    public static DLL addBlock(DLL list, Block data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
        } else {
            Node temp = head;
            while (temp.next != null) {
                temp = temp.next;
            }
            temp.next = newNode;
            newNode.prev = temp;
        }
        return list;
    }

    public static void printList(DLL list) {
        System.out.println("\nThe List is: ");
        Node current = head;
        while (current != null) {
            System.out.println(current.data.rollNo + " - " + current.data.name + " - " + current.data.branch);
            current = current.next;
        }
    }

    public static void main(String[] args) {
        DLL list = new DLL();
        Scanner sc = new Scanner(System.in);

        Block b1 = new Block(1, "Harsh", "CSE");
        list = DLL.addBlock(list, b1);

        for (int i = 1; i <= 3; i++) {
            System.out.printf("Enter data for student %d:\n", i + 1);
            int roll = sc.nextInt();
            sc.nextLine();
            String name = sc.nextLine();
            String branch = sc.nextLine();

            Block b = new Block(roll, name, branch);
            list = DLL.addBlock(list, b);
        }

        printList(list);
        sc.close();
    }
}
