class Solution {
    public int solution(int[] queue, int location) {
        int answer = 0;
        int[] priority = new int[10];
        for(int i = 0; i < queue.length; i++) {
            if (queue[i] < 1 || queue[i] > 9) return 0;
            priority[queue[i]]++;
        }
        int qpiv = 0, ppiv = 9;
        while(true) {
            if(priority[ppiv] > 0) {
                int printidx = qpiv;
                for(int i = 0; i < queue.length; i++) {
                    if(queue[printidx] == ppiv) {
                        qpiv = printidx + 1;
                        if(qpiv == queue.length) qpiv = 0;
                        priority[ppiv]--;
                        answer++;
                        if(printidx == location) return answer;
                        if(priority[ppiv] <= 0) break;
                    }
                    printidx++;
                    if(printidx >= queue.length) printidx = 0;
                }
            }
            else ppiv--;
            if (ppiv < 0) return -1;
        }
    }
}
