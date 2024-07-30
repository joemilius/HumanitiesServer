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

membership1 = Membership(
    admin=True,
    user_id=user1.id,
    group_id=group1.id
)
membership2 = Membership(
    admin=True,
    user_id=user2.id,
    group_id=group2.id
)
membership3 = Membership(
    admin=True,
    user_id=user3.id,
    group_id=group3.id
)
membership4 = Membership(
    admin=False,
    user_id=user2.id,
    group_id=group3.id
)

movie1 = Movie(
    title='Avengers',
    image='alt',
    year='2012',
    director='Joss Whedon',
    cast='Robert Downy Jr.',
    description='Superheros save the world',
    group_id=group3.id
)

movie2 = Movie(
    title='SpaceJam',
    image='alt',
    year='2012',
    director='Joss Whedon',
    cast='Micheal Jordan',
    description='Basketball saves the world',
    group_id=group1.id
)

movie3 = Movie(
    title='Wolverine',
    image='alt',
    year='2012',
    director='Joss Whedon',
    cast='Hugh Jackman',
    description='Angsty superhero faces being an outcast',
    group_id=group2.id
)

music1 = Music(
    artist_name = "Radiohead",
    album_name = "Kid A",
    image = 'alt',
    year = '2003',
    description = 'follow up to OK Computer',
    group_id=group2.id
)

music2 = Music(
    artist_name = "Portishead",
    album_name = "I'm a woman",
    image = 'alt',
    year = '1995',
    description = 'triphop',
    group_id=group3.id
)

music1 = Music(
    artist_name = "Taylor Swift",
    album_name = "Red",
    image = 'alt',
    year = '2003',
    description = 'pop',
    group_id=group1.id
)