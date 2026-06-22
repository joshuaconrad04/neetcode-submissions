impl Solution {
    pub fn count_bits(n: i32) -> Vec<i32> {
    
        let mut res = Vec::new();
            pub fn cn_bit(n: i32) -> i32{
            let mut w = n;
            let mut res = 0;

            for _ in 0..32{
                if (w&1)==1{
                    res+=1;
                }
                w>>=1;
            }
            res
        }


        for i in 0..=n {
            let tmp = cn_bit(i);
            res.push(tmp);
        }
        res
    }

    
}
