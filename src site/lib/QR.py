import qrcode 
import threading
import os
import time



def makeQR(link, filename, color):
    qr = qrcode.QRCode(version=1, box_size=10, border=5) 
    qr.add_data(link)
    qr.make(fit = True)
    img = qr.make_image(fill_color = color, 
                        back_color = 'black') 
    img.save('static/{0}.png'.format(filename))
    return link, filename

def delete(file):
    time.sleep(20)
    os.remove('static/{0}.png'.format(file))

remove_later = lambda file: threading.Thread(target=delete, args=(file, )).start()


if __name__ == '__main__':
    print(makeQR('https://google.com', 'try', 'red'))