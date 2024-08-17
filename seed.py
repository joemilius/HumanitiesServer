from models import db, User, Group, Membership, Invitation, Movie, Book, Music, Movie_Comment, Book_Comment, Music_Comment
from app import app

with app.app_context():

    User.query.delete()
    Group.query.delete()
    Membership.query.delete()
    Movie.query.delete()
    Music.query.delete()
    Book.query.delete()

    print("Creating Users ...")
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
    
    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)

    print("Creating Groups ...")

    group1 = Group(
        group_name="Loony Tunes"
    )

    group2 = Group(
        group_name="Space Lake"
    )

    group3 = Group(
        group_name="Marvel"
    )

    db.session.add(group1)
    db.session.add(group2)
    db.session.add(group3)
    print(group1.id)

    print("Creating Memberships ...")

    membership1 = Membership(
        admin=True,
        user=user1,
        group=group1
    )
    membership2 = Membership(
        admin=True,
        user=user2,
        group=group2
    )
    membership3 = Membership(
        admin=True,
        user=user3,
        group=group3
    )
    membership4 = Membership(
        admin=False,
        user=user2,
        group=group3
    )

    db.session.add(membership1)
    db.session.add(membership2)
    db.session.add(membership3)
    db.session.add(membership4)

    print("Creating Movies ...")

    movie1 = Movie(
        title='Avengers',
        image='alt',
        year='2012',
        director='Joss Whedon',
        cast='Robert Downy Jr.',
        description='Superheros save the world',
        group=group3
    )

    movie2 = Movie(
        title='SpaceJam',
        image='alt',
        year='2012',
        director='Joss Whedon',
        cast='Micheal Jordan',
        description='Basketball saves the world',
        group=group1
    )

    movie3 = Movie(
        title='Wolverine',
        image='alt',
        year='2012',
        director='Joss Whedon',
        cast='Hugh Jackman',
        description='Angsty superhero faces being an outcast',
        group=group2
    )

    db.session.add(movie1)
    db.session.add(movie2)
    db.session.add(movie3)

    music1 = Music(
        artist_name = "Radiohead",
        album_name = "Kid A",
        image = 'alt',
        year = '2003',
        description = 'follow up to OK Computer',
        group=group2
    )

    music2 = Music(
        artist_name = "Portishead",
        album_name = "I'm a woman",
        image = 'alt',
        year = '1995',
        description = 'triphop',
        group=group3
    )

    print("Creating Music ...")

    music3 = Music(
        artist_name = "Taylor Swift",
        album_name = "Red",
        image = 'alt',
        year = '2003',
        description = 'pop',
        group=group1
    )

    db.session.add(music1)
    db.session.add(music2)
    db.session.add(music3)

    print("Creating Books ...")

    book1 = Book(
        title = 'Catch 22',
        author = 'Joseph Heller',
        image = 'alt',
        description = 'the absurdity of war',
        group=group1
    )

    book2 = Book(
        title = 'Foundation',
        author = 'Isaac Asimov',
        image = 'alt',
        description = 'sci-fi predictive measures ensure the continuation of civilization',
        group=group2
    )
    book3 = Book(
        title = 'Superfolks',
        author = 'Robert Mayer',
        image = 'alt',
        description = 'what happens to superheros as they age',
        group=group3
    )
    
    db.session.add(book1)
    db.session.add(book2)
    db.session.add(book3)

    print("Creating Invitations ...")

    invitation1 = Invitation(
        message = "I would like to join",
        accepted = False,
        user = user1,
        group = group3
    )

    invitation2 = Invitation(
        message = "I would like to join",
        accepted = False,
        user = user3,
        group = group1
    )

    db.session.add(invitation1)
    db.session.add(invitation2)

    print("Creating Movie_Comments ... ")

    movie_comment1 = Movie_Comment(
        stars=5,
        content='Super good',
        movie=movie2,
        user=user1
    )

    movie_comment2 = Movie_Comment(
        stars=5,
        content='Super good',
        movie=movie1,
        user=user3
    )
    movie_comment3 = Movie_Comment(
        stars=5,
        content='Super good',
        movie=movie3,
        user=user2
    )

    db.session.add(movie_comment1)
    db.session.add(movie_comment2)
    db.session.add(movie_comment3)

    print("Creating Music_Comments ...")

    music_comment1 = Music_Comment(
        stars=4,
        content='Super good',
        music=music1,
        user=user2
    )

    music_comment2 = Music_Comment(
        stars=4,
        content='Super good',
        music=music2,
        user=user3
    )

    music_comment3 = Music_Comment(
        stars=4,
        content='Super good',
        music=music3,
        user=user1
    )

    db.session.add(music_comment1)
    db.session.add(music_comment2)
    db.session.add(music_comment3)

    print("Creating Book_Comments ...")

    book_comment1 = Book_Comment(
        stars=4,
        content='Super good',
        book=book1,
        user=user1
    )

    book_comment2 = Book_Comment(
        stars=4,
        content='Super good',
        book=book2,
        user=user2
    )

    book_comment3 = Book_Comment(
        stars=4,
        content='Super good',
        book=book3,
        user=user3
    )

    db.session.add(book_comment1)
    db.session.add(book_comment2)
    db.session.add(book_comment3)


    db.session.commit()
    print("Seeding Complete")