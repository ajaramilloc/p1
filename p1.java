import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class p1 {

    private static List<Integer> soluciones = new ArrayList<>();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int totalcases = 0;

        if (scanner.hasNextLine()) {
            totalcases = Integer.parseInt(scanner.nextLine());
        }

        for (int i = 0; i < totalcases; i++) {
            String[] input_data = scanner.nextLine().split(" ");
            List<Integer> T = new ArrayList<>();

            for (int j = 0; j < input_data.length; j++) {
                T.add(Integer.parseInt(input_data[j]));
            }

            System.out.println(F(T,0,0));
        }

        scanner.close();
    }

    private static int encontrarI(List<Integer> T) {
        for (int i = T.size() - 1; i >= 0; i--) {
            if (i != T.size() - 1 && T.get(i) < T.get(i + 1)) {
                return i;
            }
        }
        return -1;
    }

    private static int encontrarX(List<Integer> T, int i) {
        for (int x = i - 1; x >= 0; x--) {
            if (T.get(x) > 0) {
                return x;
            }
        }
        return -1;
    }

    private static int F(List<Integer> T, int i, int movs) {
        i = encontrarI(T);
        int x = encontrarX(T, i);
        int newMovs = 0;

        if (x < i) {
            newMovs = i - x;
        }

        if (i == -1) {
            soluciones.add(movs);
            return movs;
        } else if (!soluciones.isEmpty() && movs > soluciones.stream().min(Integer::compare).get()) {
            return Integer.MAX_VALUE;
        } else if (i == 0) {
            T.set(0, T.get(0) + 1);
            T.set(1, T.get(1) - 1);
            return F(T, i, movs + 1);
        } else {
            List<Integer> option1 = new ArrayList<>(T);
            option1.set(i, option1.get(i) + 1);
            option1.set(i + 1, option1.get(i + 1) - 1);

            List<Integer> option2 = new ArrayList<>(T);
            option2.set(x, option2.get(x) - 1);
            option2.set(i, option2.get(i) + 1);

            if (F(option1, i, movs + 1) <= F(option2, i, movs + newMovs)) {
                return F(option1, i, movs + 1);
            } else {
                return F(option2, i, movs + newMovs);
            }
        }
    }
}
