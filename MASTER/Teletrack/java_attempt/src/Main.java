import javax.swing.*;
import java.util.ArrayList;
import java.util.List;

public class Main {
    private static int fact(int x) {
        if (x == 0) return 1;
        else return(x * Main.fact(x - 1));
    }

    public static void main(String[] args) {

        double l_left = .01, l_right = 1,  delta_l = .05, m = .9;
        int M = 10, N = 10;

        float X1 = Main.fact(M) / (Main.fact(N) * Main.fact(M - N));
        double X = l_left;

        // 1
        List<Double> P1_k = new ArrayList<>();
        List<Double> G1_k = new ArrayList<>();
        List<Double> E1_k = new ArrayList<>();

        while (X < l_right) {
            double X2 = Math.pow(X / m, N);
            int S = 0;
            int Y = 0;
            while(Y <= N) {
                double Y2 = Math.pow(X / m, Y);
                double Y1 = Main.fact(M) / (Main.fact(Y) * Main.fact(M - Y));
                S += Y1 * Y2;
                Y += 1;
            }

            P1_k.add(X1 * (X2 / S));
            G1_k.add(X * M * (1 - P1_k.get(P1_k.size() - 1)));
            E1_k.add((X * M / m) * (1 - P1_k.get(P1_k.size() - 1)));
            X += delta_l;
        }

        // 2
        List<Double> P2_k = new ArrayList<>();
        List<Double> G2_k = new ArrayList<>();
        List<Double> E2_k = new ArrayList<>();
        X = l_left;
        while (X < l_right) {
            double X2 = Math.pow(X * M / m, N) / Main.fact(N);
            int S = 0;
            int Y = 0;
            while(Y <= (N + 1)) {
                double Y2 = (Math.pow(X * M / m, Y) / Main.fact(Y));
                S += Y2;
                Y += 1;
            }

            P2_k.add(X2 / S);
            G2_k.add(X * M * (1 - P2_k.get(P2_k.size() - 1)));
            E2_k.add((X * M / m) * (1 - P2_k.get(P2_k.size() - 1)));
            X += delta_l;
        }

        // 3
        X1 = Main.fact(M) / (Main.fact(N) * Main.fact(M - N));
        X = l_left;

        List<Double> P3_k = new ArrayList<>();
        List<Double> G3_k = new ArrayList<>();
        List<Double> E3_k = new ArrayList<>();

        while(X < l_right) {
            double X2 = Math.pow(X / (m + X), N);
            double Y2 = Math.pow((1 - (X / (m + X))), (M - N));
            P3_k.add(X1 * X2 * Y2);
            G3_k.add(X * M * (1 - P3_k.get(P3_k.size() - 1)));
            E3_k.add((X * M / m) * (1 - P3_k.get(P3_k.size() - 1)));
            X += delta_l;
        }

        JFrame frame = new JFrame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.add(new GraphingData());
        frame.setSize(400,400);
        frame.setLocation(200,200);
        frame.setVisible(true);
    }
}
