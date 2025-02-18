const slider = document.getElementById('price-slider');
const minValue = document.getElementById('price-min');
const maxValue = document.getElementById('price-max');
const minPriceInput = document.getElementById('min-price-input');
const maxPriceInput = document.getElementById('max-price-input');

noUiSlider.create(slider, {
    start: [100, 500], // начальные значения
    connect: true, // соединение между ползунками        
    range: {
        min: 0, // минимальное значение            
        max: 1000  // максимальное значение
    }, step: 50, // шаг изменения значений
});

// Подключаем обработчик события "update" для слайдера    
slider.noUiSlider.on('update', function (values, handle) {
    // values: массив текущих значений ползунков [минимум, максимум]    // handle: индекс обновленного ползунка (0 — левый, 1 — правый)
    if (handle === 0) {
        let minPrice = Math.round(values[0]);
        // Обновляем текст минимального значения (левый ползунок)        
        minValue.textContent = minPrice
        // Запись значения в скрытое поле (для Django)
        minPriceInput.value = minPrice;
    } else {
        let maxPrice = Math.round(values[1]);
        // Обновляем текст максимального значения (правый ползунок)       
        maxValue.textContent = maxPrice
        // Запись значения в скрытое поле (для Django)
        maxPriceInput.value = maxPrice;
    }
});







