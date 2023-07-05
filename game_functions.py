"""A collection of functions used by the game."""
import sys
import pygame

from time import sleep
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, settings, screen, stats, audio, sb, ship,
                         aliens, bullets, alien_bullets):
    """Responds to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    # Removed the ability to go up and down.
    # if event.key == pygame.K_UP:
    #     ship.moving_up = True
    # elif event.key == pygame.K_DOWN:
    #     ship.moving_down = True

    if event.key == pygame.K_SPACE:
        if stats.game_active:
            fire_bullet(settings, screen, ship, bullets)
        else:
            # Starts the game if not active
            start_game(settings, screen, stats, audio, sb, ship, aliens,
                       bullets, alien_bullets)
    
    # Exits the game if 'q' is pressed.
    if event.key == pygame.K_q:
        exit_game(settings, stats)


def check_keyup_events(event, ship):
    """Responds to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False   
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(settings, screen, stats, audio, sb, play_button, ship, aliens,
                 bullets, alien_bullets):
    """Responds to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game(settings, stats)

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, stats, audio, sb,
                                 ship, aliens, bullets, alien_bullets)
        
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(settings, screen, stats, audio, sb, play_button,
                              ship, aliens, bullets, alien_bullets, mouse_x,
                              mouse_y)


def check_play_button(settings, screen, stats, audio, sb, play_button, ship,
                      aliens, bullets, alien_bullets, mouse_x, mouse_y):
    """Starts a new game whem the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked:
        start_game(settings, screen, stats, audio, sb, ship, aliens, bullets, 
                   alien_bullets)

def start_game(settings, screen, stats, audio, sb, ship, aliens, bullets,
               alien_bullets):
    """Starts a new game, if the game is not currently active."""
    if not stats.game_active:
        # Empties the list of aliens and bullets.
        aliens.empty()
        bullets.empty()
        alien_bullets.empty()

        # Resets the game settings.
        settings.initialise_dynamic_settings()

        # Hides the mouse cursor.
        pygame.mouse.set_visible(False)

        # Resets game statistics.
        stats.reset_stats()
        stats.game_active = True

        # Resets the scoreboard images.
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # Creates a new fleet and centers the ship.
        create_fleet(settings, screen, audio, ship, aliens)
        ship.center_ship()


def update_screen(settings, screen, stats, sb, ship, bullets, aliens,
                  play_button, alien_bullets):
    """Updates images on the screen and flips to the new screen."""
    # Redraws the background.
    screen.blit(settings.bg_image, screen.get_rect())

    # Redraws all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    for alien_bullet in alien_bullets.sprites():
        alien_bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # Draws the score information.
    sb.show_score()

    # Draws the play button if the game is inactive.
    if not stats.game_active:
        play_button.draw_button()

    # Makes the most recently drawn screen visible.
    pygame.display.flip()

    # Keeps the game running at 120 fps.
    settings.clock.tick(120)
    

def fire_bullet(settings, screen, ship, bullets):
    """Fire a bullet if the limit is not yet reached."""
    # Creates a new bullet and adds it to the bullets group.
    if len(bullets) < settings.bullets_allowed:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)      
        ship.cannon_sound()

def update_bullets(settings, screen, stats, audio, sb, ship, aliens, bullets,
                   alien_bullets):
    """Updates position of bullets and gets rid of old bullets."""
    # Updates bullet position.
    bullets.update()
    alien_bullets.update()

    # Gets rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    for alien_bullet in alien_bullets.copy():
        if alien_bullet.rect.top >= screen.get_height():
            alien_bullets.remove(alien_bullet)
    
    check_bullet_alien_collisions(settings, screen, stats, audio, sb, ship, 
                                  aliens, bullets, alien_bullets)
    check_bullet_ship_collisions(settings, screen, stats, audio, sb, ship, 
                                 aliens, bullets, alien_bullets)


def check_bullet_ship_collisions(settings, screen, stats, audio, sb, ship,
                                 aliens, bullets, alien_bullets):
    """Responds to alien_bullet-ship collision"""
    if pygame.sprite.spritecollideany(ship, alien_bullets):
        ship_hit(settings, screen, stats, audio, sb, ship, aliens, bullets,
                 alien_bullets)


def check_bullet_alien_collisions(settings, screen, stats, audio, sb, ship,
                                  aliens, bullets, alien_bullets):
    """Responds to bullet-alien collision"""
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            for alien in aliens:
                alien.explode()
            stats.score += settings.alien_points * len(aliens)
            sb.prep_score()

    if len(aliens) == 0:
        start_new_level(settings, stats, screen, audio, sb, ship, aliens,
                        bullets, alien_bullets)


def start_new_level(settings, stats, screen, audio, sb, ship, aliens,
                    bullets, alien_bullets):
    """Starts a new level if the whole fleet is destroyed."""
    bullets.empty()
    alien_bullets.empty()
    settings.increase_speed()

    # Increases level.
    stats.level += 1
    sb.prep_level()

    create_fleet(settings, screen, audio, ship, aliens)
    sleep(0.3)



def get_number_aliens_x(settings, alien_width) -> int:
    """Determine the number of aliens that fit in a row."""   
    available_space_x = settings.screen_width - 3 * alien_width
    number_aliens_x  = int(available_space_x / (2 * alien_width))         
    return number_aliens_x


def get_number_rows(settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (settings.screen_height - 
                         (5 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(settings, screen, audio, aliens, alien_number, row_number):
    """Creates an alien and places it in the row"""
    alien = Alien(settings, screen, audio)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * (row_number + 1)
    aliens.add(alien)


def create_fleet(settings, screen, audio, ship, aliens):
    """Creates a full fleet of aliens."""
    # Creates an alien and find the number of aliens in a row.
    alien = Alien(settings, screen)
    number_aliens_x = get_number_aliens_x(settings, alien.rect.width)
    number_rows = get_number_rows(settings, ship.rect.height,
                                  alien.rect.height)

    # Creates the first row of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(settings, screen, audio, aliens, alien_number,
                         row_number)


def check_fleet_edges(settings, aliens):
    """Responds appropriately if an alien has reached an edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break


def change_fleet_direction(settings, aliens):
    """Drops the entire fleet and changes its direction."""
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1


def ship_hit(settings, screen, stats, audio, sb, ship, aliens, bullets,
             alien_bullets):
    """Responds to the ship being hit by an alien."""
    # Pauses the rest of the game while the ship is exploding
    ship.explode()
    
    if stats.ships_left > 0:
        # Updates scoreboard.
        stats.ships_left -= 1
        sb.prep_ships()

        # Empties the lists of aliens and bullets.
        aliens.empty()
        bullets.empty()
        alien_bullets.empty()

        # Creates a new fleet and centers the ship.
        create_fleet(settings, screen, audio, ship, aliens)
        ship.center_ship()
    else:
        # Updates high score if needed.
        check_high_score(stats, sb)

        # Stops the games and displays the mouse cursor.
        stats.game_active = False

        pygame.mouse.set_visible(True)


def check_aliens_bottom(settings, stats, screen, audio, sb, ship, aliens,
                        bullets, alien_bullets):
    """Checks if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treats this the same as if the ship got hit.
            ship_hit(settings, screen, stats, audio, sb, ship, aliens, bullets,
                     alien_bullets)
            break

    
def update_aliens(settings, stats, screen, audio, sb, ship, aliens, bullets,
                  alien_bullets):
    """Checks if the fleet is at an edge, then updates the position 
    of all aliens in the fleet."""
    check_fleet_edges(settings, aliens)

    for alien in aliens:
        alien_bullet = alien.try_shooting()
        if alien_bullet:
            alien_bullets.add(alien_bullet)

    aliens.update()

    # Looks for alien-ship collisions.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(settings, screen, stats, audio, sb, ship, aliens, bullets,
                 alien_bullets)

    # Looks for aliens hitting the bottom of the screen.
    check_aliens_bottom(settings, stats, screen, audio, sb, ship, aliens,
                        bullets, alien_bullets)


def check_high_score(stats, sb):
    """Checks to see if there's a new high score."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def exit_game(settings, stats):
    """Saves and exits the game"""
    # Saves the high score to a 'txt' file.
    with open(settings.high_score_filename, 'w') as high_score_txt:
        high_score_txt.write(str(stats.high_score))

    # Exits the game.
    sys.exit()