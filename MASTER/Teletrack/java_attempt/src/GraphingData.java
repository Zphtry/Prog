import java.awt.*;
import java.awt.geom.*;
import javax.swing.*;


public class GraphingData extends JPanel {
    private int[] data = {
            21, 14, 18, 3, 86, 88, 74, 87, 54, 77,
            61, 55, 48, 60, 49, 36, 38, 27, 20, 18
    };

    protected void paintComponent(Graphics g) {
        super.paintComponent(g);

        Graphics2D g2 = (Graphics2D)g;
        g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

        int width = getWidth(), height = getHeight();

        int PAD = 20;

        // Draw ordinate.
        g2.draw(new Line2D.Double(PAD, PAD, PAD, height - PAD));

        // Draw abscissa.
        g2.draw(new Line2D.Double(PAD, height - PAD, width - PAD, height - PAD));

        double xInc = (width - 2 * PAD) / (data.length - 1);
        double scale = (height - 2 * PAD) / getMax();

        // Mark data points.
        g2.setPaint(Color.red);
        for (int i = 0; i < data.length; i++) {
            double x = PAD + i * xInc;
            double y = height - PAD - scale * data[i];
//            g2.fill(new Ellipse2D.Double(x - 2, y - 2, 4, 4));
            g2.draw(new Line2D.Double(x - 2, y - 2, 4, 4));
        }
    }

    private int getMax() {
        int max = -Integer.MAX_VALUE;
        for (int aData : data) {
            if (aData > max)
                max = aData;
        }
        return max;
    }
}