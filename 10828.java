import java.util.*;

public class Main {
    static class Node {
        public int value;
        public Node next;
        public Node(int val) {
            value = val;
            next = null;
        }
    }


    static class Stack {
        public Node top;
        int count;
        
        public Stack() {
            top  = null;
            count = 0;
        }

        public boolean isEmpty() {
            return (count == 0);
        }

        public void push(int a) {
            Node newnode;
            newnode = new Node(a);

            if (isEmpty()) {
                top = newnode;
                count++;
            }

            else {
                newnode.next = top;
                top = newnode;
                count++;
            }

        }

        public void pop() {
            if (isEmpty()) {
                System.out.println("-1");
            }

            else {
                int ret = top.value;
                top = top.next;
                count--;
                System.out.println(ret);
            }
        }
    }

    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        String input;
        Stack stack = new Stack();

        for (int i = 0; i < n; i++ ) {
            input = sc.next();

            if (input.equals("push")) stack.push(sc.nextInt());

            else if (input.equals("pop")) stack.pop();

            else if (input.equals("size")) {
            	System.out.println(stack.count);
            }

            else if (input.equals("empty")) {
                if (stack.isEmpty()) System.out.println("1");
                else System.out.println("0");
            }

            else if (input.equals("top")) {
                if (stack.isEmpty()) System.out.println("-1");
                else System.out.println(stack.top.value);
            }

        }
        sc.close();
    }
}