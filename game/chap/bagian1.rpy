label bagian1:
    window hide
    call screen sesi(1)
    scene kelas with fade
    show budayu with dissolve
    bdy "Hmm.. hari ini hanya ibu yang dapat mengisi jam pelajaran ya.. "
    show budayu mlt_standar1
    bdy "Jadi apa yang kalian ributkan selama jam kosong? Selain menjiplak jawaban teman."
    show santi mt_lirik papan at left with dissolve
    show budayu mlt_standar
    snt "..."
    show santi mt_standar mlt_standar1
    snt "Tadi kami membahas tentang Tumpek Landep, bu."
    hide santi with dissolve
    show budayu mt_lirik mlt_standar1
    bdy "Kalian membahas hari suci yang dirayakan hari ini ya? kebetulan sekali sekarang materi kita adalah tentang hari suci."
    show budayu mt_standar mlt_standar
    bdy "Jadi apa yang kalian ketahui tentang Tumpek Landep?"
    show santi mlt_senyum papan at left with dissolve
    snt "Hari dimana kita diingatkan untuk mempertajam pikiran."
    show budayu mlt_senyum
    bdy "Pintar. [snt], kamu langsung menjawab makna filosofisnya."
    show santi mt_pejam
    show budayu mt_pejam mlt_senyum1
    show gita als_bingung mt_standar at right with dissolve
    bdy "Seperti biasa kamu tidak pernah mengecewakan."
    show gita als_marah mt_lirik
    gta "..."
    hide gita 
    hide santi
    with dissolve
    show budayu mt_standar mlt_senyum
    bdy "Baiklah, agar teman-teman yang lain juga paham, biar ibu jelaskan sedikit poin pentingnya untuk kalian."
    
    scene pop3_bg with fade
    show pop3_ppn with moveintop
    show budayu at left with moveinleft
    pause 0.5
    show pop3a with dissolve
    show budayu mlt_standar
    bdy "Tumpek Landep terjadi setiap hari sabtu kliwon wuku Landep."
    show pop3b
    show budayu mt_lirik mlt_standar1
    bdy "Kata “Landep” di sini berarti “Tajam”"
    show budayu mt_standar mlt_standar
    show pop3c
    bdy "Secara harfiah tajam di sini merujuk pada senjata besi seperti keris, tombak, pisau, sabit, dan sebagainya."
    show budayu
    show pop3d
    bdy "Namun secara filosofis, tajam yang dimaksud adalah “ketajaman pikiran”."
    show pop3e
    show budayu mt_lirik mlt_senyum
    bdy "Ada yang tahu apa yang dimaksud dengan ketajaman pikiran?"

    jump choice_bagian1_1

    label  choice_bagian1_1:
        scene pop3_bg
        show pop3_ppn
        show budayu als_standar mt_standar mlt_standar at left 
        show pop3a
        show pop3b
        show pop3c
        show pop3d
        show pop3e
        menu:
            "Pikiran menusuk":
                mnk als_bingung mt_mikir mlt_standar1 efk_keringat "Pikiran menusuk."
                show budayu als_bingung mt_pejam
                gta "Pfft..!"
                glg "Kenapa tidak sekalian “pikiran memotong, mengiris, mencincang”?"
                "Siswa-siswi" "Hahaha!" with hpunch
                show budayu als_marah mt_standar mlt_teriak
                bdy "Tenang semuanya!" with vpunch
                show budayu als_standar mlt_standar1
                bdy "“Pikiran menusuk” dalam puisi bisa diartikan sebagai pikiran yang menyakitkan."
                show budayu mlt_standar
                bdy "Apakah itu yang kamu maksudkan [mnk]?"
                show budayu als_bingung
                mnk als_bingung mt_mikir efk_cemas "Emm.. tidak tahu, bu. Saya hanya menebak."
                show budayu als_marah mt_pejam mlt_standar1 efk_x
                bdy "..."
                show budayu mt_standar mlt_teriak
                bdy "Kalau jawab itu yang serius! Sudah menyontek! sekarang di jam pelajaran kamu masih gak mau serius?!" with vpunch
                mnk als_sedih mt_cemas mlt_standar efk_cemas "..m-maaf, bu..!"
                show budayu mlt_standar1
                "..."
                "Seketika semua kelas kembali hening."

            "Kemampun berpikir kritis":
                mnk mlt_senyum1 "Kemampuan berpikir kritis."
                show budayu mt_pejam mlt_senyum
                bdy "Benar."

            "Mengingat semua informasi":
                mnk als_bingung mt_mikir mlt_standar1 "Mengingat semua informasi."
                show budayu mlt_standar1
                bdy "Mengingat semua informasi itu lebih berkaitan dengan daya ingat, sedangkan ketajaman pikiran itu berkaitan dengan kemampuan menganalisis informasi."

    scene pop3_bg
    show pop3_ppn
    show budayu at left 
    show pop3a
    show pop3b
    show pop3c
    show pop3d
    show pop3e
    show budayu mlt_standar
    show pop3f
    bdy "Ketajaman pikiran berarti kemampuan berpikir kritis."
    show budayu mlt_standar1
    show pop3g
    bdy "Orang yang berpikir kritis akan menganalisis informasi sebelum menyimpulkan sesuatu."
    show budayu mlt_standar
    show pop3h
    bdy "Sederhananya, mereka akan mempertimbangkan sebab-akibat dan baik-buruk sebelum mengambil keputusan dalam hidup."
    show budayu mlt_standar1
    bdy "Contohnya, mengontrol diri dan tidak terbawa emosi, karena itu akan merugikan diri sendiri maupun orang lain. "
    show budayu mt_lirik mlt_standar
    bdy "Contoh lainnya, berpikir sebelum bertindak dan tidak mudah percaya."
    show budayu mt_standar mlt_standar1
    bdy "Jadi sebelum melakukan sesuatu kalian harus pikirkan dulu apakah itu merugikan orang lain atau diri sendiri?"
    bdy "Apakah itu melanggar aturan? Apakah itu bisa dipercaya atau tidak."
    
    scene kelas with fade
    show budayu with dissolve
    bdy "Kita memang tidak bisa luput dari kesalahan, tapi belajarlah dari kesalahan sebelumnya."
    show budayu mt_lirik mlt_standar1
    bdy "Jangan mengulangi kesalahan yang sama."
    show budayu mlt_standar
    "Bu Dayu melihat ke arahku dan [gta]. Sepertinya contoh itu ditargetkan pada kami berdua."
    scene kelas with fade
    "Bel istirahat kedua pun berbunyi."
    show budayu mlt_standar1 with dissolve
    bdy "Sekian dari ibu untuk jam pelajaran hari ini"
    show budayu mlt_standar
    bdy "[snt] apa kamu sudah melaporkannya ke wali kelas?"
    show santi papan at left with dissolve 
    snt "Sudah Bu, kami diizinkan pulang lebih awal."
    hide santi with dissolve
    bdy "Baiklah. Kalian dipersilakan untuk pulang."
    show budayu mt_lirik mlt_standar1
    bdy "Tapi [mnk], [gta], ingat kalau kalian akan remedial di kelas ini setelah bel pulang nanti. Jadi tetap di sekolah."
    show budayu mlt_standar
    bdy "Soal remedial ini berkaitan dengan apa yang Ibu ajarkan tadi. Jadi belajarlah secara mandiri dari buku atau sumber lain."
    show budayu mt_standar
    mnk als_sedih " Baik, Bu.."
    show gita als_bingung mt_pejam at right with dissolve
    gta "...baik, Bu.."
    hide gita 
    hide budayu
    with dissolve
    snt "{i}Asana Parama Santih{/i}"
    "Siswa-siswi" "{i}Om Santih Santih Santih Om{/i}"
    call screen amanat(1)


    call screen sesi(0)


    return