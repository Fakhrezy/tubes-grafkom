import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from math import cos, sin, pi, sqrt
import random

cloud_positions = [
    {"x": -0.5, "y": 0.8, "scale": 0.8},
    {"x": 0.0, "y": 0.9, "scale": 1.2},
    {"x": 0.7, "y": 0.7, "scale": 0.9},
    {"x": -0.8, "y": 0.6, "scale": 1.0},
    {"x": 0.4, "y": 0.5, "scale": 0.7},
    {"x": 1.1, "y": 0.5, "scale": 1.2}
]

small_star_positions = [(random.uniform(-1, 1), random.uniform(-1, 1)) for _ in range(50)]
small_star_velocities = [(random.uniform(-0.005, 0.005), random.uniform(-0.005, 0.005)) for _ in range(50)]
large_star_positions = [(random.uniform(-1, 1), random.uniform(-1, 1)) for _ in range(10)]
large_star_scale = 1.0

pocong_position = {"x": -0.3, "y": -0.4, "scale": 0.4, "angle": 0}

def draw_moon(radius=0.4):
    glColor3f(0.7, 0.7, 0.7)  # Warna abu-abu untuk bulan
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0, 0)
    for i in range(101):
        angle = 2.0 * pi * i / 100
        x = radius * cos(angle)
        y = radius * sin(angle)
        glVertex2f(x, y)
    glEnd()

def draw_mountains(scale=1.0):
    glColor3f(0.5, 0.5, 0.5)  # Warna abu-abu
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.5 * scale, -0.25 * scale)
    glVertex2f(0, 0.5 * scale)
    glVertex2f(0.5 * scale, -0.25 * scale)
    glEnd()

def draw_ground():
    glColor3f(0.0, 0.8, 0.0)  # Warna hijau untuk daratan
    glBegin(GL_QUADS)
    glVertex2f(-1, -0.5)
    glVertex2f(1, -0.5)
    glVertex2f(1, -1)
    glVertex2f(-1, -1)
    glEnd()

def draw_tree(scale=1.0):
    glColor3f(0.5, 0.35, 0.05)  # Warna coklat untuk batang pohon
    glBegin(GL_QUADS)
    glVertex2f(-0.01 * scale, -0.3 * scale)
    glVertex2f(0.01 * scale, -0.3 * scale)
    glVertex2f(0.01 * scale, 0)
    glVertex2f(-0.01 * scale, 0)
    glEnd()

    glColor3f(0.0, 0.5, 0.0)  # Warna hijau untuk daun pohon (bentuk bulat)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0, 0.1 * scale)
    for i in range(101):
        angle = 2.0 * pi * i / 100
        x = 0.1 * scale * cos(angle)
        y = 0.1 * scale * sin(angle) + 0.1 * scale
        glVertex2f(x, y)
    glEnd()
    
def draw_pocong(scale=1.0, time=0):
    global pocong_position
    angle = 10 * sin(time)  # Gunakan fungsi sinus untuk memberikan gerakan
    pocong_position["angle"] = angle

    # Gambar batang pohon berbentuk lingkaran
    glColor3f(1.0, 1.0, 1.0)  # Warna putih untuk batang pohon
    glBegin(GL_TRIANGLE_FAN)
    for i in range(101):
        angle = 2.0 * pi * i / 100
        x = 0.08 * scale * cos(angle)
        y = -0.25 * scale + 0.2 * scale * sin(angle)  # Turunkan posisi batang
        glVertex2f(x, y)
    glEnd()

    # Gambar daun pohon (bentuk bulat)
    glColor3f(1.0, 1.0, 1.0)  # Warna putih untuk daun pohon
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0, 0.03 * scale)  # Turunkan posisi daun
    for i in range(101):
        angle = 2.0 * pi * i / 100
        x = 0.1 * scale * cos(angle)
        y = 0.12 * scale * sin(angle) + 0.05 * scale  # Turunkan posisi daun
        glVertex2f(x, y)
    glEnd()
    
    # Geser ke bawah segitiga di atas daun (segitiga terbalik)
    glColor3f(1.0, 1.0, 1.0)  # Warna putih untuk segitiga
    glBegin(GL_TRIANGLES)
    glVertex2f(0, 0.1 * scale)  # Posisi puncak segitiga, geser ke bawah
    glVertex2f(-0.1 * scale, 0.30 * scale)  # Posisi titik kiri segitiga, geser ke bawah
    glVertex2f(0.1 * scale, 0.30 * scale)  # Posisi titik kanan segitiga, geser ke bawah
    glEnd()

def draw_cloud(position):
    x, y, scale = position["x"], position["y"], position["scale"]
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)
    for i in range(101):
        angle = 2.0 * pi * i / 100
        cloud_radius = 0.1 * scale
        cloud_x = x + cloud_radius * cos(angle)
        cloud_y = y + 0.05 * scale * sin(angle)
        glVertex2f(cloud_x, cloud_y)
    glEnd()

def draw_star(position, size, color):
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_POINTS)
    glVertex2f(position[0], position[1])
    glEnd()

    glColor3f(color[0], color[1], color[2])
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(position[0], position[1])
    for i in range(101):
        angle = 2.0 * pi * i / 100
        x = size * cos(angle) + position[0]
        y = size * sin(angle) + position[1]
        glVertex2f(x, y)
    glEnd()

def draw_stars(time):
    # Gambar bintang kecil
    for i in range(len(small_star_positions)):
        position = (
            small_star_positions[i][0] + small_star_velocities[i][0],
            small_star_positions[i][1] + small_star_velocities[i][1]
        )
        draw_star(position, 0.005, (1.0, 1.0, 1.0))  # Warna putih

    # Gambar bintang besar dengan animasi transformasi skala
    global large_star_scale
    large_star_scale = abs(sin(time * 0.001))  # Gunakan fungsi sinus untuk animasi
    for position in large_star_positions:
        draw_star(position, 0.02 * large_star_scale, (1.0, 1.0, 0.8))

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Gambar langit gelap
    glColor3f(0.0, 0.0, 0.1)  # Warna biru gelap
    glBegin(GL_QUADS)
    glVertex2f(-1, -1)
    glVertex2f(1, -1)
    glVertex2f(1, 1)
    glVertex2f(-1, 1)
    glEnd()

    # Gambar bintang
    draw_stars(pygame.time.get_ticks())

    # Gambar bulan dengan radius lebih kecil
    glTranslatef(0.5, 0.5, 0.0)
    draw_moon(radius=0.2)

    # Gambar gunung pertama 
    glLoadIdentity()
    glTranslatef(-0.5, -0.5, 0.0)
    draw_mountains(scale=0.75)

    # Gambar daratan
    glLoadIdentity()
    draw_ground()

    # Gambar gunung kedua 
    glLoadIdentity()
    glTranslatef(0.5, -0.5, 0.0)
    draw_mountains(scale=0.5)

    # Gambar pohon pertama 
    glLoadIdentity()
    glTranslatef(0.8, -0.5, 0.0)
    draw_tree()

    glLoadIdentity()
    glTranslatef(0.9, -0.6, 0.0)
    draw_tree(0.5)

    # Gambar pohon kedua 
    glLoadIdentity()
    glTranslatef(-0.8, -0.4, 0.0)
    draw_tree(scale=0.6)

    glLoadIdentity()
    glTranslatef(-0.7, -0.4, 0.0)
    draw_tree(scale=0.4)

    glLoadIdentity()
    glTranslatef(pocong_position["x"], pocong_position["y"], 0.0)
    draw_pocong(scale=pocong_position["scale"], time=pygame.time.get_ticks())

    # Gambar awan
    for cloud_position in cloud_positions:
        draw_cloud(cloud_position)

    # Perbarui posisi awan
    for cloud_position in cloud_positions:
        cloud_position["x"] += 0.001

    pygame.display.flip()


pygame.init()
layar = (800, 600)
pygame.display.set_mode(layar, DOUBLEBUF | OPENGL)

# Set proyeksi ortografis
glOrtho(-1, 1, -1, 1, -1, 1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    draw()
    pygame.time.wait(10)
