import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Ukuran jendela permainan
window_size = (960, 540)

# Membuat jendela permainan
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Tempat Pemakaman Umum (dengan transformasi)")

def load_background(background_image):
    # Memuat gambar latar belakang dan menyesuaikannya dengan ukuran jendela
    background = pygame.image.load(background_image)
    background = pygame.transform.scale(background, window_size)
    return background

def load_bintang(bintang_image):
    # Memuat gambar tambahan (bintang)
    bintang = pygame.image.load(bintang_image)
    # Sesuaikan ukuran gambar sesuai kebutuhan
    bintang = pygame.transform.scale(bintang, (50, 50))  # Ganti ukuran 
    return bintang

def load_pocong(pocong_image):
    # Memuat gambar tambahan (pocong)
    pocong = pygame.image.load(pocong_image)
    pocong = pygame.transform.scale(pocong, (150, 150))  # Ganti ukuran 
    return pocong

def load_pocong_rf(pocong_image):
    pocong = pygame.image.load(pocong_image)
    pocong = pygame.transform.scale(pocong, (150, 150))
    # REFLEKSI SUMBU X
    pocong = pygame.transform.flip(pocong, True, False)
    return pocong


def load_jurig(jurig_image):
    # Memuat gambar tambahan (bintang)
    jurig = pygame.image.load(jurig_image)
    jurig = pygame.transform.scale(jurig, (100, 100))  # Ganti dengan ukuran yang sesuai
    return jurig

def load_bulan(bulan_image):
    # Memuat gambar tambahan (bintang)
    bulan = pygame.image.load(bulan_image)
    bulan = pygame.transform.scale(bulan, (200, 200))  # Ganti dengan ukuran yang sesuai
    return bulan

def game_loop():
    clock = pygame.time.Clock()

    # File Gambar
    background_image = "background.png"
    bintang_image = "star.png"
    pocong_image = "pocong.png"
    jurig_image = "jurig.png"
    bulan_image = "bulan.png"

    background = load_background(background_image)
    bintang = load_bintang(bintang_image)
    pocong = load_pocong(pocong_image)
    pocong_rf = load_pocong_rf(pocong_image)
    jurig = load_jurig(jurig_image)
    bulan = load_bulan(bulan_image)
    
    # BINTANG
    angle = 0
    scaling_direction = 2 # kecepatan skala bintang
    
    # JURIG
    jurig_x = 0
    jurig_reset_pos = window_size[0] + 50  # Posisi reset jurig_x setelah melewati batas
    # JURIG GERAK
    jurig_speed = 3  # Kecepatan 0 untuk berhenti
    
    # POCONG
    pocong_x = 200  
    pocong_y = 200  
    pocong_speed = 5  # Kecepatan translasi pocong
    jumping_up = True  # Status loncatan pocong

    # Daftar bintang dengan koordinat dan skala
    stars = [
        {"x": 600, "y": 50, "scale": 0.5},
        {"x": 450, "y": 130, "scale": 0.5},
        {"x": 350, "y": 40, "scale": 0.5}
    ]
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Menampilkan latar belakang pada jendela
        screen.blit(background, (0, 0))
        
        
        
        

        
        # TRANSLASI POCONG ke atas dan ke bawah LONCAT
        screen.blit(pocong, (pocong_x, pocong_y))
        if jumping_up:
            pocong_y -= pocong_speed
            if pocong_y <= 200:  # Posisi puncak loncatan
                jumping_up = False
        else:
            pocong_y += pocong_speed
            if pocong_y >= 300:  # Posisi bawah loncatan
                jumping_up = True
        
        
        # REFLEKSI POCONG
        screen.blit(pocong, (500, 270))
        # Yang di REFLEKSI
        screen.blit(pocong_rf, (700, 270))
        
        
        # TRANSLASI JURIG ke kanan 
        screen.blit(jurig, (jurig_x, 400))
        jurig_x += jurig_speed  # Ubah sesuai kecepatan translasi yang diinginkan
        # Jika jurig melewati batas, reset posisinya
        if jurig_x > jurig_reset_pos:
            jurig_x = -jurig.get_width()


        # ROTASI BULAN
        rotated_bulan = pygame.transform.rotate(bulan, angle)
        bulan_rect = rotated_bulan.get_rect(center=(800, 70))
        screen.blit(rotated_bulan, bulan_rect.topleft)
        # BERHENTI ROTASI ISIKAN 0
        angle += 1  # Ubah sesuai kecepatan rotasi yang diinginkan
        
        # SKALA BINTANG
        for star in stars:
            scaled_bintang = pygame.transform.scale(bintang, (int(40 * star["scale"]), int(40 * star["scale"])))
            bintang_rect = scaled_bintang.get_rect(center=(star["x"], star["y"]))
            screen.blit(scaled_bintang, bintang_rect.topleft)
            star["scale"] += 0.01 * scaling_direction
            if star["scale"] >= 2.0 or star["scale"] <= 0.5: # menentukan ukuran skala maks dan min
                scaling_direction *= -1
        
        
        
        


        # Update layar
        pygame.display.flip()

        # Menetapkan batas FPS
        clock.tick(30)

if __name__ == "__main__":
    game_loop()
