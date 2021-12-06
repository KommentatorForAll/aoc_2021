import java.math.BigInteger;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class Main {

    public static void main(String[] args) {
        String input = "5,1,1,1,3,5,1,1,1,1,5,3,1,1,3,1,1,1,4,1,1,1,1,1,2,4,3,4,1,5,3,4,1,1,5,1,2,1,1,2,1,1,2,1,1,4,2,3,2,1,4,1,1,4,2,1,4,5,5,1,1,1,1,1,2,1,1,1,2,1,5,5,1,1,4,4,5,1,1,1,3,1,5,1,2,1,5,1,4,1,3,2,4,2,1,1,4,1,1,1,1,4,1,1,1,1,1,3,5,4,1,1,3,1,1,1,2,1,1,1,1,5,1,1,1,4,1,4,1,1,1,1,1,2,1,1,5,1,2,1,1,2,1,1,2,4,1,1,5,1,3,4,1,2,4,1,1,1,1,1,4,1,1,4,2,2,1,5,1,4,1,1,5,1,1,5,5,1,1,1,1,1,5,2,1,3,3,1,1,1,3,2,4,5,1,2,1,5,1,4,1,5,1,1,1,1,1,1,4,3,1,1,3,3,1,4,5,1,1,4,1,4,3,4,1,1,1,2,2,1,2,5,1,1,3,5,2,1,1,1,1,1,1,1,4,4,1,5,4,1,1,1,1,1,2,1,2,1,5,1,1,3,1,1,1,1,1,1,1,1,1,1,2,1,3,1,5,3,3,1,1,2,4,4,1,1,2,1,1,3,1,1,1,1,2,3,4,1,1,2";
        ArrayList<Integer> inp = new ArrayList<>();
        for (String i : input.split(",")) {
            inp.add(Integer.parseInt(i));
        }
        HashMap<Integer, BigInteger> hm = new HashMap<>(), tmp;
        for (int i : inp) {
            hm.put(i, hm.getOrDefault(i, BigInteger.ZERO).add(BigInteger.ONE));
        }
        int day = 0;
        while (day < 256) {
            tmp = new HashMap<>();
            for (Map.Entry<Integer, BigInteger> e : hm.entrySet()) {
                int cd = e.getKey() -1;
                if (cd < 0) {
                    tmp.put(8, e.getValue().add(tmp.getOrDefault(8, BigInteger.ZERO)));
                    cd = 6;
                }
                tmp.put(cd, e.getValue().add(tmp.getOrDefault(cd, BigInteger.ZERO)));
            }
            hm = tmp;
            day++;
        }
        BigInteger sum = BigInteger.ZERO;
        for (BigInteger v : hm.values()) {
            sum = sum.add(v);
        }
        System.out.println(sum);
    }
}