import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

/*
 * Tried to use a lot of constructs to learn features of the language 
 */
class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int indexNums1 = 0, indexNums2 = 0;
        boolean averagedMedian = (nums1.length + nums2.length) % 2 == 0;
        double lastMinValue = -1, newMinValue = -1;
        List<Integer> nums1List = Arrays.stream(nums1).boxed().collect(Collectors.toList());
        List<Integer> nums2List = Arrays.stream(nums2).boxed().collect(Collectors.toList());
        int flooredHalfIndex = (int) Math.floor((nums1.length + nums2.length) / 2);
        for (int i = 0; i <= flooredHalfIndex; i++) {
            // VALUE UPDATE
            lastMinValue = newMinValue;
            switch (traverseIntListOnPos(nums1List, indexNums1, nums2List, indexNums2)) {
                case WhoToAdvance.FIRST -> {
                    newMinValue = nums1List.get(indexNums1);
                    indexNums1++;
                }
                case WhoToAdvance.SECOND -> {
                    newMinValue = nums2List.get(indexNums2);
                    indexNums2++;
                }
            }
            // RETURN CLAUSES
            // Method always reaches this.
            if (i == flooredHalfIndex) {
                return !averagedMedian ? newMinValue : (lastMinValue + newMinValue) / 2;
            }
        }
        throw new IndexOutOfBoundsException("There are no elements in the arrays");
    }

    enum WhoToAdvance {
        FIRST, SECOND
    }

    public WhoToAdvance traverseIntListOnPos(List<Integer> list1, int pos1, List<Integer> list2, int pos2)
            throws IndexOutOfBoundsException {
        if (pos1 >= list1.size() && pos2 >= list2.size())
            throw new IndexOutOfBoundsException("The method is being called on positions greater than existing ones");
        else if (pos1 >= list1.size())
            return WhoToAdvance.SECOND;
        else if (pos2 >= list2.size())
            return WhoToAdvance.FIRST;
        else if (list1.get(pos1) >= list2.get(pos2)) {
            return WhoToAdvance.SECOND;
        } else {
            return WhoToAdvance.FIRST;
        }

    }

    public static void main(String[] args) {
        System.out.println("hUH?");
        System.out.println(List.of(1, 32, 3).stream().filter(number -> number > 5).collect(Collectors.toList()));
        Solution sol = new Solution();
        double test1 = sol.findMedianSortedArrays(new int[] { 1, 3 }, new int[] { 2 });
        System.out.println(test1);
        System.out.println(Math.abs(test1 - 2.0) < 0.001);
        double test2 = sol.findMedianSortedArrays(new int[] { 1, 2 }, new int[] { 3, 4 });
        System.out.println(test2);
        System.out.println(Math.abs(test2 - 2.5) < 0.001);
    }
}