package org.example;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.Random;
import java.util.LinkedList;

class SnakeGame extends JFrame {
    private final int TILE_SIZE = 25;
    private final int BOARD_WIDTH = 30;
    private final int BOARD_HEIGHT = 20;
    private final int DELAY = 150;

    private LinkedList<Point> snake;
    private Point food;
    private char direction = 'R'; // U, D, L, R
    private boolean running = false;
    private Timer timer;

    private GamePanel gamePanel;

    public SnakeGame() {
        setTitle("Змейка");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setResizable(true);

        gamePanel = new GamePanel();
        add(gamePanel);
        pack();

        setLocationRelativeTo(null);
        addKeyListener(new KeyAdapter());

        initGame();
    }

    private void initGame() {
        snake = new LinkedList<>();
        snake.add(new Point(5, 10));
        snake.add(new Point(4, 10));
        snake.add(new Point(3, 10));

        spawnFood();

        direction = 'R';
        running = true;

        timer = new Timer(DELAY, e -> gameLoop());
        timer.start();
    }

    private void spawnFood() {
        Random rand = new Random();
        int x, y;
        do {
            x = rand.nextInt(BOARD_WIDTH);
            y = rand.nextInt(BOARD_HEIGHT);
        } while (snake.contains(new Point(x, y)));

        food = new Point(x, y);
    }

    private void gameLoop() {
        if (!running) return;

        move();
        checkCollision();
        gamePanel.repaint();
    }

    private void move() {
        Point head = snake.getFirst();
        Point newHead;

        switch (direction) {
            case 'U': newHead = new Point(head.x, head.y - 1); break;
            case 'D': newHead = new Point(head.x, head.y + 1); break;
            case 'L': newHead = new Point(head.x - 1, head.y); break;
            case 'R': newHead = new Point(head.x + 1, head.y); break;
            default: return;
        }

        snake.addFirst(newHead);
        if (newHead.equals(food)) {
            spawnFood();
        } else {
            snake.removeLast();
        }
    }

    private void checkCollision() {
        Point head = snake.getFirst();

        // Проверка столкновения со стенами
        if (head.x < 0 || head.x >= BOARD_WIDTH || head.y < 0 || head.y >= BOARD_HEIGHT) {
            gameOver();
            return;
        }

        // Проверка столкновения с собой (начиная со второго элемента)
        for (int i = 1; i < snake.size(); i++) {
            if (head.equals(snake.get(i))) {
                gameOver();
                return;
            }
        }
    }

    private void gameOver() {
        running = false;
        timer.stop();
        JOptionPane.showMessageDialog(this, "Игра окончена! Счет: " + (snake.size() - 3));
        initGame(); // Перезапуск игры
    }

    private class KeyAdapter extends java.awt.event.KeyAdapter {
        @Override
        public void keyPressed(KeyEvent e) {
            switch (e.getKeyCode()) {
                case KeyEvent.VK_UP:
                    if (direction != 'D') direction = 'U';
                    break;
                case KeyEvent.VK_DOWN:
                    if (direction != 'U') direction = 'D';
                    break;
                case KeyEvent.VK_LEFT:
                    if (direction != 'R') direction = 'L';
                    break;
                case KeyEvent.VK_RIGHT:
                    if (direction != 'L') direction = 'R';
                    break;
                case KeyEvent.VK_SPACE:
                    if (!running) {
                        timer.start();
                        running = true;
                    }
                    break;
            }
        }
    }

    private class GamePanel extends JPanel {
        public GamePanel() {
            setPreferredSize(new Dimension(BOARD_WIDTH * TILE_SIZE, BOARD_HEIGHT * TILE_SIZE));
            setBackground(Color.BLACK);
        }

        @Override
        protected void paintComponent(Graphics g) {
            super.paintComponent(g);

            // Отрисовка змейки
            g.setColor(Color.GREEN);
            for (Point p : snake) {
                g.fillRect(p.x * TILE_SIZE, p.y * TILE_SIZE, TILE_SIZE, TILE_SIZE);
            }

            // Отрисовка головы другим цветом
            if (!snake.isEmpty()) {
                g.setColor(new Color(0, 150, 0));
                g.fillRect(snake.getFirst().x * TILE_SIZE, snake.getFirst().y * TILE_SIZE, TILE_SIZE, TILE_SIZE);
            }

            // Отрисовка еды
            g.setColor(Color.RED);
            g.fillOval(food.x * TILE_SIZE, food.y * TILE_SIZE, TILE_SIZE, TILE_SIZE);

            // Отрисовка сетки
            g.setColor(Color.DARK_GRAY);
            for (int i = 0; i < BOARD_WIDTH; i++) {
                for (int j = 0; j < BOARD_HEIGHT; j++) {
                    g.drawRect(i * TILE_SIZE, j * TILE_SIZE, TILE_SIZE, TILE_SIZE);
                }
            }

            // Отображение счета
            g.setColor(Color.WHITE);
            g.setFont(new Font("Arial", Font.BOLD, 16));
            g.drawString("Счет: " + (snake.size() - 3), 10, 20);
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            new SnakeGame().setVisible(true);
        });
    }
}