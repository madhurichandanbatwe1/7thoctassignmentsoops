class media:
    def __init__(self,username):
        self.username=username
        self.posts=[]
    
    def add_posts(self,posts):
        self.posts.append(posts)
        return self.posts
    
    def display_posts(self):
        print(f'{self.username}')
        for posts in self.posts:
            print(posts)
              
    def search(self,keyword):
        for posts in self.posts:
            if f'{keyword}' in posts:
                print(posts)
priyavsmriti=media('priyav09')
priyavsmriti.add_posts('Not all days are bad')
priyavsmriti.add_posts("Keep calm and play hard")
priyavsmriti.add_posts('Word hard play hard')

priyavsmriti.display_posts()
priyavsmriti.search('hard')