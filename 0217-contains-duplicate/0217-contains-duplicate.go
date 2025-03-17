func containsDuplicate(nums []int) bool {
    hashset := make(map[int]bool)
    for _, num := range nums {
        if hashset[num] {
            return true
        }
        hashset[num] = true
    }
    return false
}
