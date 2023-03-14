from telebot import types

books = {
    "Carrie": [
        'https://github.com/kut-man/MegaBooks/files/10951957/Stephen.King.-.Carrie.pdf',
        'https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1381972494l/6360296.jpg'],

    "IT": [
        'https://github.com/kut-man/MegaBooks/files/10951958/Stephen.King.-.It.pdf',
        'https://images-na.ssl-images-amazon.com/images/I/71dIjJTeOSL.jpg'],

    "Bird Box": [
        'https://github.com/kut-man/MegaBooks/files/10951949/Bird.Box.pdf',
        'https://images-na.ssl-images-amazon.com/images/I/81SRiprjQSL.jpg'],

    "The Help": [
        'https://github.com/kut-man/MegaBooks/files/10951960/The.Help.pdf',
        'https://images-na.ssl-images-amazon.com/images/I/81wSLYbTFYL.jpg'],

    "One Hundred Years of Solitude": [
        'https://github.com/kut-man/MegaBooks/files/10951954/One.Hundred.Years.of.Solitude.pdf',
        'https://lh3.googleusercontent.com/proxy/42zPU7rKI4713e8-bz8vu6VCRat_Un78ZF6XK1S2x1RNKK-3I-evjzPj9BJ9vd-xakna2c7KoS02ey-IMekSyGuaAOqYkrIukXMSihaRTzB2uxP7dgmjy76s1ff4mDtDMHQyPStNTkJV1v_5n_gp1Ml0Cv3yK5AsDdfl6Xl7o6w'],

    "Memoirs of a Geisha": [
        'https://github.com/kut-man/MegaBooks/files/10951953/Memoirs.of.a.Geisha.PDFDrive.pdf',
        'https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/9e23f652099375.590480dbf1908.png'],
    "21 урок для XXI века": [
        'https://github.com/kut-man/MegaBooks/files/10951947/21.XXI.pdf',
        'https://s1.livelib.ru/boocover/1003030762/o/137a/Yuval_Noj_Harari__21_urok_dlya_XXI_veka.jpeg'],
    "Homo Deus": [
        'https://github.com/kut-man/MegaBooks/files/10951951/Homo.Deus.pdf',
        'https://www.rahvaraamat.ee/images/products/001/165/891/thumbnails/big/52636cf87b3d630540e342493c0e51876fa30dca/homo-deus-%D0%BA%D1%80%D0%B0%D1%82%D0%BA%D0%B0%D1%8F-%D0%B8%D1%81%D1%82%D0%BE%D1%80%D0%B8%D1%8F-%D0%B1%D1%83%D0%B4%D1%83%D1%89%D0%B5%D0%B3%D0%BE.jpg'],
    "Sapiens": [
        'https://github.com/kut-man/MegaBooks/files/10951956/Sapiens.pdf',
        'https://img-gorod.ru/26/022/2602293_detail.jpg'],
    "Harry Potter": '',
    "Robinson Crusoe": [
        'https://github.com/kut-man/MegaBooks/files/10951955/robinson-crusoe.pdf',
        'https://m.media-amazon.com/images/I/51PxDr7bKxL._SL_300_.jpg'],
    "Fahrenheit_451": [
        'https://github.com/kut-man/MegaBooks/files/10951950/Fahrenheit_451.pdf',
        'https://images-na.ssl-images-amazon.com/images/I/71OFqSRFDgL.jpg'],
    "Alice's Adventures in Wonderland": [
        'https://github.com/kut-man/MegaBooks/files/10951948/Alice.s.Adventures.in.Wonderland.pdf',
        'https://blackwells.co.uk/jacket/l/9781447279990.jpg'],
    "Little Women": [
        'https://github.com/kut-man/MegaBooks/files/10951952/LITTLE.WOMEN.pdf',
        'https://images-na.ssl-images-amazon.com/images/I/71eAXvgIrFL.jpg'],
    "The Great Gatsby": [
        'https://github.com/kut-man/MegaBooks/files/10951959/The.Great.Gatsby.pdf',
        'https://images-na.ssl-images-amazon.com/images/I/81djg0KWthS.jpg'],
    "Philosopher's Stone": [
        'https://github.com/kut-man/MegaBooks/files/10951940/01.Harry.Potter.and.the.Sorcerer.s.Stone.pdf',
        'https://www.adazing.com/wp-content/uploads/2022/12/Harry-Potter-Book-Covers-Philosophers-Stone-us-2.jpg'],
    "Chamber of Secrets": [
        'https://github.com/kut-man/MegaBooks/files/10951941/02.Harry.Potter.and.the.Chamber.of.Secrets.pdf',
        'https://www.adazing.com/wp-content/uploads/2022/12/Harry-Potter-Book-Covers-Chamber-of-Secrets-us-1.png'],
    "Prisoner of Azkaban": [
        'https://github.com/kut-man/MegaBooks/files/10951942/03.Harry.Potter.and.the.Prisoner.of.Azkaban.pdf',
        'https://www.adazing.com/wp-content/uploads/2022/12/Harry-Potter-Book-Covers-Prisoner-of-Azkaban-us-1.png'],
    "Goblet of Fire": [
        'https://github.com/kut-man/MegaBooks/files/10951943/4_harry_potter_and_the_goblet_of_fire.pdf',
        'https://www.adazing.com/wp-content/uploads/2022/12/Harry-Potter-Book-Covers-Goblet-of-Fire-us-1.png'],
    "Order of the Phoenix": [
        'https://github.com/kut-man/MegaBooks/files/10951944/05.Harry.Potter.and.the.Order.of.the.Phoenix.pdf',
        'https://www.adazing.com/wp-content/uploads/2022/12/Harry-Potter-Book-Covers-Order-of-the-Phoenix-us-1.png'],
    "Half-Blood Prince": [
        'https://github.com/kut-man/MegaBooks/files/10951945/06.Harry.Potter.and.the.Half-Blood.Prince.pdf',
        'https://www.adazing.com/wp-content/uploads/2022/12/Harry-Potter-Book-Covers-Half-Blood-Prince-us-1.png'],
    "Deathly Hallows": [
        'https://github.com/kut-man/MegaBooks/files/10951946/07.Harry.Potter.and.the.Deathly.Hallows.pdf',
        'https://www.adazing.com/wp-content/uploads/2022/12/Harry-Potter-Book-Covers-Deathly-Hallows-us-1-768x1154.png']
}


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
