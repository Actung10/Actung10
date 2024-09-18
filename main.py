import pygame
import random
import time
import sys

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BG_COLOR = (225, 250, 253)

#关卡不同难度图片层数设定
layers_easy = 3
layers_normal = 4
layers_hard = 5
#不同难度时间不同
time_easy = 120
time_normal = 150
time_hard = 180

difficulty = {0:"简单",1:"普通",2:"困难"} #难度

#-----------AI生成代码片段1开始--------------
#排行榜排序
difficulty_order = {'简单': 1, '普通': 2, '困难': 3}
# 定义一个函数，用于从数组元素中提取排序键
def sort_key(item):
    return (+item[0], difficulty_order[item[1]])
#-----------AI生成代码片段1结束--------------

FPS = 30

class Game:
    level = 0 #当前关卡    
    WIDTH, HEIGHT = 800, 860 #窗口大小
    TILE_SIZE = 100 #图标大小
    ROWS, COLS = 6, 6 #行数和列数
    patterns = [pygame.image.load(f"pattern_{i}.png") for i in range(1, ROWS + 1)] #图标
    window_pic = [] #主菜单显示的图标
    board = [] #游戏板
    layers = layers_easy #游戏板层数
    layer_card = [] #游戏板最上层图案的层数
    selected = [] #选择区
    rank = [] #排行榜
    last_oper = [] #历史操作
    history_selected = [] #历史选择区 
    countdown_time = 120

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    font = None #字体

    def __init__(self):
        pygame.init()
        #screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("快乐三连消")

        self.patterns = [pygame.transform.scale(p, (self.TILE_SIZE, self.TILE_SIZE)) for p in self.patterns]

        for i in range(1, 7):  
            image = pygame.image.load(f'pattern_{i}.png').convert_alpha()  # 加载图片
            image = pygame.transform.scale(image, (120, 120))  # 缩放图片到120x120
            if i <= 3:
                image = pygame.transform.rotate(image, 30)
            else:
                image = pygame.transform.rotate(image, 330)
            self.window_pic.append(image)

        self.font = pygame.font.Font("C://Windows//Fonts//STXINWEI.TTF", 25) #字体

        self.main_menu()
    
    #-----------AI生成代码片段2开始-------------- 
    def draw_button(self, text, x, y, width, height, color, screen):
        pygame.draw.rect(screen, color, (x, y, width, height))
        text_surface = self.font.render(text, True, WHITE)
        text_rect = text_surface.get_rect(center=(x + width / 2, y + height / 2))
        screen.blit(text_surface, text_rect)

    # 检查是否点击了按钮
    def is_clicked(self, x, y, button_x, button_y, button_width, button_height):
        return x > button_x and x < button_x + button_width and y > button_y and y < button_y + button_height

    # 主菜单
    def main_menu(self):
        self.level = 0
        clock = pygame.time.Clock()
        running = True
        while running:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if self.is_clicked(mouse_x, mouse_y, 200, 400, 100, 50):
                        self.difficulty_menu()
                    elif self.is_clicked(mouse_x, mouse_y, 350, 400, 100, 50):
                        self.option_menu()
                    elif self.is_clicked(mouse_x, mouse_y, 500, 400, 100, 50):
                        self.rank_menu()

            self.screen.fill(BG_COLOR)
            # 渲染文本
            font2 = pygame.font.Font("C://Windows//Fonts//STXINWEI.TTF", 72)
            text_surface = font2.render("快乐三连消", True, BLACK)
            # 获取文本的矩形区域
            text_rect = text_surface.get_rect()
            # 设置文本显示的位置（偏上部）
            text_rect.topleft = (self.WIDTH // 2 - text_rect.width // 2 + 10, 100)  # 根据实际情况调整位置
            # 将文本渲染到屏幕上
            self.screen.blit(text_surface, text_rect)
            self.draw_button("开始游戏", 200, 400, 100, 50, RED, self.screen)
            self.draw_button("说明", 350, 400, 100, 50, RED, self.screen)
            self.draw_button("排行榜", 500, 400, 100, 50, RED, self.screen)

            for i in range(3):
                x = 25 + i * 90  # 从左向右递增   
                y = 450 + i * 75  # 从下向上递减
                self.screen.blit(self.window_pic[i], (x, y))
            # 右侧阶梯状图片
            for i in range(3, 6):
                x = 625 - (i - 3) * 75  # 从右向左递增
                y = 450 - (3 - i) * 75  # 从下向上递减
                self.screen.blit(self.window_pic[i], (x, y))

            pygame.display.flip()
        pygame.quit()
        sys.exit()
    #-------------AI生成代码片段2结束------------

    #-----------AI生成代码片段3开始--------------
    def difficulty_menu(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.main_menu()  # 按下ESC键时调用主菜单函数
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if self.is_clicked(mouse_x, mouse_y, 300, 300, 200, 50):
                        self.layers = layers_easy
                        self.countdown_time = time_easy
                        self.game_run()
                    elif self.is_clicked(mouse_x, mouse_y, 300, 400, 200, 50):
                        self.layers = layers_normal
                        self.countdown_time = time_normal
                        self.game_run()
                    elif self.is_clicked(mouse_x, mouse_y, 300, 500, 200, 50):
                        self.layers = layers_hard
                        self.countdown_time = time_hard
                        self.game_run()
                    elif self.is_clicked(mouse_x, mouse_y, 650, 750, 100, 50):
                        self.main_menu()

            self.screen.fill(BG_COLOR)
            # 渲染文本
            font3 = pygame.font.Font("C://Windows//Fonts//STXINWEI.TTF", 72)
            text_surface = font3.render("难度选择", True, BLACK)
            # 获取文本的矩形区域
            text_rect = text_surface.get_rect()
            # 设置文本显示的位置（偏上部）
            text_rect.topleft = (self.WIDTH // 2 - text_rect.width // 2 - 5, 100)  # 根据实际情况调整位置
            # 将文本渲染到屏幕上
            self.screen.blit(text_surface, text_rect)
            self.draw_button("简单", 300, 300, 200, 50, RED, self.screen)
            self.draw_button("正常", 300, 400, 200, 50, RED, self.screen)
            self.draw_button("困难", 300, 500, 200, 50, RED, self.screen)
            self.draw_button("返回", 650, 750, 100, 50, RED, self.screen)
            pygame.display.flip()

        pygame.quit()
        sys.exit()
    #-----------AI生成代码片段3结束--------------

    #-----------AI生成代码片段4开始-------------- 
    def option_menu(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if self.is_clicked(mouse_x, mouse_y, 650, 750, 100, 50):
                        self.main_menu()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.main_menu()  # 按下ESC键时调用主菜单函数
            # 填充背景色
            self.screen.fill(BG_COLOR)
            # 渲染文本
            text_lines = [
                "Ctrl + Z或通关键: 直接通过当前关卡",
                "Ctrl + C或撤销键: 撤销上一步操作，可无限撤消",
                "ESC : 退出到主菜单界面",
                "点击图片可将图片移动到选择区，选择区内有三张相同的图片即可消除",
                "简单难度图案有三层，普通难度图案有四层，困难难度图案有五层",
                "前两关均有办法通关，后面关卡则有20%概率一定有办法通关",
                "排行榜最多只显示通关数最高的五个数据"
            ]
            y_offset = 270  # 文本起始的垂直位置
            for i, line in enumerate(text_lines):
                font4 = pygame.font.Font("C://Windows//Fonts//STXINWEI.TTF", 25)
                text_surface = font4.render(line, True, BLACK)
                text_rect = text_surface.get_rect(center=(self.WIDTH // 2, y_offset + i * 50))  # 每行文字间隔50像素
                self.draw_button("返回", 650, 750, 100, 50, RED, self.screen)
                self.screen.blit(text_surface, text_rect)

            # 更新屏幕显示
            pygame.display.flip()
        pygame.quit()
        sys.exit()
    #-----------AI生成代码片段4结束-------------- 

    #-----------AI生成代码片段5开始--------------
    def rank_menu(self):
        running = True
        font5 = pygame.font.Font("C://Windows//Fonts//STXINWEI.TTF", 72)
        small_font = pygame.font.Font("C://Windows//Fonts//STXINWEI.TTF", 40)

        rankings = sorted(self.rank, key=sort_key, reverse=True)[:5]
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if self.is_clicked(mouse_x, mouse_y, 650, 750, 100, 50):
                        self.main_menu()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.main_menu()  # 按下ESC键时调用主菜单函数
            # 填充背景色
            self.screen.fill(BG_COLOR)

            # 渲染排行榜标题
            title_surface = font5.render("排行榜", True, BLACK)
            title_rect = title_surface.get_rect()
            title_rect.topleft = (self.WIDTH // 2 - title_rect.width // 2, 80)
            self.screen.blit(title_surface, title_rect)

            # 绘制表格标题
            header_rank_surface = small_font.render("排名", True, BLACK)
            header_rank_rect = header_rank_surface.get_rect(center=(200, 300))
            self.screen.blit(header_rank_surface, header_rank_rect)

            header_level_surface = small_font.render("通关数", True, BLACK)
            header_level_rect = header_level_surface.get_rect(center=(600, 300))
            self.screen.blit(header_level_surface, header_level_rect)

            # 绘制表格数据
            data_start_y = 360
            for i, ranking in enumerate(rankings):
                if ranking[0] == 0:
                    continue
                rank_surface = small_font.render(str(i + 1), True, BLACK)
                rank_rect = rank_surface.get_rect(center=(200, data_start_y + i * 60))
                self.screen.blit(rank_surface, rank_rect)

                rank_text = str(ranking[0]) + '(' + ranking[1] + ')'
                level_surface = small_font.render(rank_text, True, BLACK)
                level_rect = level_surface.get_rect(center=(600, data_start_y + i * 60))
                self.screen.blit(level_surface, level_rect)

            self.draw_button("返回", 650, 750, 100, 50, RED, self.screen)
            # 更新屏幕显示
            pygame.display.flip()
        pygame.quit()
        sys.exit()
    #-----------AI生成代码片段5结束--------------

    #-----------AI生成代码片段6开始--------------
    def success_window(self):
        running = True
        font6 = pygame.font.Font("C://Windows//Fonts//STXINWEI.TTF", 50)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.rank.append((self.level, difficulty[self.layers - 3]))
                        self.main_menu()  # 按下ESC键时调用主菜单函数
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if self.is_clicked(mouse_x, mouse_y, self.WIDTH // 2 + 50, level_rect.bottom + 100, 150, 50):
                        self.rank.append((self.level, difficulty[self.layers - 3]))
                        self.main_menu()
                    elif self.is_clicked(mouse_x, mouse_y, self.WIDTH // 2 - 200, level_rect.bottom + 100, 150, 50):
                        self.game_run()

            self.screen.fill(BG_COLOR)

            # 显示恭喜信息
            congrats_text = font6.render("恭喜您，通过此关", True, BLACK)
            congrats_rect = congrats_text.get_rect(center=(self.WIDTH // 2, 200))
            self.screen.blit(congrats_text, congrats_rect)

            # 显示已通过的关卡数
            level_text = font6.render(f"您已通过{self.level}关", True, BLACK)
            level_rect = level_text.get_rect(center=(self.WIDTH // 2, congrats_rect.bottom + 75))
            self.screen.blit(level_text, level_rect)

            # 绘制按钮
            next_level_button = pygame.Rect(self.WIDTH // 2 - 150, level_rect.bottom + 50, 150, 50)
            main_menu_button = pygame.Rect(self.WIDTH // 2 + 150, level_rect.bottom + 50, 150, 50)
            self.draw_button("下一关", self.WIDTH // 2 - 200, level_rect.bottom + 100, 150, 50, RED, self.screen)
            self.draw_button("返回主菜单", self.WIDTH // 2 + 50, level_rect.bottom + 100, 150, 50, RED, self.screen)

            pygame.display.flip()
        pygame.quit()
        sys.exit()
    
    def fail_window(self):
        running = True
        font6 = pygame.font.Font("C://Windows//Fonts//STXINWEI.TTF", 50)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.rank.append((self.level - 1, difficulty[self.layers - 3]))
                        self.main_menu()  # 按下ESC键时调用主菜单函数
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if self.is_clicked(mouse_x, mouse_y, self.WIDTH // 2 - 75, level_rect.bottom + 100, 150, 50):
                        self.rank.append((self.level - 1, difficulty[self.layers - 3]))
                        self.main_menu()

            self.screen.fill(BG_COLOR)

            # 显示信息
            congrats_text = font6.render("很遗憾，游戏失败", True, BLACK)
            congrats_rect = congrats_text.get_rect(center=(self.WIDTH // 2, 200))
            self.screen.blit(congrats_text, congrats_rect)

            # 显示已通过的关卡数
            level_text = font6.render(f"您已通过{self.level - 1}关", True, BLACK)
            level_rect = level_text.get_rect(center=(self.WIDTH // 2, congrats_rect.bottom + 75))
            self.screen.blit(level_text, level_rect)

            # 绘制按钮
            main_menu_button = pygame.Rect(self.WIDTH // 2 + 150, level_rect.bottom + 50, 150, 50)
            self.draw_button("返回主菜单", self.WIDTH // 2 - 75, level_rect.bottom + 100, 150, 50, RED, self.screen)

            pygame.display.flip()
        pygame.quit()
        sys.exit()
    #-----------AI生成代码片段6结束--------------

    def judge(self, x, y, r, c):
        if 100 + 1 * self.layer_card[r][c] + c * self.TILE_SIZE <= x and 100 + 1 * self.layer_card[r][c] + (c + 1) * self.TILE_SIZE >= x and 100 + 1 * self.layer_card[r][c] + r * self.TILE_SIZE <= y and 100 + 1 * self.layer_card[r][c] + (r + 1) * self.TILE_SIZE >= y:
            return True
        return False

    def draw_board(self):
        for i in range(self.layers):
            for row in range(self.ROWS):
                for col in range(self.COLS):
                    tile = self.board[i][row][col]
                    if tile is not None:
                        self.screen.blit(tile, (100 + 1 * i + col * self.TILE_SIZE, 100 + 1 * i + row * self.TILE_SIZE)) #让不同层的图片稍微偏一点，有点层次感
    
    def draw_selcted(self):
        x_offset = 100  # 图片的起始x坐标
        y_offset = 760  # 图片的起始y坐标
        for i, image in enumerate(self.selected):
            # 计算每张图片的位置
            x = x_offset + (i % (600 // 100)) * 100
            y = y_offset
            self.screen.blit(image, (x, y))

    def check_match(self):
        if len(self.selected) >= 3:
            for i in range(len(self.selected) - 2):
                for j in range(i + 1, len(self.selected) - 1):
                    if self.selected[i] == self.selected[j] and self.selected[i] == self.selected[len(self.selected) - 1]:
                        self.selected.pop(len(self.selected) - 1)
                        self.selected.pop(j)
                        self.selected.pop(i)
                        break
    
    def cancel(self):
        if self.last_oper:
            l1, r1, c1, img1 = self.last_oper[len(self.last_oper) - 1]
            self.board[l1][r1][c1] = img1
            self.layer_card[r1][c1] += 1
            self.last_oper = self.last_oper[:-1]
            self.selected.clear()
            if self.history_selected:
                last_selected = self.history_selected[-1]
                for surface in last_selected:
                    self.selected.append(surface)
            self.history_selected = self.history_selected[:-1]

    def success_judge(self):
        for i in range(len(self.layer_card)):
            for j in range(len(self.layer_card[i])):
                if self.layer_card[i][j] != -1:
                    return False
        if len(self.selected) == 0:
            return True
        else:
            return False

    def game_run(self):
        running = True
        clock = pygame.time.Clock()

        #当前关卡
        self.level += 1
        #数组清理
        self.board.clear()
        self.selected.clear()
        self.layer_card.clear()
        self.last_oper.clear()
        self.history_selected.clear()
        #预处理
        if self.level <= 2:
            for l in range(self.layers):
                arr = []
                for i in range(self.ROWS):
                    for j in range(self.COLS):
                        arr.append(i + 1)
                random.shuffle(arr)
                board_row = []
                for a in range(self.ROWS):
                    board_col = []
                    for b in range(self.COLS):
                        board_col.append(self.patterns[arr[self.COLS * a + b] - 1])
                    board_row.append(board_col)
                self.board.append(board_row)                 
        else:
            random_number = random.randint(1, 10)
            if random_number <= 2:
                for l in range(self.layers):
                    arr = []
                    for i in range(self.ROWS):
                        for j in range(self.COLS):
                            arr.append(i + 1)
                    random.shuffle(arr)
                    board_row = []
                    for a in range(self.ROWS):
                        board_col = []
                        for b in range(self.COLS):
                            board_col.append(self.patterns[arr[self.COLS * a + b] - 1])
                        board_row.append(board_col)
                    self.board.append(board_row)
            else:
                for i in range(self.layers):
                    self.board.append([[random.choice(self.patterns) for _ in range(self.COLS)] for _ in range(self.ROWS)])
                
        for i in range(self.ROWS):
            layer_card_row = []
            for j in range(self.COLS):
                layer_card_row.append(self.layers - 1)
            self.layer_card.append(layer_card_row)

        start_time = time.time()  # 获取当前时间

        while running:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.rank.append((self.level - 1, difficulty[self.layers - 3]))
                        self.main_menu()  # 按下ESC键时调用主菜单函数
                    elif event.key == pygame.K_z and pygame.key.get_mods() & pygame.KMOD_CTRL:#直接通过本关
                        self.success_window()
                    elif event.key == pygame.K_c and pygame.key.get_mods() & pygame.KMOD_CTRL:#撤销
                        self.cancel()
                elif event.type == pygame.MOUSEBUTTONDOWN:#消除
                    x, y = event.pos
                    if self.is_clicked(x, y, self.WIDTH - 80, 100, 70, 40):
                        self.cancel()
                    elif self.is_clicked(x, y, self.WIDTH - 80, 150, 70, 40):
                        self.success_window()
                    else:
                        for r in range(self.ROWS):
                            for c in range(self.COLS):
                                if self.judge(x, y, r, c):
                                    row = r
                                    col = c
                                    break
                        l = self.layer_card[row][col]
                        if self.board[l][row][col] is not None and len(self.selected) < 6:
                            self.history_selected.append(self.selected.copy())
                            self.selected.append(self.board[l][row][col])
                            self.last_oper.append((l, row, col, self.board[l][row][col]))
                            self.board[l][row][col] = None
                            self.layer_card[row][col] -= 1;
                        if len(self.selected) >= 3:
                            self.check_match()

            # 计算剩余时间
            elapsed_time = time.time() - start_time
            remaining_time = int(self.countdown_time - elapsed_time)
            #倒计时结束游戏失败
            if remaining_time <= 0:
                self.fail_window()

            #画图
            self.screen.fill(BG_COLOR)
            self.draw_board()

            black_frame = pygame.Rect((self.WIDTH // 2) - (600 // 2), self.HEIGHT - 100, 600, 100)
            pygame.draw.rect(self.screen, (251,253, 208), black_frame)
            text = "选择区(最大容量：6)"
            text_surface = self.font.render(text, True, BLACK)
            text_rect = text_surface.get_rect()
            # 将文本定位到框的左上方，稍微高于框的上边缘
            text_rect.topleft = (black_frame.x - 95, black_frame.y - text_rect.height - 10)
            self.screen.blit(text_surface, text_rect)

            self.draw_selcted()

            #当前关卡文本
            title_surface = self.font.render(f"当前关卡： {self.level}", True, BLACK)
            title_rect = title_surface.get_rect()
            title_rect.topleft = (25, 25)
            self.screen.blit(title_surface, title_rect)
            # 倒计时文本
            countdown_text = self.font.render(f"剩余时间：{remaining_time}秒", True, BLACK)
            countdown_rect = countdown_text.get_rect()
            countdown_rect.topright = (self.WIDTH - 10, 25)  # 将文本定位到右上角
            self.screen.blit(countdown_text, countdown_rect)
            #撤销键
            cancel_button = pygame.Rect(self.WIDTH - 80, 70, 70, 40)
            pygame.draw.rect(self.screen, (251,253, 208), (self.WIDTH - 80, 100, 70, 40))
            canceltext_surface = self.font.render("撤销", True, BLACK)
            canceltext_rect = canceltext_surface.get_rect(center=(self.WIDTH - 45, 120))
            self.screen.blit(canceltext_surface, canceltext_rect)

            success_button = pygame.Rect(self.WIDTH - 80, 150, 70, 40)
            pygame.draw.rect(self.screen, (251,253, 208), (self.WIDTH - 80, 150, 70, 40))
            successtext_surface = self.font.render("通关", True, BLACK)
            successtext_rect = successtext_surface.get_rect(center=(self.WIDTH - 45, 170))
            self.screen.blit(successtext_surface, successtext_rect)

            pygame.display.flip()
            if self.success_judge():
                self.success_window()
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    game = Game()