class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;
        ArrayList<Integer> arr = new ArrayList<>();
        int p=0;
        while(p<prices.length) {
            if (p==0) {
                profit=0;
                arr.add(prices[p]);
                p++;
            }
            else{
                int profitc=prices[p]-Collections.min(arr);
            if (profitc > profit){
                profit=profitc;
            }
            arr.add(prices[p]);
            p++;
            }
            
        



        }
        return profit;

        
    }
}
