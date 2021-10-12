./bat

%file_sizes%= read(file_size.txt)
curl 'https://up.ufile.io/v1/upload/create_session' \
-d 'file_size={%file_sizes%}'

> ./ fuid.txt