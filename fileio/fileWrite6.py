f=open("score.txt","r")
score=f.readline()
score=list(map(int,score))
score_sum=0

for i in score:
    score_sum+=i
avg=score_sum/len(score)

print("합 %d이다" %score_sum)
print("평균은 %d" %avg)