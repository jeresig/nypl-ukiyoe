PREFIX GROUPS

     4,830 images
     2,260 prefixes (1,100 w/matches)
     
     None
         NYPL/04MID/No-number1.jpg {u'Harunobu': 1}
         NYPL/04MID/No-number2.jpg {}
     100390
         NYPL/04MID/100390.a.jpg {u'Yoshitoshi': 3}
         NYPL/04MID/100390.b(F).jpg {u'Yoshitoshi': 4}
         NYPL/04MID/100390.b.jpg {u'Yoshitoshi': 5}
         NYPL/04MID/100390.c.jpg {u'Yoshitoshi': 5}
     101318
         NYPL/04MID/101318(F).jpg {}
         NYPL/04MID/101318(P).jpg {}

WEB (steve's localhost)

    (nypl)$ pip install flask Flask-PyMongo
    (nypl)$ python web.py

DATABASE (provisional)

     IMPORT
     $ python cache2store.py > store.json
     $ mongoimport --db nypl --collection images --drop --file store.json

     $ head -1 store.json | jsonlint
     {
       "matches": {
         "Yoshitoshi": 3
       },
       "prefix": "100390",
       "location": "https://ukiyo-e.org/upload/5640bfce5aba25c45df549d285725661",
       "fname": "NYPL/04MID/100390.a.jpg"
     }

     MONGOD (steve's localhost)
     $ cd ~/Code/nypl
     $ mongod --dbpath data/db
     
UPSEARCH

     $ head -3 matches.log
     Sat Jul 23 01:11:29 2016
     found 4832 uploads in NYPL/04MID/
     getting 4832 matches

     $ tail -12 matches.log
     Found 47% (2262/4832) matches.
     wrote matches_dict_1.py
     #1 Utamaro: 191
     #2 Hokusai: 189
     #3 Hokkei: 175
     #4 Harunobu: 145
     #5 Gakutei: 141
     #6 Unknown: 134
     #7 Kiyochika: 104
     #8 Yanagawa Shigenobu: 79
     #9 Hosoda Eishi: 59
     #10 Chikanobu: 56

MATCHES - Get/sample matching upsearch results.

     See `matches.py -h`.

     This script is also rerunnable. You can pass in cached match data:

     $ matches.py NYPL/04MID/ cache_04MID.py --cache cache_04MID_1.py

     Cache hits have curly braces:
     {1385} NYPL/04MID/113565.3.jpg {'Angy\xc3\xbbsai Enshi': 2} https://ukiyo-e.org/upload/f7165b4261d23ee250e613a291bfa35a
     [1386] NYPL/04MID/109266.a.jpg {} https://ukiyo-e.org/upload/1ededfed7e0e7cf728a02451ce7737c8
     [1387] NYPL/04MID/113352.b.jpg {} https://ukiyo-e.org/upload/80ab972264528a057890a3e110da7fb9
     {1388} NYPL/04MID/101519.a.jpg {'Yasuji': 1} https://ukiyo-e.org/upload/24cb1042ba60f545407501835c8ebb11

     NYPL/04MID/

     $ tail matches.log
     Found 41% (41/100) matches in sample (100/4832)
     wrote matches_dict.py
     #1 Hokkei: 6
     #2 Hokuba: 3
     #3 Harunobu: 3
     #4 Ogata Gekko: 2
     #5 Kunisada: 2
     #6 Unknown: 2
     #7 Yanagawa Shigenobu: 2
     #8 Shunsho: 2
     #9 Utamaro: 2
     #10 Gakutei: 2

     $ head matches_dict.py | fold | head
     matches = {'NYPL/04MID/96500.b.jpg': {'Hiroshige': 1}, 'NYPL/04MID/95096.a.jpg':
      {'Ikkei': 1, 'Unknown': 2}, 'NYPL/04MID/113187(P).jpg': {'Shigemasa': 2}, 'NYPL
     /04MID/113715/113722(F).jpg': {'Katsushika Taito II': 1}, 'NYPL/04MID/113619/113
     623(b).jpg': {'Harumasa': 2}, 'NYPL/04MID/63007.a.jpg': {'Yoshikazu': 5}, 'NYPL/
     04MID/101916.a.jpg': {'Ogata Gekko': 2}, 'NYPL/04MID/113414.jpg': {'Utamaro': 1}
     , 'NYPL/04MID/114092/114144(F).jpg': {'Hokuba': 1}, 'NYPL/04MID/114208/114283.jp
     g': {'Shunman': 1}, 'NYPL/04MID/109437.jpg': {'Hokkei': 1}, 'NYPL/04MID/101921.b
     .jpg': {'Ogata Gekko': 1}, 'NYPL/04MID/113675/113678.jpg': {'Gakutei': 1}, 'NYPL
     /04MID/113588.2.jpg': {'Toyokuni I': 1}, 'NYPL/04MID/113063.jpg': {'Harunobu': 4
     }, 'NYPL/04MID/101979.c.jpg': {'Kiyochika': 2}, 'NYPL/04MID/108505.a.jpg': {'Chi

     NYPL/05THUM/

     $ tail matches.log
     [92] 113400.jpg {'Utamaro': 1} https://ukiyo-e.org/upload/d3643d4b250c53ad3b05d37155725e80
     [93] 89279.jpg {'Hokusai': 24} https://ukiyo-e.org/upload/fb98fcaba1b06e804427c912c3a38289
     [94] 113207(P).jpg {} https://ukiyo-e.org/upload/076a3a53290efd7a268bf79de0a96c65
     [95] 109384(P).jpg {'Hokusai': 1} https://ukiyo-e.org/upload/7669ee5fea7408c840fa70c7a5fbba02
     [96] 109298.jpg {'Hokkei': 1} https://ukiyo-e.org/upload/dd7db82894b0a54253cd307889e34b2e
     [97] 109550b.jpg {'Kunisada': 2} https://ukiyo-e.org/upload/ce0e7f233178eae31336f91a03d9869b
     [98] 112974(F).jpg {} https://ukiyo-e.org/upload/ae31fc8b73ec6cf6db65191a4ca1455a
     [99] 109312.jpg {'Hiroshige': 11} https://ukiyo-e.org/upload/224bb4bdfd731676ab4497190e8722c1
     [100] 113603.1.jpg {'Toyohiro': 1} https://ukiyo-e.org/upload/06628d539e967b447f2e4cbfbd5d5606
     48% (48/100) matches in sample (100/1300)     

UPLOADER

     See `upload.py -h`, `pydoc uploader`, and uploader.log
     Uploader class: uploader.py
     Uploader tests: uploader_tests.py
     upload script: upload.py
     upload log: uploader.log
     virtualenv: nypl

     You can try a "dry run" like this:
     $ workon nypl
     (nypl)$ ./upload.py https://ukiyo-e.org/upload NYPL/05THUM --dry --limit 3

     REQUIREMENTS
     See `uploader_requirements.txt`

     NEEDED PACKAGES
     sudo apt-get install python-pip
     sudo apt-get install python-virtualenv
     sudo apt-get install build-essential libssl-dev libffi-dev python-dev

SIMILAR IMAGES

     [2] NYPL/05THUM/100390.b(F).jpg 302 https://ukiyo-e.org/upload/7eaf13ebd58e2ea7ca2b49a21f740a6f
     [3] NYPL/05THUM/100390.b.jpg 302 https://ukiyo-e.org/upload/1b2a902580aa1b20930be7f662c8b7f1

FILETYPES

     NYPL$ find 05THUM/ -type f | sed -e 's/.*\.//'| sort | uniq -c
        4832 jpg
          20 db
           6 upload
           2 2
     NYPL$ find 04MID/ -type f | sed -e 's/.*\.//'| sort | uniq -c
        4832 jpg
          19 db
           3 upload
     NYPL$ find 03JPG/ -type f | sed -e 's/.*\.//'| sort | uniq -c
        4832 jpg
          20 db
     NYPL$ find 02TIF/ -type f | sed -e 's/.*\.//'| sort | uniq -c
        4832 tif
          20 db
     NYPL$ find 01RAW/ -type f | sed -e 's/.*\.//'| sort | uniq -c
        4832 nksc
        4832 nef
          19 db

"dup" DIRECTORIES

     NYPL$ ls -lh 0*/dup/ | head; ls -lh 0*/dup/ | tail
     01RAW/dup/:
     total 128M
     -rw-r--r-- 1 ubuntu ubuntu  43M Jul 12 09:42 101989.ax.nef
     -rw-r--r-- 1 ubuntu ubuntu  43M Jul 12 09:42 101989.bx.nef
     -rw-r--r-- 1 ubuntu ubuntu  42M Jul 12 09:42 101989.cx.nef
     drwxr-xr-x 2 ubuntu ubuntu 4.0K Jul 12 09:42 NKSC_PARAM
     -rw-r--r-- 1 ubuntu ubuntu 835K Jul 12 09:42 Thumbs.db
     
     02TIF/dup/:
     total 122M
     -rw-r--r-- 1 ubuntu ubuntu 454K Jul 12 11:51 101989.bx.jpg
     -rw-r--r-- 1 ubuntu ubuntu 430K Jul 12 11:51 101989.cx.jpg
     -rw-r--r-- 1 ubuntu ubuntu 1.2M Jul 12 11:51 Thumbs.db
     
     05THUM/dup/:
     total 532K
     -rw-r--r-- 1 ubuntu ubuntu 3.3K Jul 12 11:51 101989.ax.jpg
     -rw-r--r-- 1 ubuntu ubuntu 2.7K Jul 12 11:51 101989.bx.jpg
     -rw-r--r-- 1 ubuntu ubuntu 2.3K Jul 12 11:51 101989.cx.jpg
     -rw-r--r-- 1 ubuntu ubuntu 517K Jul 12 11:51 Thumbs.db

CONTENTS

     NYPL$ ls -lh 01RAW/ | head; ls -lh 01RAW/ | tail
     total 125G
     -rw-r--r-- 1 ubuntu ubuntu  42M Jul 12 07:11 100390.a.nef
     -rw-r--r-- 1 ubuntu ubuntu  43M Jul 12 07:11 100390.b(F).nef
     -rw-r--r-- 1 ubuntu ubuntu  43M Jul 12 07:11 100390.b.nef
     -rw-r--r-- 1 ubuntu ubuntu  42M Jul 12 07:11 100390.c.nef
     -rw-r--r-- 1 ubuntu ubuntu  46M Jul 12 07:11 101318(F).nef
     -rw-r--r-- 1 ubuntu ubuntu  48M Jul 12 07:12 101318(P).nef
     -rw-r--r-- 1 ubuntu ubuntu  44M Jul 12 07:12 101503.a.nef
     -rw-r--r-- 1 ubuntu ubuntu  45M Jul 12 07:12 101503.b(F).nef
     -rw-r--r-- 1 ubuntu ubuntu  43M Jul 12 07:12 101503.b.nef
     -rw-r--r-- 1 ubuntu ubuntu  48M Jul 12 09:42 98377.nef
     -rw-r--r-- 1 ubuntu ubuntu  48M Jul 12 09:42 98377(P).nef
     -rw-r--r-- 1 ubuntu ubuntu  45M Jul 12 09:42 99728.a.nef
     -rw-r--r-- 1 ubuntu ubuntu  44M Jul 12 09:42 99728.b.nef
     drwxr-xr-x 3 ubuntu ubuntu 4.0K Jul 12 09:42 dup
     -rw-r--r-- 1 ubuntu ubuntu  47M Jul 12 09:42 missing number01.nef
     -rw-r--r-- 1 ubuntu ubuntu  47M Jul 12 09:42 missing number02.nef
     drwxr-xr-x 2 ubuntu ubuntu 112K Jul 12 09:42 NKSC_PARAM
     -rw-r--r-- 1 ubuntu ubuntu  46M Jul 12 09:42 No-number1.nef
     -rw-r--r-- 1 ubuntu ubuntu  45M Jul 12 09:42 No-number2.nef
     
     NYPL$ ls -lh 02TIF/ | head; ls -lh 02TIF/ | tail
     total 138G
     -rw-r--r-- 1 ubuntu ubuntu  38M Jul 12 09:42 100390.a.tif
     -rw-r--r-- 1 ubuntu ubuntu  48M Jul 12 09:42 100390.b(F).tif
     -rw-r--r-- 1 ubuntu ubuntu  46M Jul 12 09:42 100390.b.tif
     -rw-r--r-- 1 ubuntu ubuntu  44M Jul 12 09:42 100390.c.tif
     -rw-r--r-- 1 ubuntu ubuntu  40M Jul 12 09:42 101318(F).tif
     -rw-r--r-- 1 ubuntu ubuntu  44M Jul 12 09:42 101318(P).tif
     -rw-r--r-- 1 ubuntu ubuntu  57M Jul 12 09:42 101503.a.tif
     -rw-r--r-- 1 ubuntu ubuntu  60M Jul 12 09:42 101503.b(F).tif
     -rw-r--r-- 1 ubuntu ubuntu  64M Jul 12 09:42 101503.b(P).tif
     -rw-r--r-- 1 ubuntu ubuntu  61M Jul 12 11:38 98377(P).tif
     -rw-r--r-- 1 ubuntu ubuntu  52M Jul 12 11:38 98377.tif
     -rw-r--r-- 1 ubuntu ubuntu  57M Jul 12 11:38 99728.a.tif
     -rw-r--r-- 1 ubuntu ubuntu  55M Jul 12 11:38 99728.b.tif
     drwxr-xr-x 2 ubuntu ubuntu 4.0K Jul 12 11:38 dup
     -rw-r--r-- 1 ubuntu ubuntu  44M Jul 12 11:38 missing number01.tif
     -rw-r--r-- 1 ubuntu ubuntu  48M Jul 12 11:38 missing number02.tif
     -rw-r--r-- 1 ubuntu ubuntu  50M Jul 12 11:38 No-number1.tif
     -rw-r--r-- 1 ubuntu ubuntu  49M Jul 12 11:38 No-number2.tif
     -rw-r--r-- 1 ubuntu ubuntu 246K Jul 12 11:38 Thumbs.db
     
     NYPL$ ls -lh 03JPG/ | head; ls -lh 03JPG/ | tail
     total 10G
     -rw-r--r-- 1 ubuntu ubuntu 2.0M Jul 12 11:38 100390.a.jpg
     -rw-r--r-- 1 ubuntu ubuntu 3.2M Jul 12 11:38 100390.b(F).jpg
     -rw-r--r-- 1 ubuntu ubuntu 2.7M Jul 12 11:38 100390.b.jpg
     -rw-r--r-- 1 ubuntu ubuntu 2.4M Jul 12 11:38 100390.c.jpg
     -rw-r--r-- 1 ubuntu ubuntu 2.4M Jul 12 11:38 101318(F).jpg
     -rw-r--r-- 1 ubuntu ubuntu 3.4M Jul 12 11:38 101318(P).jpg
     -rw-r--r-- 1 ubuntu ubuntu 4.0M Jul 12 11:38 101503.a.jpg
     -rw-r--r-- 1 ubuntu ubuntu 4.9M Jul 12 11:38 101503.b(F).jpg
     -rw-r--r-- 1 ubuntu ubuntu 3.8M Jul 12 11:38 101503.b.jpg
     -rw-r--r-- 1 ubuntu ubuntu 3.2M Jul 12 11:49 98377.jpg
     -rw-r--r-- 1 ubuntu ubuntu 5.2M Jul 12 11:49 98377(P).jpg
     -rw-r--r-- 1 ubuntu ubuntu 4.5M Jul 12 11:49 99728.a.jpg
     -rw-r--r-- 1 ubuntu ubuntu 4.3M Jul 12 11:49 99728.b.jpg
     drwxr-xr-x 2 ubuntu ubuntu 4.0K Jul 12 11:49 dup
     -rw-r--r-- 1 ubuntu ubuntu 3.2M Jul 12 11:49 missing number01.jpg
     -rw-r--r-- 1 ubuntu ubuntu 3.7M Jul 12 11:49 missing number02.jpg
     -rw-r--r-- 1 ubuntu ubuntu 3.2M Jul 12 11:49 No-number1.jpg
     -rw-r--r-- 1 ubuntu ubuntu 3.8M Jul 12 11:49 No-number2.jpg
     -rw-r--r-- 1 ubuntu ubuntu 716K Jul 12 11:49 Thumbs.db
     
     NYPL$ ls -lh 04MID/ | head; ls -lh 04MID/ | tail
     total 2.2G
     -rw-r--r-- 1 ubuntu ubuntu  352K Jul 12 11:49 100390.a.jpg
     -rw-r--r-- 1 ubuntu ubuntu  579K Jul 12 11:49 100390.b(F).jpg
     -rw-r--r-- 1 ubuntu ubuntu  496K Jul 12 11:49 100390.b.jpg
     -rw-r--r-- 1 ubuntu ubuntu  446K Jul 12 11:49 100390.c.jpg
     -rw-r--r-- 1 ubuntu ubuntu  489K Jul 12 11:49 101318(F).jpg
     -rw-r--r-- 1 ubuntu ubuntu  756K Jul 12 11:49 101318(P).jpg
     -rw-r--r-- 1 ubuntu ubuntu  859K Jul 12 11:49 101503.a.jpg
     -rw-r--r-- 1 ubuntu ubuntu  980K Jul 12 11:49 101503.b(F).jpg
     -rw-r--r-- 1 ubuntu ubuntu  789K Jul 12 11:49 101503.b.jpg
     -rw-r--r-- 1 ubuntu ubuntu  628K Jul 12 11:51 96656.9.jpg
     -rw-r--r-- 1 ubuntu ubuntu  724K Jul 12 11:51 98377.jpg
     -rw-r--r-- 1 ubuntu ubuntu  998K Jul 12 11:51 98377(P).jpg
     -rw-r--r-- 1 ubuntu ubuntu  893K Jul 12 11:51 99728.a.jpg
     -rw-r--r-- 1 ubuntu ubuntu  883K Jul 12 11:51 99728.b.jpg
     drwxr-xr-x 2 ubuntu ubuntu  4.0K Jul 12 11:51 dup
     -rw-r--r-- 1 ubuntu ubuntu  854K Jul 12 11:51 missing number01.jpg
     -rw-r--r-- 1 ubuntu ubuntu  972K Jul 12 11:51 missing number02.jpg
     -rw-r--r-- 1 ubuntu ubuntu  660K Jul 12 11:51 No-number1.jpg
     -rw-r--r-- 1 ubuntu ubuntu  894K Jul 12 11:51 No-number2.jpg
     
     NYPL$ ls -lh 05THUM/ | head; ls -lh 05THUM/ | tail
     total 16M
     -rw-r--r-- 1 ubuntu ubuntu 2.7K Jul 12 11:51 100390.a.jpg
     -rw-r--r-- 1 ubuntu ubuntu 3.3K Jul 12 11:51 100390.b(F).jpg
     -rw-r--r-- 1 ubuntu ubuntu 3.3K Jul 12 11:51 100390.b.jpg
     -rw-r--r-- 1 ubuntu ubuntu 3.6K Jul 12 11:51 100390.c.jpg
     -rw-r--r-- 1 ubuntu ubuntu 4.8K Jul 12 11:51 101318(F).jpg
     -rw-r--r-- 1 ubuntu ubuntu 5.2K Jul 12 11:51 101318(P).jpg
     -rw-r--r-- 1 ubuntu ubuntu 4.6K Jul 12 11:51 101503.a.jpg
     -rw-r--r-- 1 ubuntu ubuntu 4.9K Jul 12 11:51 101503.b(F).jpg
     -rw-r--r-- 1 ubuntu ubuntu 4.7K Jul 12 11:51 101503.b.jpg
     -rw-r--r-- 1 ubuntu ubuntu 3.4K Jul 12 11:51 98377.jpg
     -rw-r--r-- 1 ubuntu ubuntu 3.4K Jul 12 11:51 98377(P).jpg
     -rw-r--r-- 1 ubuntu ubuntu 4.7K Jul 12 11:51 99728.a.jpg
     -rw-r--r-- 1 ubuntu ubuntu 4.4K Jul 12 11:51 99728.b.jpg
     drwxr-xr-x 2 ubuntu ubuntu 4.0K Jul 12 11:51 dup
     -rw-r--r-- 1 ubuntu ubuntu 4.0K Jul 12 11:51 missing number01.jpg
     -rw-r--r-- 1 ubuntu ubuntu 3.7K Jul 12 11:51 missing number02.jpg
     -rw-r--r-- 1 ubuntu ubuntu 3.7K Jul 12 11:51 No-number1.jpg
     -rw-r--r-- 1 ubuntu ubuntu 4.2K Jul 12 11:51 No-number2.jpg
     -rw-r--r-- 1 ubuntu ubuntu 362K Jul 12 11:51 Thumbs.db

TRIPTYCH

     $ grep ^Location */*.upload*
     05THUM/101989.a.jpg.upload:Location: https://ukiyo-e.org/upload/fa79554eb747f6f79ef903f81b816eb0
     05THUM/101989.a.jpg.upload.2:Location: https://ukiyo-e.org/upload/66647ff45ce8f94590d88fa3bc29bdd9
     05THUM/101989.b.jpg.upload.2:Location: https://ukiyo-e.org/upload/f0d2bcc76116cfe1b488e9e197d52884
     05THUM/101989.c.jpg.upload:Location: https://ukiyo-e.org/upload/36fe1cf6acd61c0c25685c333de23193

ABOUT the ".nksc" (sidecar) files

     <http://imaging.nikon.com/lineup/microsite/capturenxd/about/>

UPLOAD

     curl -F "file=@98377.jpg" -i https://ukiyo-e.org/upload
     https://ukiyo-e.org/upload/414bd957d311703f4bc08d8155963395
     https://ukiyo-e.org/upload/414bd957d311703f4bc08d8155963395?type=json
