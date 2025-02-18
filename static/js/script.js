document.addEventListener("DOMContentLoaded", () => {
    let btn = document.querySelector(".btn_contacs")
    let close = document.querySelector(".btn_close")
    let popup = document.querySelector(".popup")
    let dark = document.querySelector(".dark_filter")
    let circles = document.querySelectorAll(".btn_circle")
    let slides = document.querySelectorAll(".slide")
    let catalog = document.querySelector(".catalog_link")
    let products = document.querySelector(".new_products")
    let basket = document.querySelector(".basket")
    let enter = document.querySelector(".enter")
    let enter_btn = document.querySelector("#enter_btn")
    let search = document.querySelector(".search-form")
    let search_btn = document.querySelector(".search_btn")
    let add_cart_links = document.querySelectorAll(".add_to_cart")
    let cart_btn = document.querySelector(".cart_button")
    let cart_container = document.querySelector(".cart_container")
    let sort = document.querySelector(".sort")
    let catalog_products = document.querySelector(".ice_cream_catalog")
    let goods = Array.from(document.querySelectorAll(".prd"))


    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.startsWith(name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }


    add_cart_links.forEach(link => {
        link.addEventListener('click', function (event) {
            event.preventDefault(); // Останавливаем переход по ссылке

            const url = link.getAttribute('href'); // Получаем URL из ссылки.

            // Отправляем AJAX-запрос
            fetch(url, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'), // Передаём CSRF-токен
                    'Content-Type': 'application/json',
                },
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Успешное добавление: обновляем интерфейс
                    update_cart_button(data.total_count); // Обновляем кнопку корзины.
                    updateCartHTML(data.cart_html);    // Обновляем содержимое корзины.
                } else {
                    // Ошибка
                    console.error(data.error);
                }
            })
            .catch(error => {
                console.error('Ошибка при запросе:', error);
                alert('Произошла ошибка при добавлении товара в корзину.');
            });
        });
    });


    cart_container.addEventListener("click", (event) =>{
        event.preventDefault()
        let target = event.target
        if (target.tagName === "A" && target.classList.contains("delete_from_cart")) {
            let url = target.getAttribute("href")
            fetch(url, {
                method: "POST",
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'), // Передаём CSRF-токен
                    'Content-Type': 'application/json',
                }
            })
            .then(response => response.json())
            .then((data) => {
                if (data.success) {
                    update_cart_button(data.total_count)
                    updateCartHTML(data.cart_html);
                }
                else {
                    console.error(data.error)
                }
            })
            .catch((error) => {
                console.error(error)
                alert("Произошла ошибка при удаление товара из корзины!")
            })
        }
    })

    function update_cart_button(total_count) {
        if (total_count > 0) {
            cart_btn.classList.remove('cart_btn_empty')
            cart_btn.textContent = `${total_count} товар`
        }
        else {
            cart_btn.classList.add('cart_btn_empty')
            cart_btn.textContent = 'Пусто'
        }
    }

    function updateCartHTML(cart_html) {
        cart_container.innerHTML = cart_html
    }

    if (btn) {
        btn.addEventListener("click", () => {
            popup.classList.add("popup_show")
            dark.classList.add("dark")
        })
        close.addEventListener("click", () => {
            popup.classList.remove("popup_show")
            dark.classList.remove("dark")
        })
        for (let [index, element] of circles.entries()) {
            element.addEventListener("click", () => {
                for (let [ind, el] of circles.entries()) {
                    el.classList.remove("btn_circle_active")
                    slides[ind].classList.remove("slide_active")
                }
                element.classList.add("btn_circle_active")
                slides[index].classList.add("slide_active")
            })
        }
        catalog.addEventListener("mouseenter", () => {
            products.classList.add("product_active")

        })
        products.addEventListener("mouseleave", () => {
            products.classList.remove("product_active")
        })

    }

    cart_btn.addEventListener("mouseenter", () => {

        cart_container.classList.add("basket_active")
    })
    cart_container.addEventListener("mouseleave", () => {
        cart_container.classList.remove("basket_active")
    })

    if (enter_btn) {
        enter_btn.addEventListener("mouseenter", () => {
            enter.classList.add("active_enter")
            enter_btn.classList.add("active_enter_btn")
        })
        enter.addEventListener("mouseleave", () => {
            enter.classList.remove("active_enter")
            enter_btn.classList.remove("active_enter_btn")
        })
    }


    search_btn.addEventListener("mouseenter", () => {
        search.classList.add("search_active")
        search_btn.classList.add("search_btn_active")
    })
    search.addEventListener("mouseleave", () => {
        search.classList.remove("search_active")
        search_btn.classList.remove("search_btn_active")
    })

    if (sort) {
        sort.addEventListener("change", (event) => {
            selected_value = event.target.value
            goods.sort((a, b) => {
                if (selected_value == "fat") {
                    let a_fat = parseFloat(a.dataset.fat)
                    let b_fat = parseFloat(b.dataset.fat)
                    return a_fat - b_fat
                }
                if (selected_value == "cheep") {
                    let a_cheep = parseFloat(a.dataset.price)
                    let b_cheep = parseFloat(b.dataset.price)
                    return a_cheep - b_cheep
                }
                if (selected_value == "expensive") {
                    let a_expensive = parseFloat(a.dataset.price)
                    let b_expensive = parseFloat(b.dataset.price)
                    return b_expensive - a_expensive
                }
                if (selected_value == "popular") {
                    let a_popular = a.dataset.popular
                    if (a_popular === "hit") {
                        return -1
                    }
                    else {
                        return 1
                    }
                        
                    
                }
            })
            catalog_products.innerHTML = ""
            goods.forEach(good => catalog_products.appendChild(good))
        })
    }

})





