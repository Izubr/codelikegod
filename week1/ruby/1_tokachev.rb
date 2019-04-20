def permute(nums)
  return [nums] if nums.size < 2

  nums.each_with_object([]) do |num, result|
    permute(nums - [num]).each do |num_chunk|
      result << [num] + num_chunk
    end
  end
end
