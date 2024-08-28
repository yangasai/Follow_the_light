<p align="center">
 <img src="https://i.imgur.com/B2GEsgB.png" width="726" length="2000">
</p>

<p align="center">
 <img src="https://img.shields.io/badge/Ren'Py-7.4.11-grin" alt="[Ren'Py Version]">
 <img src="https://img.shields.io/badge/Follow_the_light-1.6-pink" alt="[Game Version]">
 <img src="https://img.shields.io/badge/License-MIT-blue" alt="[License]">
</p>

## About

Following the Light is a visual novel based on the key theme of the Everlasting Summer game. There are many new mechanics available in the game, an updated visual part and a reworking of the main plot with additions.

## Gameplay

<p align="center">
 <img src="https://i.imgur.com/Rjuj3mX.png" width="826" length="2000">
</p>

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Слайдер Скриншотов</title>
    <style>
        .slider {
            width: 300px; /* Ширина слайдера */
            overflow: hidden;
            position: relative;
            margin: auto;
        }
        .slides {
            display: flex;
            transition: transform 0.5s ease;
        }
        .slide {
            min-width: 300px; /* Ширина каждого изображения */
        }
        img {
            width: 100%; /* Автоширина изображений */
            border-radius: 10px; /* Закругление углов */
        }
        button {
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            background-color: rgba(255, 255, 255, 0.7);
            border: none;
            cursor: pointer;
            padding: 10px;
        }
        #prev {
            left: 10px;
        }
        #next {
            right: 10px;
        }
    </style>
</head>
<body>

<div class="slider">
    <div class="slides">
        <div class="slide"><img src="screenshot1.jpg" alt="Скриншот 1"></div>
        <div class="slide"><img src="screenshot2.jpg" alt="Скриншот 2"></div>
        <div class="slide"><img src="screenshot3.jpg" alt="Скриншот 3"></div>
    </div>
    <button id="prev">Назад</button>
    <button id="next">Вперед</button>
</div>

<script>
    let index = 0;
    const slides = document.querySelector('.slides');
    const totalSlides = document.querySelectorAll('.slide').length;

    document.getElementById('next').addEventListener('click', () => {
        index = (index + 1) % totalSlides;
        updateSlider();
    });

    document.getElementById('prev').addEventListener('click', () => {
        index = (index - 1 + totalSlides) % totalSlides;
        updateSlider();
    });

    function updateSlider() {
        const offset = -index * 300; // Ширина слайда
        slides.style.transform = `translateX(${offset}px)`;
    }
</script>

</body>
</html>


There is a lot of interactivity in the game, from quests to simple transitions:

<p align="center">
 <img src="https://i.imgur.com/b9TQg1i.png" width="826" length="2000">
</p>

<p align="center">
 <img src="https://i.imgur.com/WqVXF3N.png" width="826" length="2000">
</p>

## Developers

- [Yandere](https://github.com/yangasai)

## License

The MIT License (MIT)

Copyright © 2024 Yandere


Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
