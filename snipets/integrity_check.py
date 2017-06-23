# integrity check
from checksumdir import dirhash

if dirhash('../graphics', 'md5') == '5c1e58acacb3e51ee1dab67bca6ef033':
#               ^ Anpassen bei Bedarf
    print('[INFO]: Integrity check passed!')
else:
    print('[ERROR]: Integrity seems broken!')
    exit(1)
