# import the pygame module, so you can use it
from random import randint
import pygame

# define some commonly used constants
#colors
CAROLINABLUE = (75, 156, 211)
#positions
HALF: int = 320
FOURTH: int = 160
BOTTOM: pygame.Rect = pygame.Rect(0, 639, 640, 1)
BOX1_WIDTH: int = 32 
BOX1_HEIGHT: int = 32 
BOX2_WIDTH: int = 8
BOX2_HEIGHT: int = 32
BOX3_WIDTH: int = 64
BOX3_HEIGHT: int = 32

def main():

    #setup
    pygame.init()
    pygame.display.set_caption("box game!")
    FPS = pygame.time.Clock()
    FPS.tick(60)
    SCREEN = pygame.display.set_mode((640,640))
    SCREEN.fill(CAROLINABLUE)
    running = True

    #init boxes
    boxes: list[Box] = [] #these will be used to draw the boxes 
    boxes_rects: list[pygame.Rect] = [] #these will be used to check for collisions.
    #any box created has to be added to both
    falling_box = Box(SCREEN, (80, 40))
    box_generator: BoxGenerator = BoxGenerator(SCREEN)

    #other init
    tick: int = 1     
    num_boxes: int = 1 

    #flags
    first_box: bool = True

    while running:
        #inputs
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    running = False

        falling_box.move()            
        falling_box.fall()

        #when the first... need first_box flag?
        if falling_box.done:
            tmp = falling_box
            falling_box = box_generator.get_box() 
            num_boxes += 1
            boxes.append(tmp)
            boxes_rects.append(tmp.rect)

        #check for collisions
        if num_boxes > 1:
            for rect in boxes_rects:
                if rect.colliderect(falling_box.rect):
                    tmp = falling_box
                    falling_box = box_generator.get_box()
                    num_boxes += 1
                    boxes.append(tmp)
                    boxes_rects.append(tmp.rect)       


        #update
        SCREEN.fill(CAROLINABLUE)
        falling_box.draw()
        for box in boxes:
            box.draw()
        pygame.display.update()
        FPS.tick(60)

        tick += 1
        if tick == 60:
            tick = 0

        

class Box(pygame.sprite.Sprite):
    """A simple box that rescales the box.png image."""
    image: pygame.Surface
    image_number: int
    rect: pygame.Rect
    dimensions: tuple
    SCREEN: pygame.Surface
    done: bool


    def __init__(self, SCREEN: pygame.display, dimensions: tuple = (32, 32), top_left_start_location: tuple = None, image_number: int = randint(0, 2)):
        super().__init__()
        self.image_number = image_number
        if self.image_number == 0:
            self.image = pygame.image.load("src/box.png")
        elif self.image_number == 1:
            self.image = pygame.image.load("src/box2.png")
        else:
            self.image = pygame.image.load("src/box3.png")
        self.SCREEN = SCREEN
        self.setDimensions(dimensions)
        self.setLocation(top_left_start_location)
        self.done = False

    def draw(self):
        self.SCREEN.blit(self.image, self.rect)
    
    def setDimensions(self, dimensions: tuple):
        self.dimensions = dimensions
        self.image = pygame.transform.scale(self.image, self.dimensions) 
        self.rect = self.image.get_rect()
    
    def setLocation(self, location: tuple):
        if location == None:
            #since we're starting from the top left, we want to go halfway to the right 
            #and move back left by half of the width of the box
            x: int = HALF - self.dimensions[0]/2 
            self.rect.topleft = (x, 0)
        else:
            self.rect.topleft = location
    
    def move(self, amt: tuple = None):
        #check what's pressed this frame
        pressed = pygame.key.get_pressed()
        if not self.done:
            if pressed[pygame.K_LEFT]:
                self.rect.move_ip(-5, 0)
            if pressed[pygame.K_RIGHT]:
                self.rect.move_ip(5, 0)
        
        if amt != None:
           self.rect.topleft = (self.rect.topleft[0] + amt[0], self.rect.topleft[1] + amt[1])
    
    def fall(self):
        if not self.done:
            self.setLocation((self.rect.topleft[0], self.rect.topleft[1] + 5))
        if self.rect.colliderect(BOTTOM):
            self.done = True
    
    def stop_moving(self):
        self.done = True

class BoxGenerator:
    next_box: Box
    SCREEN: pygame.Surface

    def __init__(self, SCREEN: pygame.Surface):
        self.SCREEN = SCREEN
        self.generate_box()
    
    def generate_box(self):
        image_number: int = randint(0, 2)
        match image_number:
            case 0:
                self.next_box = Box(self.SCREEN, (randint(BOX1_HEIGHT, 2 * BOX1_HEIGHT), randint(BOX1_WIDTH, 2 * BOX1_WIDTH)), image_number=image_number)
            case 1:
                self.next_box = Box(self.SCREEN, (randint(2 * BOX2_WIDTH, 3 * BOX2_WIDTH), randint(2 * BOX2_HEIGHT, 3 * BOX2_HEIGHT)), image_number=image_number)
            case _:
                self.next_box = Box(self.SCREEN, (randint(BOX3_WIDTH, 1.5 * BOX3_WIDTH), randint(BOX3_HEIGHT, 1.5 * BOX3_HEIGHT)), image_number=image_number)

    def get_box(self) -> Box: 
        tmp = self.next_box
        self.generate_box()
        return tmp

if __name__=="__main__":
    main()