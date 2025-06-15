import java.util.*;

class Solution {
    static class Truck {
        int weight;
        int enterTime;

        Truck(int weight, int enterTime) {
            this.weight = weight;
            this.enterTime = enterTime;
        }
    }

    public int solution(int bridge_length, int weight, int[] truck_weights) {
        Queue<Truck> bridge = new LinkedList<>();
        int time = 0;
        int totalWeight = 0;
        int index = 0;

        while (index < truck_weights.length || !bridge.isEmpty()) {
            time += 1;

            if (!bridge.isEmpty() && time - bridge.peek().enterTime >= bridge_length) {
                totalWeight -= bridge.poll().weight;
            }

            if (index < truck_weights.length && totalWeight + truck_weights[index] <= weight) {
                bridge.offer(new Truck(truck_weights[index], time));
                totalWeight += truck_weights[index];
                index += 1;
            }
        }

        return time;
    }
}