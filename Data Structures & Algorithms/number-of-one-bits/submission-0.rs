impl Solution {
    pub fn hamming_weight(n: u32) -> i32 {

        let mut res = 0;
        let mut val = n;
        for _ in 0..32{
            if (val&1) == 1 {
                res+=1;
            }
            val >>= 1;
        }
        return res
    }
}
