from telebot import types

books = ['Carrie', 'IT', 'Bird Box', 'The Help',
         'One Hundred Years of Solitude', 'Memoirs of a Geisha', '21 урок для XXI века', 'Homo Deus', 'Sapiens',
         'Harry Potter', 'Robinson Crusoe', 'Fahrenheit_451', "Alice's Adventures in Wonderland", 'Little Women',
         'The Great Gatsby']

book_photos = ['https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1381972494l/6360296.jpg',
               'https://images-na.ssl-images-amazon.com/images/I/71dIjJTeOSL.jpg',
               'https://images-na.ssl-images-amazon.com/images/I/81SRiprjQSL.jpg',
               'https://images-na.ssl-images-amazon.com/images/I/81wSLYbTFYL.jpg',
               'https://lh3.googleusercontent.com/proxy/42zPU7rKI4713e8-bz8vu6VCRat_Un78ZF6XK1S2x1RNKK-3I-evjzPj9BJ9vd-xakna2c7KoS02ey-IMekSyGuaAOqYkrIukXMSihaRTzB2uxP7dgmjy76s1ff4mDtDMHQyPStNTkJV1v_5n_gp1Ml0Cv3yK5AsDdfl6Xl7o6w',
               'https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/9e23f652099375.590480dbf1908.png',
               'https://s1.livelib.ru/boocover/1003030762/o/137a/Yuval_Noj_Harari__21_urok_dlya_XXI_veka.jpeg',
               'https://www.rahvaraamat.ee/images/products/001/165/891/thumbnails/big/52636cf87b3d630540e342493c0e51876fa30dca/homo-deus-%D0%BA%D1%80%D0%B0%D1%82%D0%BA%D0%B0%D1%8F-%D0%B8%D1%81%D1%82%D0%BE%D1%80%D0%B8%D1%8F-%D0%B1%D1%83%D0%B4%D1%83%D1%89%D0%B5%D0%B3%D0%BE.jpg',
               'https://img-gorod.ru/26/022/2602293_detail.jpg',
               'https://kbimages1-a.akamaihd.net/5214c13c-52c9-4d8e-b50e-d8848657ce93/1200/1200/False/harry-potter-the-complete-collection-1-7-1.jpg',
               'https://m.media-amazon.com/images/I/51PxDr7bKxL._SL_300_.jpg',
               'https://images-na.ssl-images-amazon.com/images/I/71OFqSRFDgL.jpg',
               'https://blackwells.co.uk/jacket/l/9781447279990.jpg',
               'https://images-na.ssl-images-amazon.com/images/I/71eAXvgIrFL.jpg',
               'https://images-na.ssl-images-amazon.com/images/I/81djg0KWthS.jpg']

pdf_links = ['https://github.com/kut_man/Pong_Final_JavaFX/files/6573828/Carrie.Stephen_King.pdf',
             'https://github.com/kut_man/Pong_Final_JavaFX/files/6573830/IT.Stephen.King.pdf',
             'https://github.com/kut_man/Pong_Final_JavaFX/files/6573827/Bird.Box.pdf',
             'https://github.com/kut_man/Pong_Final_JavaFX/files/6573825/The.Help.Kathryn.Stockett.pdf',
             'https://github.com/kut_man/Pong_Final_JavaFX/files/6573824/One.Hundred.Years.Of.Solitude.pdf',
             'https://github.com/kut_man/Pong_Final_JavaFX/files/6573823/Memoirs.of.a.Geisha.pdf',
             'https://github.com/kut_man/Pong_Final_JavaFX/files/6573839/21.XXI.pdf',
             'https://github.com/kut_man/Pong_Final_JavaFX/files/6573840/Homo.Deus.pdf',
             'https://github.com/kut_man/Pong_Final_JavaFX/files/6573842/Homo.Sapiens.pdf',
             'https://github.com/kut_man/Pong_Final_JavaFX/files/6573818/Harry.Potter.pdf,'
             'https://github.com/kut_man/Pong_Final_JavaFX/files/6573821/Robinson.Crusoe.pdf',
             'https://github.com/kut_man/Pong_Final_JavaFX/files/6573803/Fahrenheit_451.pdf',
             'https://github.com/kut_man/Pong_Final_JavaFX/files/6573832/Alice.s.Adventures.in.Wonderland.pdf',
             'https://github.com/kut_man/Pong_Final_JavaFX/files/6573835/Little.Women.pdf',
             'https://github.com/kut_man/Pong_Final_JavaFX/files/6573836/The.Great.Gatsby.pdf']


def catalog():
    markup_reply_catalog = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for k in books:
        book1 = types.KeyboardButton(k)
        markup_reply_catalog.add(book1)
    book_back = types.KeyboardButton("Back")
    markup_reply_catalog.add(book_back)
    return markup_reply_catalog


def horror():
    markup_reply_horror = types.ReplyKeyboardMarkup(resize_keyboard=True)
    book1 = types.KeyboardButton("Carrie")
    book2 = types.KeyboardButton("IT")
    book3 = types.KeyboardButton("Bird Box")
    book_back = types.KeyboardButton("Back")

    markup_reply_horror.add(book1, book2, book3, book_back)

    return markup_reply_horror


def historical():
    markup_reply_historical = types.ReplyKeyboardMarkup(resize_keyboard=True)
    book4 = types.KeyboardButton("The Help")
    book5 = types.KeyboardButton("One Hundred Years of Solitude")
    book6 = types.KeyboardButton("Memoirs of a Geisha")
    book_back = types.KeyboardButton("Back")

    markup_reply_historical.add(book4, book5, book6, book_back)

    return markup_reply_historical


def russian():
    markup_reply_russian = types.ReplyKeyboardMarkup(resize_keyboard=True)
    book7 = types.KeyboardButton("21 урок для XXI века")
    book8 = types.KeyboardButton("Homo Deus")
    book9 = types.KeyboardButton("Sapiens")
    book_back = types.KeyboardButton("Back")

    markup_reply_russian.add(book7, book8, book9, book_back)

    return markup_reply_russian


def fantasy():
    markup_reply_fantasy = types.ReplyKeyboardMarkup(resize_keyboard=True)
    book10 = types.KeyboardButton("Harry Potter")
    book11 = types.KeyboardButton("Robinson Crusoe")
    book12 = types.KeyboardButton("Fahrenheit_451")
    book_back = types.KeyboardButton("Back")

    markup_reply_fantasy.add(book10, book11, book12, book_back)

    return markup_reply_fantasy


def novels():
    markup_reply_detective = types.ReplyKeyboardMarkup(resize_keyboard=True)
    book13 = types.KeyboardButton("Alice's Adventures in Wonderland")
    book14 = types.KeyboardButton("Little Women")
    book15 = types.KeyboardButton("The Great Gatsby")
    book_back = types.KeyboardButton("Back")

    markup_reply_detective.add(book13, book14, book15, book_back)

    return markup_reply_detective