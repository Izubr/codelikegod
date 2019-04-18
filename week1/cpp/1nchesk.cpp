class Solution {

private:

    vector<vector<int>> result;

public:

    void recursive_permute(vector<int> &nums,int start) {

        if(start >= nums.size()) 

            return;

        recursive_permute(nums, start+1);

        for(int i=0; i<start; i++){

            swap(nums[i], nums[start]);

            result.push_back(nums);

            recursive_permute(nums, start+1);

            swap(nums[i], nums[start]);

        }

    }

    vector<vector<int>> permute(vector<int>& nums) {

        result.push_back(nums);

        recursive_permute(nums,1);

        return result;

    }

};