import pygame
import math

pygame.init()

# Ustawienie szerokości okna
ekran_wiel = (600, 600)
ekran = pygame.display.set_mode(ekran_wiel)

# Środek okna
sr_x, sr_y = ekran_wiel[0] // 2, ekran_wiel[1] // 2

# Kolory
tlo = (255, 255, 0)  # Żółte tło
border_color = (0, 0, 0)  # Kolor obramówki
center_color = (0, 0, 255)  # Kolor środka sześciokąta
number_color = (255, 255, 255)  # Biały kolor liczby
number_border_color = (0, 0, 0)  # Kolor obramówki liczby

# Promień sześciokąta
promien = 150

# Inicjalizacja wzoru
reference_vertices = [(sr_x + int(promien * math.cos(2 * math.pi * i / 6)),
                       sr_y + int(promien * math.sin(2 * math.pi * i / 6)))
                      for i in range(6)]


vertices = reference_vertices.copy() # Kopia wzoru, na której będą dokonywane przekształcenia

button_number = None   # Sprawdzamy, który klawisz został naciśnięty aby wyświetlić przekształcenie
running = True         # Sprawdamy czy program działa
wyswietl_szesc = True  # Sprawdzamy czy kształt ma być wyświetlany

# Czcionka naszej liczby
font = pygame.font.Font(None, 36)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                vertices = reference_vertices.copy()
                wyswietl_szesc = True
                button_number = 1
            elif event.key == pygame.K_2:
                vertices = [(2 * x - sr_x, 2 * y - sr_y) for x, y in reference_vertices]
                angle = math.radians(45)
                vertices = [(int((x - sr_x) * math.cos(angle) - (y - sr_y) * math.sin(angle) + sr_x),
                             int((x - sr_x) * math.sin(angle) + (y - sr_y) * math.cos(angle) + sr_y))
                            for x, y in vertices]
                wyswietl_szesc = True
                button_number = 2
            elif event.key == pygame.K_3:
                vertices = [(x, 2 * sr_y - y) for x, y in reference_vertices]
                vertices = [(x, int(2 * (y - sr_y) + sr_y)) for x, y in vertices]
                wyswietl_szesc = True
                button_number = 3
            elif event.key == pygame.K_4:
                shear_factor = 0.4
                vertices = [(x + shear_factor * y, y) for x, y in reference_vertices]

                min_x = min(vertices, key=lambda point: point[0])[0]
                max_x = max(vertices, key=lambda point: point[0])[0]
                shift_x = (min_x + max_x) / 2 - sr_x
                vertices = [(x - shift_x, y) for x, y in vertices]

                wyswietl_szesc = True
                button_number = 4
            elif event.key == pygame.K_5:
                scale_factor_x = 2
                scale_factor_y = 1
                translation_y = -158

                vertices = [(scale_factor_x * x, scale_factor_y * y) for x, y in reference_vertices]

                vertices = [(x, y + translation_y) for x, y in vertices]

                min_x = min(vertices, key=lambda point: point[0])[0]
                max_x = max(vertices, key=lambda point: point[0])[0]
                shift_x = (min_x + max_x) / 2 - sr_x
                vertices = [(x - shift_x, y) for x, y in vertices]

                wyswietl_szesc = True
                button_number = 5
            elif event.key == pygame.K_6:
                shear_factor_y = -0.4
                angle_rotation = 0

                vertices = [(x, x * shear_factor_y + y) for x, y in reference_vertices]

                angle_rad = math.radians(angle_rotation)
                vertices = [
                    (int((x - sr_x) * math.cos(angle_rad) - (y - sr_y) * math.sin(angle_rad) + sr_x),
                     int((x - sr_x) * math.sin(angle_rad) + (y - sr_y) * math.cos(angle_rad) + sr_y))
                    for x, y in vertices]

                min_y = min(vertices, key=lambda point: point[1])[1]
                max_y = max(vertices, key=lambda point: point[1])[1]
                shift_y = (min_y + max_y) / 2 - sr_y
                vertices = [(x, y - shift_y) for x, y in vertices]

                wyswietl_szesc = True
                button_number = 6
            elif event.key == pygame.K_7:
                vertices = [(x, 2 * sr_y - y) for x, y in reference_vertices]
                vertices = [(x, int(2 * (y - sr_y) + sr_y)) for x, y in vertices]
                wyswietl_szesc = True
                button_number = 7

    # Wypełnienie tła
    ekran.fill(tlo)

    # Rysowanie sześciokąta jeśli zmienna wyswietl_szesc jest True
    if wyswietl_szesc:
        pygame.draw.polygon(ekran, center_color, vertices, 0)  # Wypełnienie środka szescianu
        pygame.draw.polygon(ekran, border_color, vertices, 2)  # Rysowanie obramówki szescianu

        # Rysowanie numeru przycisku w lewym górnym rogu
        if button_number is not None:
            number_text = font.render(str(button_number), True, number_color)
            number_rect = number_text.get_rect()
            number_rect.topleft = (10, 10)
            pygame.draw.rect(ekran, number_border_color, number_rect)
            ekran.blit(number_text, number_rect.topleft)

    # Aktualizacja ekranu
    pygame.display.flip()

# Zakończenie działania pygame
pygame.quit()