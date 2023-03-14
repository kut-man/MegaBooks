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
        'https://m.media-amazon.com/images/I/81MI6+TpYkL._AC_UF1000,1000_QL80_.jpg'],

    "Memoirs of a Geisha": [
        'https://github.com/kut-man/MegaBooks/files/10951953/Memoirs.of.a.Geisha.PDFDrive.pdf',
        'https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/9e23f652099375.590480dbf1908.png'],
    "21 урок для XXI века": [
        'https://github.com/kut-man/MegaBooks/files/10951947/21.XXI.pdf',
        'https://s1.livelib.ru/boocover/1003030762/o/137a/Yuval_Noj_Harari__21_urok_dlya_XXI_veka.jpeg'],
    "Homo Deus": [
        'https://github.com/kut-man/MegaBooks/files/10951951/Homo.Deus.pdf',
        'https://cv3.litres.ru/pub/c/cover_max1500/36300631.jpg'],
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


def catalog(start, end):
    markup_reply_catalog = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for k in range(start, end):
        book = types.KeyboardButton(list(books.keys())[k])
        markup_reply_catalog.add(book)
    book_back = types.KeyboardButton("Back")
    markup_reply_catalog.add(book_back)
    return markup_reply_catalog
