```
x = 1
for i in range(len(nums)-1):
if(nums[i]!=nums[i+1]):
nums[x] = nums[i+1]
x+=1
return(x)
```
​
​
​
```
if len(nums) <= 1 {
return 1
}
i, j := 0, 1
for j < len(nums) {
if nums[i] == nums[j] {
j++
} else {
nums[i+1] = nums[j]
i++
j++
}
}
return i+1
}
```
​