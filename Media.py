import pandas as pd

profile_data = pd.DataFrame([],columns=["Name", "Email id","Total posts"])
post_data = pd.DataFrame([],columns = ["Name ", "Total Likes ", "Total comments ", "Views "])

class profile:
    register=[]
    records = []
    def __init__(self,name,mail):
        while name  in profile.register:
            print("sorry that name is not available")
            name=input("Enter your name")
        self.name =name
        profile.register.append(self.name)
        profile.records.append(self)
        self.mail=mail
        self.totalposts=0
        self.post=[]
        profile_data.loc[len(profile_data.index)]=[self.name , self.mail,len(self.post)]
        self.liked_posts = []
        self.commented_posts = {}
    def total_posts(self):
        print("total posts are",self.totalposts)
def like(posts,profile):
    posts.likies(profile) 
def comment(posts,profile):
    posts.comm(profile)
def all_likes(posts):
    print("Total likes are",posts.total_likes())
    sum =0
    for i in posts.like_people:
        print(sum , ": ", end=" ")
        print(i)
        sum= sum+1
def all_comments(posts):
    print("The total comments are",len(posts.comment_people))
    sum =0
    for i,j in posts.comment_people.items():
        print(sum, " ",i,":",j)
        sum = sum + 1

class post:
    obj=[]
    def __init__(self,profile,content):
        profile.post.append(self)
        post.obj.append(self)
        self.profile= profile
        self.views=[]
        self.likees=[]
        self.like_people={}
        self.commentees = []
        self.comment_people={}
        self.comment_peoples={}
        self.comment=[]
        print('\n','\n')
        self.post=content
        profile.totalposts+=1
        post_data.loc[len(post_data.index)]=[self.profile.name , len(self.like_people) , len(self.comment_people) , len(self.views)]
        self.indexs=len(post_data) -1
    def likies(self,profilex):
        if profilex.name not in self.like_people:
            self.views.append(profilex.name)
            self.like_people[profilex.name]=profilex
            self.likees.append(profilex.name)
            profilex.liked_posts.append(self)
        else:
            print(f" {profilex.name}you have already liked our post ")
        post_data.iloc[self.indexs] = [self.profile.name , len(self.like_people), len(self.comment_people), len(self.views)]
    def comm(self,profilex):
        self.coments=input("Enter your comment :")
        self.comment.append(self.coments)
        if profilex.name not in self.views:
            self.views.append(profilex.name)
        if profilex.name not in self.comment_people:
            self.comment_people[profilex.name] = self.coments
            self.comment_peoples[profilex.name]= profilex
            self.commentees.append(profilex.name)
            profilex.commented_posts[self] = self.coments
        post_data.iloc[self.indexs] = [self.profile.name , len(self.like_people), len(self.comment_people), len(self.views)]
    def total_likes(self):
        return len(self.like_people)
    def total_comments(self):
        return len(self.comment_peoples)
def see_profile(profilex):
    print(profilex.name)
    print("Total posts  :",profilex.totalposts)
    if len(profilex.post) ==0:
            print("No post for this profile")
            return 
    print("press 1 to view all his posts")
    profile_number=int(input())
    if profile_number==1:
        for i in profilex.post:
            review_post(i,profilex)
            see_in_detail(i)
    print("Thank yoy for visting", profilex.name , "profile")
def see_like_detail(pose1):
        print("enter the index number to view their profile")
        print("press n  to not view any of the profile")
        while True:
            index_number=input()
            if index_number == "n":
                print(f"Thank you for viewing the likes of this {pose1.profile.name} post ")
                break
            elif int(index_number) in range(len(pose1.like_people)):
                see_profile(pose1.like_people[pose1.likees[int(index_number)]])
                break
            else:
                print("You have entered a wrong index ,enter again ")
def see_comment_detail(pose1):
        print("Enter the index number to view their profile ")
        print("print n to not view any of the profile")
        while True:
            index_number=input()
            if index_number == "n":
                print(f"Thankyou for viewing all the comments of this {pose1.profile.name} post ")
                break
            elif int(index_number) in range(len(pose1.comment_peoples)):
                see_profile(pose1.comment_peoples[pose1.commentees[int(index_number)]])
                break
            else:
                print("you have entered a wrong number , please enter the number again")
def see_in_detail(pose1):
    print("press rl to see all the comments and press r to see the people who liked the post and press N to do nothing")
    while True:
        m = input()
        if m=="r":
            all_likes(pose1)
            see_like_detail(pose1)
            print("press r now to view all the comments of ", pose1.profile.name," press anyhting if you do not want to view anything")
            comment_watch = input()
            if comment_watch == "r":
                if len(pose1.comment_peoples) != 0 :
                    see_comment_detail(pose1)
                else:
                    print("No comments to this post")
            else:
                pass
            break
        elif m=="rl":
            all_comments(pose1)
            see_comment_detail(pose1)
            print("press r1 to view the likes of" ,pose1.profile.name ,"press anyhting if you do not want to watch it ")
            like_watch = input()
            if like_watch == "r1":
                see_like_detail(pose1)
            else:
                pass
            break
        elif m == 'N':
            break
        else:
            print("you have entered wrong key press again ")
def review_post(pose1,profilex):
    print("Name :",pose1.profile.name)
    print("The content of the post of is :",pose1.post)
    print("Total likes ",pose1.total_likes())
    print("The total comments ", pose1.total_comments())
    print("press l to like the post ")
    print("press c to comment the post ")
    print("press N  if you do not want to review the post")
    while True:
        review = input()
        if review == "N":
            break
        elif review == "l":
            like(pose1,profilex)
            print("press c to comment the post and press anything to not")
            comments = input()
            if comments == "c":
                comment(pose1,profilex)
            break
        elif review == "c":
            comment(pose1,profilex)
            print("press l to like the post and anything to not")
            likes = input()
            if likes == "l":
                like(pose1,profilex)
            break
        else:
            print("you have entered wrong key please enter again ")



profile1 = profile("harinath", "harinath@gmail.com")
profile2 = profile("manikanta","gangolamanikanta@gmail.com")
profile3= profile("Abhinav","abhinav@gmail.com")
profile4=profile("Abi","gandfkjl")
profile5 = profile("sushmitha","gangolasushmitha@gmail.com")
profile6=profile("supriya","gangolasupriya@gmail.com")
profile7 = profile("saikrishna","gangolasaikerishna@gmail.com")
profile8 = profile("python","pyhton123")
profile9 = profile("c++","c+++")
profile10= profile("c","c")
profile11= profile("java","java2")
post1 = post(profile1,"I am vey good at python programming")
post2 = post(profile2, " I like to web development ")
like(post2,profile9)
like(post2,profile8)
like(post1, profile1)
post3 = post(profile8,"I am fan of java")
like(post3 ,profile10)
like(post3,profile6)

if __name__ == "__main__":
    print("***************************** WELCOME TO SOCIAL MEDIA APP ****************************")
    n=0
    while True:
        print("press 1 to create Acoount")
        create_account = int(input())
        if create_account==1:
            name = input("Enter your name : ")
            mail = input("Enter your mail id : ")
            x = profile(name, mail)
            print(f"congratulation {name} your account is created successfully ")
            print("press 2 to view all the posts and to exit the app press n")
            while True:
                see_post = input()
                if see_post=="n":
                    print(f"Thank you {x.name}visit our app again ")
                    break
                elif see_post=="2":
                    for i in post.obj:
                        review_post(i,x)
                        see_in_detail(i)
                        print("The next post for you")
                    break
                else:
                    print("You have entered wrong key , enter again")
            print("press y if you want to create a post n for no")
            n = n+1
            create_post =input()
            if create_post == "y":
                content = input("Enter the content of the post")
                creativity = post(x,content)
            print("Thank you for visiting our app ")
            if n==2:
                break

profile_data.to_csv("D:/ inst.csv")
post_data.to_csv("D:/ instw.csv")
