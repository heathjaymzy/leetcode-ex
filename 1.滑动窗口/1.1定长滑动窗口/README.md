# 伪代码
1. 维持窗口 k - 1长度
2. 入： s[i]
3. 更新tmpans
4. 出： s[i - k + 1]是否符合要求？
  - 符合要求-1
  - 不符合要求不动
```python
for i, val in enumerate(s):
  if condition(s[i]):
    tmpans += 1
  if tmpans > ans:
    ans = tmpans
  if i < k - 1:
    continue
  if s[i - k + 1] in condition:
    tmpans -= 1
```

## 小tips
2841： 使用hash表去重：
-- hash初始化
cnt = defaultdict(int)
-- hash 删除元素
del(cnt[x])
-- zip函数打包对应的list -> dict
enumerate(zip(s1, s2))

