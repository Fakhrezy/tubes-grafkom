import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Ukuran jendela permainan
window_size = (960, 540)

# Membuat jendela permainan
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Game dengan Latar Belakang Kustom")

def load_background(background_image):
    # Memuat gambar latar belakang dan menyesuaikannya dengan ukuran jendela
    background = pygame.image.load(background_image)
    background = pygame.transform.scale(background, window_size)
    return background

def load_foreground(foreground_image):
    # Memuat gambar tambahan (foreground)
    foreground = pygame.image.load(foreground_image)
    # Sesuaikan ukuran gambar sesuai kebutuhan
    foreground = pygame.transform.scale(foreground, (70, 70))  # Ganti dengan ukuran yang sesuai
    return foreground

def load_pocong(pocong_image):
    # Memuat gambar tambahan (foreground)
    pocong = pygame.image.load(pocong_image)
    # Sesuaikan ukuran gambar sesuai kebutuhan
    pocong = pygame.transform.scale(pocong, (150, 150))  # Ganti dengan ukuran yang sesuai
    return pocong

def load_pocong_rf(pocong_image):
    pocong = pygame.image.load(pocong_image)
    pocong = pygame.transform.scale(pocong, (150, 150))
    
    # Merefleksikan gambar pocong terhadap sumbu y
    pocong = pygame.transform.flip(pocong, True, False)
    
    return pocong


def load_jurig(jurig_image):
    # Memuat gambar tambahan (foreground)
    jurig = pygame.image.load(jurig_image)
    # Sesuaikan ukuran gambar sesuai kebutuhan
    jurig = pygame.transform.scale(jurig, (100, 100))  # Ganti dengan ukuran yang sesuai
    return jurig

def load_bulan(bulan_image):
    # Memuat gambar tambahan (foreground)
    bulan = pygame.image.load(bulan_image)
    # Sesuaikan ukuran gambar sesuai kebutuhan
    bulan = pygame.transform.scale(bulan, (200, 200))  # Ganti dengan ukuran yang sesuai
    return bulan

def game_loop():
    clock = pygame.time.Clock()

    # Mengganti nama file gambar sesuai dengan yang Anda miliki
    background_image = "background.png"
    foreground_image = "star.png"
    pocong_image = "pocong.png"# Ganti dengan nama file gambar Anda
    jurig_image = "jurig.png"
    bulan_image = "bulan.png"

    background = load_background(background_image)
    foreground = load_foreground(foreground_image)
    pocong = load_pocong(pocong_image)
    pocong_rf = load_pocong_rf(pocong_image)
    jurig = load_jurig(jurig_image)
    bulan = load_bulan(bulan_image)
    
    angle = 0
    scaling_direction = 1
    jurig_x = 0
    jurig_speed = 2  # Kecepatan translasi jurig
    jurig_reset_pos = window_size[0] + 50  # Posisi reset jurig_x setelah melewati batas
    
    pocong_x = 200  # Posisi horizontal baru
    pocong_y = 200  # Posisi vertikal baru
    pocong_speed = 5  # Kecepatan translasi pocong
    jumping_up = True  # Status loncatan pocong

    # Daftar bintang dengan koordinat dan skala
    stars = [
        {"x": 600, "y": 50, "scale": 1.0},
        {"x": 500, "y": 200, "scale": 0.8},
        {"x": 350, "y": 40, "scale": 1.2}
    ]



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Menampilkan latar belakang pada jendela
        screen.blit(background, (0, 0))

        # Menampilkan gambar tambahan (foreground) di depan latar belakang
        # screen.blit(foreground, (600, 50))  # Ganti dengan posisi yang sesuai
        # screen.blit(foreground, (500, 200))
        # screen.blit(foreground, (350, 40))
        
        # Animasi TRANSLASI ke atas dan ke bawah untuk pocong dan bayangannya
        screen.blit(pocong, (pocong_x, pocong_y))

        # Memastikan pocong tetap berada di dalam jendela
        if jumping_up:
            pocong_y -= pocong_speed
            if pocong_y <= 200:  # Posisi puncak loncatan
                jumping_up = False
        else:
            pocong_y += pocong_speed
            if pocong_y >= 300:  # Posisi bawah loncatan
                jumping_up = True
        
        screen.blit(pocong, (500, 270))
        screen.blit(pocong_rf, (700, 270))
        # screen.blit(jurig, (600, 300))
        # screen.blit(bulan, (750, 40))
        
        # Animasi translasi ke kanan untuk jurig
        screen.blit(jurig, (jurig_x, 300))
        jurig_x += jurig_speed  # Ubah sesuai kecepatan translasi yang diinginkan

        # Jika jurig melewati batas, reset posisinya
        if jurig_x > jurig_reset_pos:
            jurig_x = -jurig.get_width()


        # Tambahan elemen permainan atau logika permainan dapat ditambahkan di sini
        
        rotated_bulan = pygame.transform.rotate(bulan, angle)
        bulan_rect = rotated_bulan.get_rect(center=(800, 70))
        screen.blit(rotated_bulan, bulan_rect.topleft)
        
        # Animasi skala bintang
        for star in stars:
            scaled_foreground = pygame.transform.scale(foreground, (int(70 * star["scale"]), int(70 * star["scale"])))
            foreground_rect = scaled_foreground.get_rect(center=(star["x"], star["y"]))
            screen.blit(scaled_foreground, foreground_rect.topleft)

            star["scale"] += 0.01 * scaling_direction
            if star["scale"] >= 2.0 or star["scale"] <= 0.5:
                scaling_direction *= -1
                
        # Animasi rotasi bulan
        angle += 1  # Ubah sesuai kecepatan rotasi yang diinginkan
        
        


        # Update layar
        pygame.display.flip()

        # Menetapkan batas FPS
        clock.tick(30)

if __name__ == "__main__":
    game_loop()
