/**
   * Устанавливает кольцо (background) для элемента
   * на указанный процент (0..100), используя цвет из data-color.
   */
function updateCircularProgress(element, value) {
    // Безопасность: ограничим в 0..100
    value = Math.min(Math.max(value, 0), 100);

    // Считываем цвет из data-color
    const color = element.getAttribute("data-color") || "#e57373";
    
    // Угол (максимум 270°)
    const angle = (value / 100) * 270;
    
    // Формируем conic-gradient:
    //  - color от 0 до angle (закрашенная часть)
    //  - #ccc от angle до 270° (фон кольца)
    //  - transparent от 270 до 360 (дырка снизу)
    element.style.background = `
      conic-gradient(
        ${color} 0deg,
        ${color} ${angle}deg,
        #ccc ${angle}deg,
        #ccc 270deg,
        transparent 270deg,
        transparent 360deg
      )
    `;
    
    // Обновляем цифру (округлим до целого)
    const span = element.querySelector(".progress-value");
    if (span) {
      span.textContent = Math.round(value);
    }
  }

  /**
   * Плавно анимирует переход от fromValue к toValue за duration (мс).
   */
  function animateProgress(element, fromValue, toValue, duration = 1000) {
    const startTime = performance.now();

    function animate(time) {
      const elapsed = time - startTime;
      const progress = Math.min(elapsed / duration, 1);
      const currentValue = fromValue + (toValue - fromValue) * progress;
      updateCircularProgress(element, currentValue);

      if (progress < 1) {
        requestAnimationFrame(animate);
      }
    }
    requestAnimationFrame(animate);
  }

  document.addEventListener("DOMContentLoaded", () => {
    // Собираем все элементы с классом .circular-progress
    const allProgressElems = document.querySelectorAll(".circular-progress");

    allProgressElems.forEach((element) => {
      // Начальное значение из data-value
      let currentVal = parseFloat(element.getAttribute("data-value")) || 0;
      // Устанавливаем изначально без анимации
      updateCircularProgress(element, currentVal);

      // Каждые 2 секунды анимированно переходим к случайному значению
      setInterval(() => {
        const newVal = Math.random() * 100; // случайное 0..100
        animateProgress(element, currentVal, newVal, 1500);
        currentVal = newVal;
      }, 2000);
    });
});