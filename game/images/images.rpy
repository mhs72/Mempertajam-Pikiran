# Background
image sekolah = "bg/skl.jpeg"
image kelas = "bg/kls.jpeg"
image kantin = "bg/ktn.jpeg"
image perpus = "bg/pps.jpeg"

# CG
image cg1 = "cg/cg_1.png"
image cg1a = "cg/cg_1a.png"
image cg1b = "cg/cg_1b.png"

# Character
define mnk = Character ("Manik", image = "manik", color = "#0e573d")
define gta = Character ("Gita", image = "gita", color = "#734a79")
define bdy = Character ("Bu Dayu", image = "budayu", color = "#364f79")
define snt = Character ("Santi", image = "santi", color = "#e16c8e")
define glg = Character ("Gilang", image = "gilang", color = "#993434")
define swa1 = Character ("Siswa 1", image = "swa1")
define swa2 = Character ("Siswa 2", image = "swa2")
define swi1 = Character ("Siswi 1", image = "swi1")
define swi2 = Character ("Siswi 2", image = "swi2")

transform sprite_default:
    zoom 0.8

# Popup
image pop1 = "pop/pop1.png"
image pop2 = "pop/pop2.png"
image pop2a = "pop/pop2a.png"
image pop2b = "pop/pop2b.png"
image pop2c = "pop/pop2c.png"
image pop2d = "pop/pop2d.png"

image pop3_bg = "pop/pop3_bg.jpg"
image pop3_ppn = "pop/pop3_ppn.png"
image pop3a = "pop/pop3a.png"
image pop3b = "pop/pop3b.png"
image pop3c = "pop/pop3c.png"
image pop3d = "pop/pop3d.png"
image pop3e = "pop/pop3e.png"
image pop3f = "pop/pop3f.png"
image pop3g = "pop/pop3g.png"
image pop3h = "pop/pop3h.png"

image pop4_bg = "pop/pop4_bg.jpg"
image pop4_bku = "pop/pop4_bku.png"
image pop4a = "pop/pop4a.png"
image pop4b = "pop/pop4b.png"
image pop4c = "pop/pop4c.png"
image pop4d = "pop/pop4d.png"
image pop4e = "pop/pop4e.png"
image pop4f = "pop/pop4f.png"
image pop4g = "pop/pop4g.png"
image pop4h = "pop/pop4h.png"
image pop4i = "pop/pop4i.png"
image pop4j = "pop/pop4j.png"
image pop4k = "pop/pop4k.png"
image pop4l = "pop/pop4l.png"
image pop4m = "pop/pop4m.png"
image pop4n = "pop/pop4n.png"

image pop5 = "pop/pop5.png"
image pop5a = "pop/pop5a.png"
image pop6 = "pop/pop6.png"
image pop6a = "pop/pop6a.png"
image pop7 = "pop/pop7.png"
image pop7a = "pop/pop7a.png"

image pop8 = "pop/pop8.png"
image pop8a = "pop/pop8a.png"
image pop8bad = "pop/pop8bad.png"
image pop8god = "pop/pop8god.png"
image pop8nor = "pop/pop8nor.png"

#Amanat
define bg_putih = Solid("#ffffff")
image amnt_bingkai = "amnt/amnt_bg1.png"
image amnt_kirib = "amnt/amnt_dekor1.png"
image amnt_kanana = "amnt/amnt_dekor2.png"

image amnt1_mnk = "amnt/amnt_1b.PNG"
image amnt1_bdy = "amnt/amnt_1a.PNG"
image amnt2 = "amnt/amnt_2.PNG"
image amnt3 = "amnt/amnt_3d.PNG"
image amnt3_gta = "amnt/amnt_3b.PNG"
image amnt3_snt = "amnt/amnt_3a.PNG"
image amnt3_mnk = "amnt/amnt_3c.PNG"
image amnt4_a = "amnt/amnt_4a.PNG"
image amnt4_b = "amnt/amnt_4b.PNG"
image amnt5_gta = "amnt/amnt_5a.PNG"
image amnt5_snt = "amnt/amnt_5b.PNG"
image amnt5_glg = "amnt/amnt_5d.PNG"
image amnt5_mnk = "amnt/amnt_5c.PNG"
image amnt6 = "amnt/amnt_6.PNG"

#Style tulisan amanat
style amanat:
    size 45
    font "gui/font/LTSoul-Bold.otf"
    xalign 0.5
    text_align 0.5
    xmaximum 900

#Fungsi amanat
screen amanat(amanat):
    add bg_putih:
        at transform:
            alpha 0.0
            linear 0.5 alpha 1.0

    add "amnt_bingkai":
        at transform:
            anchor (0.5, 0.5)   # titik acuan di tengah objek
            xalign 0.5
            yalign 0.5
            zoom 0.0
            easein 0.5 zoom 1.0 

    add "amnt_kirib":
        at transform:
            xoffset -200
            yoffset 200
            easein 0.7 xoffset 0.0 yoffset 0.0

    add "amnt_kanana":
        at transform:
            xoffset 200
            yoffset -200
            easein 0.7 xoffset 0.0 yoffset 0.0
            
    if amanat == 1:  
        add "pop3_ppn":
            at transform:
                alpha 0.0
                xpos -150
                ypos 50
                pause 0.5
                yoffset -200
                easein 1.0 yoffset 0.0 alpha 1.0
        add "amnt1_bdy":
            at transform:
                xpos -500
                pause 0.5
                easein 1.0 xpos 0
        add "amnt1_mnk":
            at transform:
                xpos 500
                pause 0.5
                easein 1.0 xpos 0
        text "Belajar dari kesalahan adalah bagian dari proses mempertajam pikiran untuk mengambil keputusan yang lebih tepat ke depannya.":
            style "amanat" 
            at transform:
                xoffset -10
                alpha 0.0
                pause 1.0
                yoffset 350
                easein 1.0 yoffset 300 alpha 1.0

    elif amanat == 2:
        add "amnt2":
            at transform:
                alpha 0.0
                pause 0.5
                yoffset 200
                easein 1.0 yoffset 0.0 alpha 1.0
        text "Kontrol diri membantu kita menghindari masalah yang tidak perlu dan menjaga hubungan baik dengan orang lain.":
            style "amanat"
            at transform:
                alpha 0.0
                pause 0.5
                yoffset -100
                easein 1.0 yoffset 200 alpha 1.0

    elif amanat == 3:
        add "amnt3":
            at transform:
                alpha 0.0
                pause 0.5
                yoffset 200
                easein 0.7 yoffset 0.0 alpha 1.0    
        add "amnt3_mnk":
            at transform:
                alpha 0.0
                pause 0.6
                yoffset -100
                easein 1.0 yoffset 0.0 alpha 1.0
        add "amnt3_gta":
            at transform:
                alpha 0.0
                pause 0.6
                xoffset -100
                easein 1.0 xoffset 0.0 alpha 1.0
        add "amnt3_snt":
            at transform:
                alpha 0.0
                pause 0.6
                xoffset 100
                easein 1.0 xoffset 0.0 alpha 1.0
        text "Tidak semua informasi itu benar, penting untuk mencari tahu sebelum mempercayainya.":
            style "amanat"
            at transform:
                yoffset 350
                alpha 0.0
                pause 1.0
                easein 1.0 alpha 1.0

    elif amanat == 4:
        add "amnt4_a":
            at transform:
                alpha 0.0
                pause 0.7
                xoffset 200
                easein 1.0 xoffset 0.0 alpha 1.0
        add "amnt4_b":
            at transform:
                alpha 0.0
                pause 0.5
                xoffset -400
                easeout 0.5 xoffset 0.0 alpha 1.0
        text "Berpikir sebelum bertindak membantu kita menghindari risiko yang tidak perlu.":
            style "amanat"
            at transform:
                alpha 0.0
                yoffset 280
                pause 1.0
                xoffset -100
                easein 1.0 xoffset 0.0 alpha 1.0
    
    elif amanat == 5:
        add "amnt5_gta":
            at transform:
                alpha 0.0
                pause 0.5
                yoffset 50
                easein 1.0 yoffset 0.0 alpha 0.75
        add "amnt5_snt":
            at transform:
                alpha 0.0
                pause 0.5
                xoffset 100
                easein 1.0 xoffset 0.0 alpha 1.0
        add "amnt5_glg":
            at transform:
                alpha 0.0
                pause 0.5
                xoffset -100
                easein 1.0 xoffset 0.0 alpha 1.0
        add "amnt5_mnk":
            at transform:
                alpha 0.0
                pause 0.5
                yoffset -100
                easein 1.0 yoffset 0.0 alpha 1.0
        text "Belajar secara konsisten membuat pikiran semakin tajam dan siap menghadapi berbagai persoalan.":
            style "amanat"
            at transform:
                alpha 0.0   
                pause 0.5
                yoffset 280
                easein 1.0 yoffset 200 alpha 1.0

    elif amanat == 6:
        add "amnt6":
            at transform:
                alpha 0.0
                pause 0.5
                yoffset 100
                easein 1.0 yoffset 0.0 alpha 1.0
        text "Tumpek Landep bukan hanya seremonial semata tapi mengingatkan kita untuk mempertajam pikiran.\n\n Cerdaslah dalam bersikap!":
            style "amanat"
            at transform:
                alpha 0.0   
                pause 0.5
                yoffset 280
                easein 1.0 yoffset 150 alpha 1.0
    
    #bisa klik dimanapun untuk next
    button: 
        action Return()
        xysize (config.screen_width, config.screen_height) #ukuran area yang bisa diklik
        background None
    


#Tambahkan efek next kelap-kelip

## Side Manik
layeredimage side manik:
    always:
        "chr/mnk/mnk_bdn.png"

    group alis:
        attribute als_standar:
            "chr/mnk/als_standar.png" default
        attribute als_bingung:
            "chr/mnk/als_bing.png"
        attribute als_atas:
            "chr/mnk/als_ats.png"
        attribute als_marah:
            "chr/mnk/als_mrh.png"
        attribute als_sedih:
            "chr/mnk/als_sdh.png"
    group mata:
        attribute mt_standar:
            "chr/mnk/mt_standar.png" default
        attribute mt_pejam:
            "chr/mnk/mt_pjm.png"
        attribute mt_sipit:
            "chr/mnk/mt_spt.png"
        attribute mt_kaget:
            "chr/mnk/mt_kgt.png"
        attribute mt_lirik:
            "chr/mnk/mt_lrk.png"
        attribute mt_mikir:
            "chr/mnk/mt_mkr.png"
        attribute mt_bete:
            "chr/mnk/mt_bt.png"
        attribute mt_cemas:
            "chr/mnk/mt_cms.png"
    group mulut:
        attribute mlt_standar:
            "chr/mnk/mlt_standar.png" default
        attribute mlt_standar1:
            "chr/mnk/mlt_standar1.png"
        attribute mlt_senyum:
            "chr/mnk/mlt_sym.png"
        attribute mlt_senyum1:
            "chr/mnk/mlt_sym1.png"
        attribute mlt_teriak:
            "chr/mnk/mlt_trk.png"
        attribute mlt_tawa:
            "chr/mnk/mlt_tw.png"
        attribute mlt_marah:
            "chr/mnk/mlt_mrh.png"
    group efek:
        attribute efk_kesal:
            "chr/mnk/efk_x.png"
        attribute efk_fyuh:
            "chr/mnk/efk_f.png"
        attribute efk_keringat:
            "chr/mnk/efk_k.png"
        attribute efk_cemas:
            "chr/mnk/efk_cms.png"
        attribute efk_merona:
            "chr/mnk/efk_rona.png"
        attribute efk_kaget:
            "chr/mnk/efk_kgt.png"

transform side_small:
    zoom 0.75
    xpos -10
    yalign 1.0

transform side_small_mobile:
    zoom 0.7
    xpos -50
    yalign 1.0
    
## Gita
layeredimage gita:
    at sprite_default
    always:
        "chr/gta/gta_bdn.png"

    group alis:
        attribute als_standar:
            "chr/gta/als_standar.png" default
        attribute als_bingung:
            "chr/gta/als_bing.png"
        attribute als_sedih:
            "chr/gta/als_sdh.png"
        attribute als_marah:
            "chr/gta/als_mrh.png"
    group mata:
        attribute mt_standar:
            "chr/gta/mt_standar.png" default
        attribute mt_kaget:
            "chr/gta/mt_kgt.png"
        attribute mt_lirik:
            "chr/gta/mt_lrk.png"
        attribute mt_mikir:
            "chr/gta/mt_mkr.png"
        attribute mt_pejam:
            "chr/gta/mt_pjm.png"
        attribute mt_marah:
            "chr/gta/mt_mrh.png"
        attribute mt_sipit:
            "chr/gta/mt_spt.png"
    group mulut:
        attribute mlt_standar:
            "chr/gta/mlt_standar.png" default
        attribute mlt_standar1:
            "chr/gta/mlt_standar1.png"
        attribute mlt_senyum:
            "chr/gta/mlt_sym.png"
        attribute mlt_senyum1:
            "chr/gta/mlt_sym1.png"
        attribute mlt_teriak:
            "chr/gta/mlt_trk.png"
        attribute mlt_tawa:
            "chr/gta/mlt_tw.png"
    group efek:
        attribute efk_x:
            "chr/gta/efk_x.png"
        attribute efk_keringat:
            "chr/gta/efk_k.png"
        attribute efk_kaget:
            "chr/gta/efk_kgt.png"
        attribute efk_merona:
            "chr/gta/efk_rona.png"

## Bu Dayu
layeredimage budayu:
    at sprite_default
    always:
        "chr/bdy/bdy_bdn.png"

    group alis:
        attribute als_standar:
            "chr/bdy/als_standar.png" default
        attribute als_bingung:
            "chr/bdy/als_bing.png"
        attribute als_marah:
            "chr/bdy/als_mrh.png"
    group mata:
        attribute mt_standar:
            "chr/bdy/mt_standar.png" default
        attribute mt_lirik:
            "chr/bdy/mt_lrk.png"
        attribute mt_pejam:
            "chr/bdy/mt_pjm.png"
    group mulut:
        attribute mlt_standar:
            "chr/bdy/mlt_standar.png" default
        attribute mlt_standar1:
            "chr/bdy/mlt_standar1.png"
        attribute mlt_senyum:
            "chr/bdy/mlt_sym.png"
        attribute mlt_senyum1:
            "chr/bdy/mlt_sym1.png"
        attribute mlt_teriak:
            "chr/bdy/mlt_trk.png"
    group efek:
        attribute efk_x:
            "chr/bdy/efk_x.png"

## Santi
layeredimage santi:
    at sprite_default
    always:
        "chr/snt/snt_bdn.png"

    group alis:
        attribute als_standar:
            "chr/snt/als_standar.png" default
        attribute als_bingung:
            "chr/snt/als_bing.png"
        attribute als_sedih:
            "chr/snt/als_sdh.png"
        attribute als_marah:
            "chr/snt/als_mrh.png"
    group mata:
        attribute mt_standar:
            "chr/snt/mt_standar.png" default
        attribute mt_kaget:
            "chr/snt/mt_kgt.png"
        attribute mt_lirik:
            "chr/snt/mt_lrk.png"
        attribute mt_mikir:
            "chr/snt/mt_mkr.png"
        attribute mt_pejam:
            "chr/snt/mt_pjm.png"
        attribute mt_sipit:
            "chr/snt/mt_spt.png"
    group mulut:
        attribute mlt_standar:
            "chr/snt/mlt_standar.png" default
        attribute mlt_standar1:
            "chr/snt/mlt_standar1.png"
        attribute mlt_senyum:
            "chr/snt/mlt_sym.png"
        attribute mlt_senyum1:
            "chr/snt/mlt_sym1.png"
        attribute mlt_tawa:
            "chr/snt/mlt_tw.png"
    group efek:
        attribute efk_x:
            "chr/snt/efk_x.png"
        attribute efk_keringat:
            "chr/snt/efk_k.png"
        attribute efk_fyuh:
            "chr/snt/efk_f.png"
    group aksesoris:
        attribute papan:
            "chr/snt/efk_ppn.png"

## Gilang
layeredimage gilang:
    at sprite_default
    always:
        "chr/glg/glg_bdn.png"

    group alis:
        attribute als_standar:
            "chr/glg/als_standar.png" default
        attribute als_bingung:
            "chr/glg/als_bing.png"
        attribute als_sedih:
            "chr/glg/als_sdh.png"
        attribute als_marah:
            "chr/glg/als_mrh.png"
    group mata:
        attribute mt_standar:
            "chr/glg/mt_standar.png" default
        attribute mt_kaget:
            "chr/glg/mt_kgt.png"
        attribute mt_lirik:
            "chr/glg/mt_lrk.png"
        attribute mt_mikir:
            "chr/glg/mt_mkr.png"
        attribute mt_pejam:
            "chr/glg/mt_pjm.png"
        attribute mt_marah:
            "chr/glg/mt_mrh.png"
        attribute mt_sipit:
            "chr/glg/mt_spt.png"
    group mulut:
        attribute mlt_standar:
            "chr/glg/mlt_standar.png" default
        attribute mlt_standar1:
            "chr/glg/mlt_standar1_2.png"
        attribute mlt_senyum:
            "chr/glg/mlt_sym.png"
        attribute mlt_senyum1:
            "chr/glg/mlt_sym1.png"
        attribute mlt_teriak:
            "chr/glg/mlt_trk.png"
        attribute mlt_tawa:
            "chr/glg/mlt_tw.png"
    group efek:
        attribute efk_x:
            "chr/glg/efk_x.png"
        attribute efk_marah:
            "chr/glg/efk_x2.png"
        attribute efk_keringat:
            "chr/glg/efk_k.png"
        attribute efk_kaget:
            "chr/glg/efk_kgt.png"
        attribute efk_merona:
            "chr/glg/efk_rona.png"

## Npc
image swa1:
    "chr/npc/npc_1.png" 
    zoom 0.8
image swa2:
    "chr/npc/npc_2.png" 
    zoom 0.8
image swi1:
    "chr/npc/npc_3.png" 
    zoom 0.8
image swi2:
    "chr/npc/npc_4.png" 
    zoom 0.8