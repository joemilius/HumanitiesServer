from models import User, Group, Membership, Invitation, Movie, Book, Music, Movie_Comment, Book_Comment, Music_Comment

user1 = User(
    username='bugsy',
    email='bugsbunny@gmail.com',
    first_name='Bugs',
    last_name="Bunny",
    logins=1,
    password='1234'
)

user2 = User(
    username='quacker',
    email='howardtheduck@gmail.com',
    first_name='Howard',
    last_name='Duck',
    logins=3,
    password='1234',
)

user3 = User(
    username='spiderman',
    email='friendlyneighborhood@gmail.com',
    first_name='Peter',
    last_name='Parker',
    logins=4,
    password='1234'
)

group1 = Group(
    group_name="Loony Tunes"
)

group2 = Group(
    group_name="Space Lake"
)

group3 = Group(
    group_name="Marvel"
)