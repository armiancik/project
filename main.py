import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from figure import Figure


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background = pygame.image.load('F:/pythonProject2/images/board.png')
        self.display_surface = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.board = pygame.sprite.Group()

    def start(self):

        Figure(color='white', x=0, y=300, fType='бел_пешка1',
               image="images/white_pawn.png", groups=self.board)
        Figure(color='white', x=50, y=300, fType='бел_пешка2',
               image="images/white_pawn.png", groups=self.board)
        Figure(color='white', x=100, y=300, fType='бел_пешка3',
               image="images/white_pawn.png", groups=self.board)
        Figure(color='white', x=150, y=300, fType='бел_пешка4',
               image="images/white_pawn.png", groups=self.board)
        Figure(color='white', x=200, y=300, fType='бел_пешка5',
               image="images/white_pawn.png", groups=self.board)
        Figure(color='white', x=250, y=300, fType='бел_пешка6',
               image="images/white_pawn.png", groups=self.board)
        Figure(color='white', x=300, y=300, fType='бел_пешка7',
               image="images/white_pawn.png", groups=self.board)
        Figure(color='white', x=350, y=300, fType='бел_пешка8',
               image="images/white_pawn.png", groups=self.board)
        Figure(color='black', x=0, y=50, fType='чер_пешка1',
               image="images/black_pawn.png", groups=self.board)
        Figure(color='black', x=50, y=50, fType='чер_пешка2',
               image="images/black_pawn.png", groups=self.board)
        Figure(color='black', x=100, y=50, fType='чер_пешка3',
               image="images/black_pawn.png", groups=self.board)
        Figure(color='black', x=150, y=50, fType='чер_пешка4',
               image="images/black_pawn.png", groups=self.board)
        Figure(color='black', x=200, y=150, fType='чер_пешка5',
               image="images/black_pawn.png", groups=self.board)
        Figure(color='black', x=250, y=50, fType='чер_пешка6',
               image="images/black_pawn.png", groups=self.board)
        Figure(color='black', x=300, y=50, fType='чер_пешка7',
               image="images/black_pawn.png", groups=self.board)
        Figure(color='black', x=350, y=50, fType='чер_пешка8',
               image="images/black_pawn.png", groups=self.board)
        Figure(color='white', x=50, y=350, fType='бел_конь1',
               image="images/white_knight.png", groups=self.board)
        Figure(color='white', x=300, y=350, fType='бел_конь2',
               image="images/white_knight.png", groups=self.board)
        Figure(color='black', x=50, y=0, fType='чер_конь1',
               image="images/black_knight.png", groups=self.board)
        Figure(color='black', x=300, y=0, fType='чер_конь2',
               image="images/black_knight.png", groups=self.board)
        Figure(color='white', x=100, y=350, fType='бел_слон1',
               image="images/white_bishop.png", groups=self.board)
        Figure(color='white', x=250, y=350, fType='бел_слон2',
               image="images/white_bishop.png", groups=self.board)
        Figure(color='black', x=250, y=0, fType='чер_слон1',
               image="images/black_bishop.png", groups=self.board)
        Figure(color='black', x=100, y=0, fType='чер_слон2',
               image="images/black_bishop.png", groups=self.board)
        Figure(color='white', x=0, y=350, fType='бел_ладья1',
               image="images/white_rook.png", groups=self.board)
        Figure(color='white', x=350, y=350, fType='бел_ладья2',
               image="images/white_rook.png", groups=self.board)
        Figure(color='black', x=0, y=0, fType='чер_ладья1',
               image="images/black_rook.png", groups=self.board)
        Figure(color='black', x=350, y=0, fType='чер_ладья2',
               image="images/black_rook.png", groups=self.board)
        Figure(color='white', x=200, y=350, fType='бел_королева1',
               image="images/white_queen.png", groups=self.board)
        Figure(color='white', x=150, y=350, fType='бел_король2',
               image="images/white_king.png", groups=self.board)
        Figure(color='white', x=200, y=0, fType='чер_королева1',
               image="images/black_queen.png", groups=self.board)
        Figure(color='white', x=150, y=0, fType='чер_король2',
               image="images/black_king.png", groups=self.board)

    def run(self):
        isRun = True
        self.start()
        while isRun:
            self.clock.tick(FPS)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    isRun = False
            self.screen.blit(self.background, (0, 0))
            self.board.draw(self.display_surface)
            self.board.update(events)
            pygame.display.update()
        pygame.quit()


pygame.init()
game = Game()
game.run()
