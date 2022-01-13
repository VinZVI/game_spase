class Stats():
    """отслеживание статистики"""

    def __init__(self):
        """инициализирует статистику"""
        self.reset_stats()
        self.run_game = True
        self.high_score = 0

    def reset_stats(self):
        """статистика изменяющаюся во время игры"""
        self.guns_left = 2 # жизни игрока
        self.score = 0  # текущий счет