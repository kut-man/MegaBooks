from telebot import types

books = {
    "Carrie": 'https://github.com/kut-man/MegaBooks/files/10951957/Stephen.King.-.Carrie.pdf',
    "IT": 'https://github.com/kut-man/MegaBooks/files/10951958/Stephen.King.-.It.pdf',
    "Bird Box": 'https://github.com/kut-man/MegaBooks/files/10951949/Bird.Box.pdf',
    "The Help": 'https://github.com/kut-man/MegaBooks/files/10951960/The.Help.pdf',
    "One Hundred Years of Solitude": 'https://github.com/kut-man/MegaBooks/files/10951954/One.Hundred.Years.of.Solitude.pdf',
    "Memoirs of a Geisha": 'https://github.com/kut-man/MegaBooks/files/10951953/Memoirs.of.a.Geisha.PDFDrive.pdf',
    "21 урок для XXI века": 'https://github.com/kut-man/MegaBooks/files/10951947/21.XXI.pdf',
    "Homo Deus": 'https://github.com/kut-man/MegaBooks/files/10951951/Homo.Deus.pdf',
    "Sapiens": 'https://github.com/kut-man/MegaBooks/files/10951956/Sapiens.pdf',
    "Harry Potter": '',
    "Robinson Crusoe": 'https://github.com/kut-man/MegaBooks/files/10951955/robinson-crusoe.pdf',
    "Fahrenheit_451": 'https://github.com/kut-man/MegaBooks/files/10951950/Fahrenheit_451.pdf',
    "Alice's Adventures in Wonderland": 'https://github.com/kut-man/MegaBooks/files/10951948/Alice.s.Adventures.in.Wonderland.pdf',
    "Little Women": 'https://github.com/kut-man/MegaBooks/files/10951952/LITTLE.WOMEN.pdf',
    "The Great Gatsby": 'https://github.com/kut-man/MegaBooks/files/10951959/The.Great.Gatsby.pdf',
    "Philosopher's Stone": 'https://github.com/kut-man/MegaBooks/files/10951940/01.Harry.Potter.and.the.Sorcerer.s.Stone.pdf',
    "Chamber of Secrets": 'https://github.com/kut-man/MegaBooks/files/10951941/02.Harry.Potter.and.the.Chamber.of.Secrets.pdf',
    "Prisoner of Azkaban": 'https://github.com/kut-man/MegaBooks/files/10951942/03.Harry.Potter.and.the.Prisoner.of.Azkaban.pdf',
    "Goblet of Fire": 'https://github.com/kut-man/MegaBooks/files/10951943/4_harry_potter_and_the_goblet_of_fire.pdf',
    "Order of the Phoenix": 'https://github.com/kut-man/MegaBooks/files/10951944/05.Harry.Potter.and.the.Order.of.the.Phoenix.pdf',
    "Half-Blood Prince": 'https://github.com/kut-man/MegaBooks/files/10951945/06.Harry.Potter.and.the.Half-Blood.Prince.pdf',
    "Deathly Hallows": 'https://github.com/kut-man/MegaBooks/files/10951946/07.Harry.Potter.and.the.Deathly.Hallows.pdf'
}

book_photos = ['https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1381972494l/6360296.jpg',
               'https://images-na.ssl-images-amazon.com/images/I/71dIjJTeOSL.jpg',
               'https://images-na.ssl-images-amazon.com/images/I/81SRiprjQSL.jpg',
               'https://images-na.ssl-images-amazon.com/images/I/81wSLYbTFYL.jpg',
               'https://lh3.googleusercontent.com/proxy/42zPU7rKI4713e8-bz8vu6VCRat_Un78ZF6XK1S2x1RNKK-3I-evjzPj9BJ9vd-xakna2c7KoS02ey-IMekSyGuaAOqYkrIukXMSihaRTzB2uxP7dgmjy76s1ff4mDtDMHQyPStNTkJV1v_5n_gp1Ml0Cv3yK5AsDdfl6Xl7o6w',
               'https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/9e23f652099375.590480dbf1908.png',
               'https://s1.livelib.ru/boocover/1003030762/o/137a/Yuval_Noj_Harari__21_urok_dlya_XXI_veka.jpeg',
               'https://www.rahvaraamat.ee/images/products/001/165/891/thumbnails/big/52636cf87b3d630540e342493c0e51876fa30dca/homo-deus-%D0%BA%D1%80%D0%B0%D1%82%D0%BA%D0%B0%D1%8F-%D0%B8%D1%81%D1%82%D0%BE%D1%80%D0%B8%D1%8F-%D0%B1%D1%83%D0%B4%D1%83%D1%89%D0%B5%D0%B3%D0%BE.jpg',
               'https://img-gorod.ru/26/022/2602293_detail.jpg',
               '',  # harry potter is not a book it is a collection of books.
               'https://m.media-amazon.com/images/I/51PxDr7bKxL._SL_300_.jpg',
               'https://images-na.ssl-images-amazon.com/images/I/71OFqSRFDgL.jpg',
               'https://blackwells.co.uk/jacket/l/9781447279990.jpg',
               'https://images-na.ssl-images-amazon.com/images/I/71eAXvgIrFL.jpg',
               'https://images-na.ssl-images-amazon.com/images/I/81djg0KWthS.jpg',
               'https://www.adazing.com/wp-content/uploads/2022/12/Harry-Potter-Book-Covers-Philosophers-Stone-us-2.jpg',
               'https://www.adazing.com/wp-content/uploads/2022/12/Harry-Potter-Book-Covers-Chamber-of-Secrets-us-1.png',
               'https://www.adazing.com/wp-content/uploads/2022/12/Harry-Potter-Book-Covers-Prisoner-of-Azkaban-us-1.png',
               'https://www.adazing.com/wp-content/uploads/2022/12/Harry-Potter-Book-Covers-Goblet-of-Fire-us-1.png',
               'https://www.adazing.com/wp-content/uploads/2022/12/Harry-Potter-Book-Covers-Order-of-the-Phoenix-us-1.png',
               'https://www.adazing.com/wp-content/uploads/2022/12/Harry-Potter-Book-Covers-Half-Blood-Prince-us-1.png',
               'https://www.adazing.com/wp-content/uploads/2022/12/Harry-Potter-Book-Covers-Deathly-Hallows-us-1-768x1154.png']


def catalog():
    markup_reply_catalog = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for k in books:
        book1 = types.KeyboardButton(k)
        markup_reply_catalog.add(book1)
    book_back = types.KeyboardButton("Back")
    markup_reply_catalog.add(book_back)
    return markup_reply_catalog


def harry():
    markup_reply_catalog = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for k in range(15, 22):
        book = types.KeyboardButton(list(books.keys())[k])
        markup_reply_catalog.add(book)
    book_back = types.KeyboardButton("Back")
    markup_reply_catalog.add(book_back)
    return markup_reply_catalog


def custom(number):
    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
    book1 = types.KeyboardButton(list(books.keys())[number])
    book2 = types.KeyboardButton(list(books.keys())[number+1])
    book3 = types.KeyboardButton(list(books.keys())[number+2])
    book_back = types.KeyboardButton("Back")

    markup_reply.add(book1, book2, book3, book_back)

    return markup_reply
