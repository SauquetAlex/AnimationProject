package src.Reader;

import java.awt.Color;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Iterator;
import java.util.List;
import java.util.ArrayList;

public class Frames implements Iterable<Frames.Frame> {

  public static class Frame {
    // TODO: write our own Color class?
    private final Color[] leds;

    public Frame(int size) {
      leds = new Color[size];
    }

    // TODO: bounds check
    public Color getLed(int i) {
      return leds[i];
    }

    // TODO: bounds check
    public void setLed(int i, Color led) {
      leds[i] = led;
    }

    public int numLeds() {
      return leds.length;
    }

    public String toString() {
      StringBuffer sb = new StringBuffer();
      boolean first = true;
      for (Color led : leds) {
        if (!first) {
          sb.append(",");
        } else {
          first = false;
        }
        sb.append("R:" + Integer.toHexString(led.getRed()) + " ");
        sb.append("G:" + Integer.toHexString(led.getGreen()) + " ");
        sb.append("B:" + Integer.toHexString(led.getBlue()));
      }
      return sb.toString();
    }
  }

  private List<Frame> frames = new ArrayList<Frame>();

  public Frames(String filename) throws FileNotFoundException, IOException, ArithmeticException {
    BufferedReader reader = new BufferedReader(new FileReader(filename));
    int size;
    String line;
    if ((line = reader.readLine()) != null) {
      String[] dim = line.split(" ");
      size = (int) (Math.multiplyFull(Integer.valueOf(dim[0]), Integer.valueOf(dim[1])));
    } else {
      System.err.println("Invalid file: " + filename);
      return;
    }
    while ((line = reader.readLine()) != null) {
      // System.out.println("READING: " + line);
      String[] ledStrings = line.split(" ");
      if (ledStrings.length != size) {
        System.err.println("Invalid line: " + line);
        continue;
      }

      Frame frame = new Frame(size);
      for (int i = 0; i < ledStrings.length; ++i) {
        Color led = Color.decode(ledStrings[i].substring(0, 6));
        frame.setLed(i, led);
      }
      frames.add(frame);
    }
  }

  public int numFrames() {
    return frames.size();
  }

  @Override
  public Iterator<Frame> iterator() {
    return frames.iterator();
  }
}
