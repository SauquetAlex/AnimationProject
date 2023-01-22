package src.Reader;

import java.awt.*;

class Main {

  public static void main(String[] args) {
    try {
      Frames frames = new Frames("frames.txt");
      for (Frames.Frame frame : frames) {
        System.out.println(frame);
      }
    } catch (Exception e) {
      e.printStackTrace();
    }

  }

}