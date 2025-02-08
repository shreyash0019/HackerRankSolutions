import qrcode
generate_image = qrcode.make("https://www.youtube.com/watch?v=BOEWdGDAOYk")
generate_image.save('image.png')