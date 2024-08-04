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
        password_hash='1234'
    )

    user2 = User(
        username='quacker',
        email='howardtheduck@gmail.com',
        first_name='Howard',
        last_name='Duck',
        logins=3,
        password_hash='1234',
    )

    user3 = User(
        username='spiderman',
        email='friendlyneighborhood@gmail.com',
        first_name='Peter',
        last_name='Parker',
        logins=4,
        password_hash='1234'
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

    db.session.commit()
    print("Seeding Complete")