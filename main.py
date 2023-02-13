S = list(input())
one_s = list(S)
zero_s = list(S)
mark = False
cnt = 0
#모두 1로
for i in range(len(one_s)):
  if one_s[i] == "0":
    one_s[i] = "1"
    if not mark:
      mark =True
      cnt = cnt+1
  elif mark:
    mark = False
#모두 0으로

z_mark = False
z_cnt = 0
for i in range(len(zero_s)):
  if zero_s[i] == "1":
    zero_s[i] = "0"
    if not z_mark:
      z_mark =True
      z_cnt = z_cnt+1
  elif z_mark:
    z_mark = False
if cnt == z_cnt:
  print(cnt)
else:
  print(cnt if cnt<z_cnt else z_cnt)
    