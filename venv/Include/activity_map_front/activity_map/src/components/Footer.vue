<script setup>

</script>

<template>
    <div class="container">
        <div class="links">

            <div class="account">
                <span class="title">
                    Ваш аккаунт
                </span>

                <div class="line"></div>

                <span class="varinat">
                    Войти
                </span>

                <span class="varinat">
                    Регистрации
                </span>
            </div>

            <div class="sections">
                <span class="title">
                    Разделы
                </span>

                <div class="line"></div>

                <span class="varinat">
                    Афиша
                </span>

                <span class="varinat"> 
                    Категории
                </span>

                <span class="varinat">
                    Карта
                </span>

                <span class="varinat">
                    Архив мероприятий
                </span>
            </div>

            <div class="information">
                <span class="title">
                    Информация
                </span>

                <div class="line"></div>

                <span class="varinat">
                    Соглашение
                </span>

                <span class="varinat"> 
                    Документы
                </span>

                <span class="varinat">
                    Конфиденциальность
                </span>
            </div>
        </div>

        <div class="copytight">
            <span class="inf">
                © 2022, fsociety
            </span>

            <span class="tech-supp">
                Техническая поддержка
            </span>

            <div class="icons">
                <img class="telegram" src="../assets/Footer/Telegram.svg" width="30" height="30" alt="image format png" />
                <img class="vk" src="../assets/Footer/VK.svg" width="30" height="30" alt="image format png" />
            </div>
        </div>
    </div>
</template>

<style scoped>
    .container {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #696969;
        color: white;
        text-align: center;
    }

    .copytight {
        display: flex;
        flex-direction: row;
        background-color: #2E3435;
        height: 41px;
        margin-top: 37px;
    }

    .icons {
        padding-top: 6px;
        padding-bottom: 5px;
        padding-left: 155px;
    }

    .vk{
        padding-left: 8px;
    }

    .inf{
        padding-left: 418px;
        padding-top: 11px;
        padding-bottom: 11px;
        padding-right: 155px;
        color: #A0A3A6;
        font-weight: bold;
        font-size: 16px;
    }

    .tech-supp{
        padding-left: 155px;
        padding-right: 155px;
        font-weight: bold;
        font-size: 16px;
        color: #02C0B8;
        padding-top: 11px;
        padding-bottom: 11px;
    }

    .links{
        text-align: left;
        display: flex;
        flex-direction: row;
    }

    .account{
        display: flex;
        flex-direction: column;
        padding-top: 7px;
        font-size: 14px;
        padding-left: 580px;
        padding-right: 40px;
    }

    .sections{
        display: flex;
        flex-direction: column;
        padding-top: 7px;
        font-size: 14px;
        padding-left: 40px;
        padding-right: 40px;
    }

    .information{
        display: flex;
        flex-direction: column;
        padding-top: 7px;
        font-size: 14px;
        padding-left: 50px;
        padding-right: 580px;
    }

    .title{
        color: #FFFFFF;
        font-weight: bold;
    }

    .line{
        border-bottom: 1px solid #FFFFFF;
        width: 200px;
        padding-top: 6px;
    }

    .varinat{
        padding-top: 6px;
        color: #A0A3A6;
    }
</style>