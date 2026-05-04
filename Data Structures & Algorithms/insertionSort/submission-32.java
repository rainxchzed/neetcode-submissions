// Definition for a pair
// class Pair {
//     int key;
//     String value;
//
//     Pair(int key, String value) {
//         this.key = key;
//         this.value = value;
//     }
// }
public class Solution {
    public List<List<Pair>> insertionSort(List<Pair> pairz) {
        if(pairz.size() <= 0) return new ArrayList<>();

        ArrayList<Pair> pairs = new ArrayList<>(pairz);
        List<List<Pair>> res = new ArrayList<>();
        res.add(pairz);

        for(int i = 1; i < pairs.size(); i++) {
            int j = i - 1;

            while(j >= 0 && pairs.get(j + 1).key < pairs.get(j).key) {
                Pair temp = pairs.get(j + 1);
                pairs.set(j + 1, pairs.get(j));
                pairs.set(j, temp);

                j = j - 1;
            }

            res.add(new ArrayList<>(pairs));
        }

        return res;
    }
}
