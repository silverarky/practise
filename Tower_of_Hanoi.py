#coding=utf-8
def move(n,a,b,c):
    if n==1:
        print(a+"-->"+c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)

move(3,"A","B","C")

#关注每一步骤的最终结果，而不是每一步骤的细节。
#无论每一个盘是怎么移动，底盘以上的n-1个盘都会以相同的方式移动。