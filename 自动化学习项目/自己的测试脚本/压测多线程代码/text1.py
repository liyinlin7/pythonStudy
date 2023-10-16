seeScoreValue = float( '95.00')
print(seeScoreValue)
gradeValue_ = '甲' if 100 > seeScoreValue >=90 else '乙' if 90<seeScoreValue<=80 else '丙' if 80< seeScoreValue<=60 else '丁' if 60<seeScoreValue<=0 else ''
print(gradeValue_)