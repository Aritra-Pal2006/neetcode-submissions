class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;        
        int p=0;
        int min=prices[0];
        while(p<prices.length) {
            if (p==0) {
                profit=0;
                min=Math.min(min,prices[p]);
                p++;
            }
            else{
            
            if ((prices[p]-min)> profit){
                profit=prices[p]-min;
            }
            min=Math.min(min,prices[p]);
            p++;
            }
        }
        return profit;        
    }
}
