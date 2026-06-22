impl Solution {
    pub fn count_bits(n: i32) -> Vec<i32> {


        pub fn get_bits(i: i32) -> i32{
            let mut i = i;
            let mut bit_count = 0;

            while i>0{
                i = i&i-1;
                bit_count+=1;
            }
            bit_count
        }

        let mut res = Vec::new();

        for i in 0..=n{
            res.push(get_bits(i))
        }
        res
    
}   

}